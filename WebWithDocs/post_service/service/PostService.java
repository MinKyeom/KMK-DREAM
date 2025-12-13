package com.mk.post_service.service;

import com.mk.post_service.dto.PostResponse;
import com.mk.post_service.entity.Post;
import com.mk.post_service.repository.PostRepository;
import com.mk.post_service.entity.Category;
import com.mk.post_service.repository.CategoryRepository;
import com.mk.post_service.entity.Tag;
import com.mk.post_service.repository.TagRepository;

import org.springframework.core.ParameterizedTypeReference;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.Collections; // Collections 임포트 추가

@Slf4j
@Service
@Transactional
public class PostService {

    private final PostRepository postRepository;
    private final CategoryRepository categoryRepository;
    private final TagRepository tagRepository;
    private final WebClient webClient; // WebClient 인스턴스

    // ⭐ 수정: WebClient.Builder 및 userServiceUrl을 생성자 인수로 주입하여 안전하게 초기화
    public PostService(
        WebClient.Builder webClientBuilder,
        PostRepository postRepository,
        CategoryRepository categoryRepository,
        TagRepository tagRepository,
        @Value("${user-service.url}") String userServiceUrl // ⭐ URL을 생성자에서 직접 주입
    ) {
        this.postRepository = postRepository;
        this.categoryRepository = categoryRepository;
        this.tagRepository = tagRepository;
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
                    .bodyValue(authorIds) // 사용자 ID 목록 전송
                    .retrieve()
                    .bodyToMono(new ParameterizedTypeReference<Map<String, String>>() {}); // 응답 타입 (Map<String, String>)

            // 블로킹 호출 (Microservice 간 동기 통신)
            return mono.block();

        } catch (Exception e) {
            log.error("User Service에서 닉네임 조회 실패: {}", e.getMessage());
            // 서비스 장애 격리를 위해 빈 맵 반환
            return Collections.emptyMap();
        }
    }

    // =========================================================================
    // 3. 글 작성 (POST /api/posts)
    // =========================================================================
    @Transactional
    public Post createPost(Post post, List<String> tagNames, String categoryName, String authenticatedUserId) {
        post.setAuthorId(authenticatedUserId); // 작성자 ID 설정

        // 1. 카테고리 처리: 기존 카테고리 조회 또는 새로 생성
        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> categoryRepository.save(Category.builder().name(categoryName).build()));
        post.setCategory(category);

        // 2. 태그 처리: 기존 태그 조회 또는 새로 생성하여 Set에 추가
        Set<Tag> tags = tagNames.stream()
                .map(name -> tagRepository.findByName(name)
                        .orElseGet(() -> tagRepository.save(Tag.builder().name(name).build())))
                .collect(Collectors.toSet());
        post.setTags(tags);

        return postRepository.save(post);
    }

    // =========================================================================
    // 4. 전체 글 페이지 조회 (GET /api/posts) - 닉네임 조회 및 오류 복구
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPosts(Pageable pageable) {
        Page<Post> postPage = postRepository.findAll(pageable);

        // 닉네임 일괄 조회 로직 재사용
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        return postPage.map(post -> {
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }

    // =========================================================================
    // 5. 글 상세 조회 (GET /api/posts/{id}) - 닉네임 조회 및 오류 복구
    // =========================================================================
    @Transactional(readOnly = true)
    public PostResponse getPost(Long id) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("글을 찾을 수 없습니다."));

        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(post.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");

        PostResponse response = PostResponse.fromEntity(post);
        response.setAuthorNickname(nickname);

        return response;
    }

    // =========================================================================
    // 6. 글 수정 (PUT /api/posts/{id}) - 권한 확인
    // =========================================================================
    @Transactional
    public Post updatePost(Long id, Post updatedPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("글을 찾을 수 없습니다."));

        // 권한 확인: 글 작성자의 ID와 인증된 사용자 ID가 일치해야 함
        if (!post.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("글 수정 권한이 없습니다.");
        }

        // 카테고리 업데이트
        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> categoryRepository.save(Category.builder().name(categoryName).build()));
        post.setCategory(category);

        // 태그 업데이트 (기존 태그 관계 해제 및 새 태그 설정)
        post.getTags().clear(); // 기존 태그 관계 제거
        Set<Tag> tags = tagNames.stream()
                .map(name -> tagRepository.findByName(name)
                        .orElseGet(() -> tagRepository.save(Tag.builder().name(name).build())))
                .collect(Collectors.toSet());
        post.setTags(tags);

        // 내용 업데이트
        post.setTitle(updatedPost.getTitle());
        post.setContent(updatedPost.getContent());

        return postRepository.save(post);
    }

    // =========================================================================
    // 7. 글 삭제 (DELETE /api/posts/{id}) - 권한 확인
    // =========================================================================
    @Transactional
    public void deletePost(Long id, String authenticatedUserId) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("글을 찾을 수 없습니다."));

        // 권한 확인
        if (!post.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("글 삭제 권한이 없습니다.");
        }

        postRepository.delete(post);
    }

    // =========================================================================
    // 8. 카테고리별 글 조회 (GET /api/posts/category?name=...) - 닉네임 조회 및 오류 복구
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByCategory(String categoryName, Pageable pageable) {
        Page<Post> postPage = postRepository.findByCategory_Name(categoryName, pageable);

        // 닉네임 일괄 조회 로직 재사용
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        return postPage.map(post -> {
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }

    // =========================================================================
    // 9. 태그별 글 조회 (GET /api/posts/tag?name=...) - 닉네임 조회 및 오류 복구
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByTag(String tagName, Pageable pageable) {
        Page<Post> postPage = postRepository.findByTags_Name(tagName, pageable);

        // 닉네임 일괄 조회 로직 재사용
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        return postPage.map(post -> {
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }
}