// src/main/java/com/mk/post_service/service/CommentService.java

package com.mk.post_service.service;

import com.mk.post_service.dto.CommentRequest;
import com.mk.post_service.dto.CommentResponse;
import com.mk.post_service.entity.Comment;
import com.mk.post_service.entity.Post;
import com.mk.post_service.repository.CommentRepository;
import com.mk.post_service.repository.PostRepository;

// ⭐ 수정: ParameterizedTypeReference 임포트 (WebClient 제네릭 타입 처리)
import org.springframework.core.ParameterizedTypeReference; 
import lombok.extern.slf4j.Slf4j; 
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.reactive.function.client.WebClient; 
import reactor.core.publisher.Mono;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Slf4j 
@Service
@Transactional
public class CommentService {
    private final CommentRepository commentRepository;
    private final PostRepository postRepository;
    private final WebClient webClient; // WebClient 인스턴스

    // ⭐ 1. WebClient.Builder 주입 및 User Service URL 설정
    public CommentService(
        CommentRepository commentRepository, 
        PostRepository postRepository, 
        WebClient.Builder webClientBuilder,
        @Value("${user.service.url}") String userServiceBaseUrl // 설정값을 생성자 주입
    ) {
        this.commentRepository = commentRepository;
        this.postRepository = postRepository;
        // User Service의 기본 URL로 WebClient 인스턴스 생성
        this.webClient = webClientBuilder.baseUrl(userServiceBaseUrl).build();
    }
    
    // =========================================================================
    // ⭐ MSA 통신을 위한 닉네임 일괄 조회 유틸리티 메서드 (PostService와 동일)
    // =========================================================================
    private Map<String, String> getAuthorNicknamesMap(List<String> authorIds) {
        if (authorIds.isEmpty()) {
            return Map.of();
        }
        
        try {
            // POST /nicknames/batch 로 ID 목록을 전송하고 닉네임 맵을 받음
            Mono<Map<String, String>> mono = webClient.post()
                    .uri("/nicknames/batch") 
                    .bodyValue(authorIds)
                    .retrieve()
                    .onStatus(status -> status.is4xxClientError() || status.is5xxServerError(), 
                              clientResponse -> Mono.error(new RuntimeException("User Service 통신 오류: " + clientResponse.statusCode())))
                    // ⭐ 수정: ParameterizedTypeReference를 사용하여 복합 타입(Map) 처리
                    .bodyToMono(new ParameterizedTypeReference<Map<String, String>>() {}); 
            
            return mono.block(); // 동기 호출
            
        } catch (Exception e) {
            log.error("User Service에서 닉네임 정보를 가져오는 중 오류 발생: {}", e.getMessage(), e);
            return authorIds.stream()
                .collect(Collectors.toMap(id -> id, id -> "[통신 오류]")); 
        }
    }

    // =========================================================================
    // 2. 댓글 작성 (POST /api/posts/{postId}/comments) - 닉네임 조회 적용
    // =========================================================================
    @Transactional
    public CommentResponse createComment(Long postId, CommentRequest request, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        Comment comment = new Comment();
        comment.setContent(request.getContent());
        comment.setPost(post);
        comment.setAuthorId(authenticatedUserId); // ⭐ 인증된 사용자 ID 설정

        Comment savedComment = commentRepository.save(comment);

        // 응답 생성 시 닉네임 조회 및 설정
        CommentResponse response = CommentResponse.fromEntity(savedComment);
        
        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(savedComment.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(savedComment.getAuthorId(), "[알 수 없음]");
        response.setAuthorNickname(nickname);

        return response;
    }
    
    // =========================================================================
    // 3. 댓글 조회 (GET /api/posts/{postId}/comments) - 닉네임 일괄 조회 적용
    // =========================================================================
    @Transactional(readOnly = true)
    public List<CommentResponse> getCommentsByPostId(Long postId) {
        List<Comment> comments = commentRepository.findByPost_IdOrderByCreatedAtDesc(postId);

        // 1. 모든 댓글 작성자의 authorId 추출
        List<String> authorIds = comments.stream()
            .map(Comment::getAuthorId)
            .distinct() 
            .collect(Collectors.toList());

        // 2. User Service에서 닉네임 맵 일괄 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // 3. CommentResponse로 변환 및 닉네임 설정
        return comments.stream()
                .map(comment -> {
                    CommentResponse response = CommentResponse.fromEntity(comment);
                    String nickname = nicknameMap.getOrDefault(comment.getAuthorId(), "[알 수 없음]");
                    response.setAuthorNickname(nickname);
                    return response;
                })
                .collect(Collectors.toList());
    }

    // =========================================================================
    // 4. 댓글 수정 (PUT /api/posts/comments/{commentId}) - 닉네임 단건 조회 적용
    // =========================================================================
    @Transactional
    public CommentResponse updateComment(Long commentId, CommentRequest request, String authenticatedUserId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("댓글을 찾을 수 없습니다."));

        // 권한 확인: 댓글 작성자의 ID와 인증된 사용자 ID가 일치해야 함
        if (!comment.getAuthorId().equals(authenticatedUserId)) { 
            throw new RuntimeException("댓글 수정 권한이 없습니다.");
        }
        
        comment.setContent(request.getContent());

        // 응답 생성 시 닉네임 조회 및 설정
        CommentResponse response = CommentResponse.fromEntity(comment);
        
        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(comment.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(comment.getAuthorId(), "[알 수 없음]");
        response.setAuthorNickname(nickname);
        
        return response;
    }
    
    // =========================================================================
    // 5. 댓글 삭제 (DELETE /api/posts/comments/{commentId}) - 권한 확인
    // =========================================================================
    @Transactional
    public void deleteComment(Long commentId, String authenticatedUserId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("댓글을 찾을 수 없습니다."));

        // 권한 확인
        if (!comment.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("댓글 삭제 권한이 없습니다.");
        }
        
        commentRepository.delete(comment);
    }
}