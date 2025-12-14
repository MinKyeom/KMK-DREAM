// src/main/java/com/mk/post_service/service/CommentService.java

package com.mk.post_service.service;

import com.mk.post_service.dto.CommentRequest;
import com.mk.post_service.dto.CommentResponse;
import com.mk.post_service.entity.Comment;
import com.mk.post_service.entity.Post;
import com.mk.post_service.repository.CommentRepository;
import com.mk.post_service.repository.PostRepository;

import org.springframework.core.ParameterizedTypeReference;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value; 
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException; 
import reactor.core.publisher.Mono;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.Collections;

@Slf4j
@Service
@Transactional
public class CommentService {
    private final CommentRepository commentRepository;
    private final PostRepository postRepository;
    private final WebClient webClient; 

    // WebClient.Builder 주입 및 User Service URL 설정
    public CommentService(
        CommentRepository commentRepository,
        PostRepository postRepository,
        WebClient.Builder webClientBuilder,
        @Value("${user.service.url}") String userServiceUrl // ⭐ 수정: user-service.url -> user.service.url
    ) {
        this.commentRepository = commentRepository;
        this.postRepository = postRepository;
        this.webClient = webClientBuilder.baseUrl(userServiceUrl).build();
    }


    // =========================================================================
    // 1. 댓글 작성 (POST /api/posts/{postId}/comments)
    // =========================================================================
    @Transactional
    public CommentResponse createComment(Long postId, CommentRequest request, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
                .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        Comment comment = Comment.builder()
                .content(request.getContent())
                .authorId(authenticatedUserId) // 인증된 사용자 ID 설정
                .post(post)
                .build();

        comment = commentRepository.save(comment);

        // 응답 생성 시 닉네임 조회 및 설정
        CommentResponse response = CommentResponse.fromEntity(comment);

        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(comment.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(comment.getAuthorId(), "[알 수 없음]");
        response.setAuthorNickname(nickname);

        return response;
    }

    // =========================================================================
    // 2. 댓글 목록 조회 (GET /api/posts/{postId}/comments)
    // =========================================================================
    @Transactional(readOnly = true)
    public List<CommentResponse> getCommentsByPostId(Long postId) {
        List<Comment> comments = commentRepository.findByPost_IdOrderByCreatedAtDesc(postId);

        if (comments.isEmpty()) {
            return Collections.emptyList();
        }

        // 닉네임 일괄 조회
        List<String> authorIds = comments.stream()
                .map(Comment::getAuthorId)
                .distinct()
                .collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // CommentResponse 매핑 및 닉네임 설정
        return comments.stream()
                .map((Comment comment) -> { // ✅ 수정: 람다식 입력 타입 (Comment comment) 명시
                    CommentResponse response = CommentResponse.fromEntity(comment);
                    String nickname = nicknameMap.getOrDefault(comment.getAuthorId(), "[알 수 없음]");
                    response.setAuthorNickname(nickname);
                    return response;
                })
                .collect(Collectors.toList());
    }

    // =========================================================================
    // 3. 댓글 수정 (PUT /api/posts/comments/{commentId})
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
    // 4. 댓글 삭제 (DELETE /api/posts/comments/{commentId})
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
    
    // =========================================================================
    // 5. 닉네임 일괄 조회 (User Service와의 통신)
    // =========================================================================
    private Map<String, String> getAuthorNicknamesMap(List<String> authorIds) {
        if (authorIds.isEmpty()) {
            return Collections.emptyMap();
        }

        try {
            // URL: /api/users/nicknames (User Service)
            Mono<Map<String, String>> mono = webClient.post()
                    .uri("/api/users/nicknames")
                    .bodyValue(authorIds) // 사용자 ID 목록 전송
                    .retrieve()
                    // WebClient ResponseException 처리는 주석 처리 (현재 provided file에 없음)
                    .bodyToMono(new ParameterizedTypeReference<Map<String, String>>() {}); // 응답 타입 (Map<String, String>)

            // 블로킹 호출 (Microservice 간 동기 통신)
            Map<String, String> nicknames = mono.block();
            
            return nicknames != null ? nicknames : Collections.emptyMap();

        } catch (Exception e) {
            log.error("User Service에서 닉네임 조회 실패: {}", e.getMessage());
            // 서비스 장애 격리를 위해 빈 맵 반환
            return Collections.emptyMap();
        }
    }
}