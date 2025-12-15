// src/main/java/com/mk/post_service/service/PostService.java

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
import org.springframework.web.reactive.function.client.WebClientResponseException; 
import reactor.core.publisher.Mono;
import com.mk.post_service.dto.PostRequest; // PostRequest 임포트 추가

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.Collections;
import java.util.Optional;

@Slf4j
@Service
@Transactional
public class PostService {

    private final PostRepository postRepository;
    private final CategoryRepository categoryRepository;
    private final TagRepository tagRepository;
    private final WebClient webClient;

    // WebClient.Builder 및 userServiceUrl을 생성자 인수로 주입하여 안전하게 초기화
    public PostService(
        WebClient.Builder webClientBuilder,
        PostRepository postRepository,
        CategoryRepository categoryRepository,
        TagRepository tagRepository,
        @Value("${user.service.url}") String userServiceUrl // ⭐ 수정: user-service.url -> user.service.url
    ) {
        this.postRepository = postRepository;
        this.categoryRepository = categoryRepository;
        this.tagRepository = tagRepository;
        this.webClient = webClientBuilder.baseUrl(userServiceUrl).build();
    }

    // =========================================================================
    // 1. 전체 글 페이지 조회 (GET /api/posts)
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPosts(Pageable pageable) {
        Page<Post> postPage = postRepository.findAll(pageable);

        // 닉네임 일괄 조회
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // Page<Post> -> Page<PostResponse> 변환
        return postPage.map((Post post) -> { // ✅ 수정: 람다식 입력 타입 (Post post) 명시
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }

    // =========================================================================
    // 2. 글 상세 조회 (GET /api/posts/{id})
    // =========================================================================
    @Transactional(readOnly = true)
    public PostResponse getPost(Long id) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("글을 찾을 수 없습니다."));

        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(post.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
        
        // 응답 생성
        PostResponse response = PostResponse.fromEntity(post);
        response.setAuthorNickname(nickname);

        return response;
    }

    // =========================================================================
    // 3. 글 작성 (POST /api/posts)
    // =========================================================================
    @Transactional
    public Post createPost(Post post, List<String> tagNames, String categoryName, String authenticatedUserId) {
        post.setAuthorId(authenticatedUserId); 

        // 1. 카테고리 처리: 기존 카테고리 조회 또는 새로 생성
        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> categoryRepository.save(Category.builder().name(categoryName).build()));
        post.setCategory(category);

        // 2. 태그 처리: 기존 태그 조회 또는 새로 생성
        Set<Tag> tags = tagNames.stream()
                .map(tagName -> tagRepository.findByName(tagName)
                        .orElseGet(() -> tagRepository.save(Tag.builder().name(tagName).build())))
                .collect(Collectors.toSet());
        post.setTags(tags);

        return postRepository.save(post);
    }

    // =========================================================================
    // 4. 글 수정 (PUT /api/posts/{id})
    // =========================================================================
    @Transactional
    public Post updatePost(Long id, Post postUpdates, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post existingPost = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("수정할 글을 찾을 수 없습니다."));

        // 권한 확인
        if (!existingPost.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("글 수정 권한이 없습니다.");
        }

        // 1. 내용 업데이트
        existingPost.setTitle(postUpdates.getTitle());
        existingPost.setContent(postUpdates.getContent());

        // 2. 카테고리 처리
        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> categoryRepository.save(Category.builder().name(categoryName).build()));
        existingPost.setCategory(category);

        // 3. 태그 처리
        Set<Tag> tags = tagNames.stream()
                .map(tagName -> tagRepository.findByName(tagName)
                        .orElseGet(() -> tagRepository.save(Tag.builder().name(tagName).build())))
                .collect(Collectors.toSet());
        existingPost.setTags(tags);

        return existingPost;
    }

    // =========================================================================
    // 5. 글 삭제 (DELETE /api/posts/{id})
    // =========================================================================
    @Transactional
    public void deletePost(Long id, String authenticatedUserId) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("삭제할 글을 찾을 수 없습니다."));

        // 권한 확인
        if (!post.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("글 삭제 권한이 없습니다.");
        }

        postRepository.delete(post);
    }

    // =========================================================================
    // 6. 닉네임 일괄 조회 (User Service와의 통신)
    // =========================================================================
    @Transactional(readOnly = true)
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

    // =========================================================================
    // 7. 카테고리별 글 조회 (GET /api/posts/category?name=...)
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByCategory(String categoryName, Pageable pageable) {
        Page<Post> postPage = postRepository.findByCategory_Name(categoryName, pageable);

        // 닉네임 일괄 조회 로직 재사용
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // Page<Post> -> Page<PostResponse> 변환
        return postPage.map((Post post) -> { // ✅ 수정: 람다식 입력 타입 (Post post) 명시
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }

    // =========================================================================
    // 8. 태그별 글 조회 (GET /api/posts/tag?name=...)
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByTag(String tagName, Pageable pageable) {
        Page<Post> postPage = postRepository.findByTags_Name(tagName, pageable);

        // 닉네임 일괄 조회 로직 재사용
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // Page<Post> -> Page<PostResponse> 변환
        return postPage.map((Post post) -> { // ✅ 수정: 람다식 입력 타입 (Post post) 명시
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }
}