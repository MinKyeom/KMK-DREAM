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
import org.springframework.beans.factory.annotation.Value; // @Value 임포트는 그대로 유지
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException; // WebClient 예외 처리용 추가
import reactor.core.publisher.Mono;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.Collections; // Collections 임포트 추가

@Slf4j
@Service
@Transactional
public class CommentService {
    private final CommentRepository commentRepository;
    private final PostRepository postRepository;
    private final WebClient webClient; // WebClient 인스턴스

    // ⭐ 수정: WebClient.Builder 주입 및 User Service URL 설정
    public CommentService(
        CommentRepository commentRepository,
        PostRepository postRepository,
        WebClient.Builder webClientBuilder,
        @Value("${user-service.url}") String userServiceUrl // ⭐ URL을 생성자에서 직접 주입
    ) {
        this.commentRepository = commentRepository;
        this.postRepository = postRepository;
        // ⭐ WebClient 초기화 시 주입된 userServiceUrl 사용 (안전함)
        this.webClient = webClientBuilder.baseUrl(userServiceUrl).build();
    }


    // =========================================================================
    // 2. WebClient를 사용한 닉네임 조회 메서드 (일괄 조회) - 오류 복구 로직 포함
    // =========================================================================
    /**
     * User Service에서 사용자 ID 목록을 기반으로 닉네임 맵을 조회합니다.
     * WebClient 통신 오류 시 빈 맵을 반환하여 서비스 장애를 격리(Circuit Breaking)합니다.
     */
    private Map<String, String> getAuthorNicknamesMap(List<String> authorIds) {
        if (authorIds.isEmpty()) {
            return Collections.emptyMap();
        }

        try {
            // URL: /api/users/nicknames (User Service)
            Mono<Map<String, String>> mono = webClient.post()
                    .uri("/api/users/nicknames")
                    .bodyValue(authorIds)
                    .retrieve()
                    .bodyToMono(new ParameterizedTypeReference<Map<String, String>>() {});

            return mono.block();

        } catch (WebClientResponseException e) {
             // 4xx, 5xx 에러 발생 시 처리
            log.error("User Service 닉네임 조회 실패 (HTTP Status {}): {}", e.getStatusCode(), e.getMessage());
            return Collections.emptyMap();
        } catch (Exception e) {
            log.error("User Service 닉네임 조회 실패: {}", e.getMessage());
            // 서비스 장애 격리를 위해 빈 맵 반환
            return Collections.emptyMap();
        }
    }

    // =========================================================================
    // 3. 댓글 작성 (POST /api/posts/{postId}/comments)
    // =========================================================================
    @Transactional
    public CommentResponse createComment(Long postId, CommentRequest request, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
                .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        Comment comment = Comment.builder()
                .content(request.getContent())
                .post(post)
                .authorId(authenticatedUserId) // 작성자 ID 설정
                .build();

        commentRepository.save(comment);

        // 응답 생성 시 닉네임 조회 및 설정
        CommentResponse response = CommentResponse.fromEntity(comment);

        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(comment.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(comment.getAuthorId(), "[알 수 없음]");
        response.setAuthorNickname(nickname);

        return response;
    }

    // =========================================================================
    // 4. 댓글 조회 (GET /api/posts/{postId}/comments)
    // =========================================================================
    @Transactional(readOnly = true)
    public List<CommentResponse> getCommentsByPostId(Long postId) {
        List<Comment> comments = commentRepository.findByPostIdOrderByCreatedAtAsc(postId);

        // 작성자 ID 목록 추출
        List<String> authorIds = comments.stream()
                .map(Comment::getAuthorId)
                .distinct()
                .collect(Collectors.toList());

        // 닉네임 일괄 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // CommentResponse 매핑 및 닉네임 설정
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
    // 5. 댓글 수정 (PUT /api/posts/comments/{commentId}) - 권한 확인
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
    // 6. 댓글 삭제 (DELETE /api/posts/comments/{commentId}) - 권한 확인
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