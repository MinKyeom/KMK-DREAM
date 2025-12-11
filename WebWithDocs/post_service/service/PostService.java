// src/main/java/com/mk/post_service/service/PostService.java

package com.mk.post_service.service;

import com.mk.post_service.dto.PostResponse;
import com.mk.post_service.entity.Post;
import com.mk.post_service.repository.PostRepository;
import com.mk.post_service.entity.Category; 
import com.mk.post_service.repository.CategoryRepository; 
import com.mk.post_service.entity.Tag; 
import com.mk.post_service.repository.TagRepository; 

// ⭐ 수정: ParameterizedTypeReference 임포트 (WebClient 제네릭 타입 처리)
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

@Slf4j 
@Service
@Transactional
public class PostService {

    private final PostRepository postRepository;
    private final CategoryRepository categoryRepository;
    private final TagRepository tagRepository;
    private final WebClient webClient; // WebClient 인스턴스

    // ⭐ 1. WebClient.Builder 주입 및 User Service URL 설정
    // application.yml/properties에서 user.service.url 속성으로 주입받아야 합니다.
    public PostService(
        PostRepository postRepository, 
        CategoryRepository categoryRepository, 
        TagRepository tagRepository, 
        WebClient.Builder webClientBuilder,
        @Value("${user.service.url}") String userServiceBaseUrl // 설정값을 생성자 주입
    ) {
        this.postRepository = postRepository;
        this.categoryRepository = categoryRepository;
        this.tagRepository = tagRepository;
        // User Service의 기본 URL로 WebClient 인스턴스 생성
        this.webClient = webClientBuilder.baseUrl(userServiceBaseUrl).build();
    }
    
    // =========================================================================
    // ⭐ MSA 통신을 위한 닉네임 일괄 조회 유틸리티 메서드
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
            
            return mono.block(); // 동기 호출 (서비스 계층에서는 일반적으로 사용)
            
        } catch (Exception e) {
            log.error("User Service에서 닉네임 정보를 가져오는 중 오류 발생: {}", e.getMessage(), e);
            // 통신 오류 시, 닉네임을 기본값으로 처리하여 서비스 중단 방지
            return authorIds.stream()
                .collect(Collectors.toMap(id -> id, id -> "[통신 오류]")); 
        }
    }
    
    // =========================================================================
    // 1. 전체 글 페이지 조회 (GET /api/posts) - 닉네임 일괄 조회 적용
    // =========================================================================
    @Transactional(readOnly = true)
    public Page<PostResponse> getPosts(Pageable pageable) {
        Page<Post> postPage = postRepository.findAllWithDetails(pageable);

        // 1. 페이지 내 모든 게시글의 authorId 추출
        List<String> authorIds = postPage.stream()
            .map(Post::getAuthorId)
            .distinct() 
            .collect(Collectors.toList());

        // 2. User Service에서 닉네임 맵 일괄 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);

        // 3. PostResponse로 변환 및 닉네임 설정
        return postPage.map(post -> {
            PostResponse response = PostResponse.fromEntity(post);
            String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
            response.setAuthorNickname(nickname);
            return response;
        });
    }

    // =========================================================================
    // 2. 글 상세 조회 (GET /api/posts/{id}) - 닉네임 단건 조회 적용
    // =========================================================================
    @Transactional(readOnly = true)
    public PostResponse getPost(Long postId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        PostResponse response = PostResponse.fromEntity(post);

        // 닉네임 단건 조회
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(post.getAuthorId()));
        String nickname = nicknameMap.getOrDefault(post.getAuthorId(), "[알 수 없음]");
        
        response.setAuthorNickname(nickname); 
        
        return response;
    }
    
    // =========================================================================
    // 3. 글 작성 (POST /api/posts)
    // =========================================================================
    @Transactional
    public Post createPost(Post newPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        // 1. 카테고리 설정
        Category category = categoryRepository.findByName(categoryName)
            .orElseGet(() -> {
                Category newCategory = new Category();
                newCategory.setName(categoryName);
                return categoryRepository.save(newCategory);
            });
        newPost.setCategory(category);
        
        // 2. 태그 설정 (없으면 새로 생성)
        Set<Tag> tags = tagNames.stream()
            .map(name -> tagRepository.findByName(name).orElseGet(() -> {
                Tag newTag = new Tag();
                newTag.setName(name);
                return tagRepository.save(newTag);
            }))
            .collect(Collectors.toSet());
        newPost.setTags(tags);
        
        // 3. 작성자 ID 설정 (인증 정보 사용)
        newPost.setAuthorId(authenticatedUserId);
        
        return postRepository.save(newPost);
    }
    
    // =========================================================================
    // 4. 글 수정 (PUT /api/posts/{id}) - 권한 확인 및 업데이트
    // =========================================================================
    @Transactional
    public Post updatePost(Long postId, Post updatedPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인
        if (!post.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("게시글 수정 권한이 없습니다.");
        }

        // 2. 내용 업데이트
        post.setTitle(updatedPost.getTitle());
        post.setContent(updatedPost.getContent());

        // 3. 카테고리 업데이트
        Category category = categoryRepository.findByName(categoryName)
            .orElseThrow(() -> new RuntimeException("유효하지 않은 카테고리입니다: " + categoryName));
        post.setCategory(category);
        
        // 4. 태그 업데이트
        post.getTags().clear(); // 기존 태그 제거
        Set<Tag> tags = tagNames.stream()
            .map(name -> tagRepository.findByName(name).orElseGet(() -> {
                Tag newTag = new Tag();
                newTag.setName(name);
                return tagRepository.save(newTag);
            }))
            .collect(Collectors.toSet());
        post.setTags(tags);
        
        // save는 JPA가 더티 체킹으로 처리합니다.
        return post;
    }
    
    // =========================================================================
    // 5. 글 삭제 (DELETE /api/posts/{id}) - 권한 확인
    // =========================================================================
    @Transactional
    public void deletePost(Long postId, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인
        if (!post.getAuthorId().equals(authenticatedUserId)) {
            throw new RuntimeException("게시글 삭제 권한이 없습니다.");
        }
        
        postRepository.delete(post);
    }
    
    // =========================================================================
    // 6. 카테고리별 글 조회 (GET /api/posts/category?name=...)
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
    // 7. 태그별 글 조회 (GET /api/posts/tag?name=...)
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