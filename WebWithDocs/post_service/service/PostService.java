package com.mk.post_service.service;

import com.mk.post_service.dto.*;
import com.mk.post_service.entity.*;
import com.mk.post_service.repository.*;
import org.springframework.core.ParameterizedTypeReference;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.*;
import java.util.stream.Collectors;

@Slf4j
@Service
@Transactional
public class PostService {
    private final PostRepository postRepository;
    private final CategoryRepository categoryRepository;
    private final TagRepository tagRepository;
    private final WebClient webClient;

    @Value("${user-service.url:http://localhost:8081}")
    private String userServiceUrl;

    public PostService(
            PostRepository postRepository,
            CategoryRepository categoryRepository,
            TagRepository tagRepository,
            WebClient.Builder webClientBuilder
    ) {
        this.postRepository = postRepository;
        this.categoryRepository = categoryRepository;
        this.tagRepository = tagRepository;
        this.webClient = webClientBuilder.build();
    }

    public PostResponse createPost(PostRequest request, String authenticatedUserId) {
        Post post = request.toEntity();
        post.setAuthorId(authenticatedUserId);

        if (request.getCategory() != null && !request.getCategory().trim().isEmpty()) {
            Category category = categoryRepository.findByName(request.getCategory())
                    .orElseGet(() -> categoryRepository.save(Category.builder().name(request.getCategory()).build()));
            post.setCategory(category);
        }

        if (request.getTags() != null) {
            Set<Tag> tags = request.getTags().stream()
                    .map(tagName -> tagRepository.findByName(tagName)
                            .orElseGet(() -> tagRepository.save(Tag.builder().name(tagName).build())))
                    .collect(Collectors.toSet());
            post.setTags(tags);
        }

        Post savedPost = postRepository.save(post);
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(authenticatedUserId));
        PostResponse response = PostResponse.fromEntity(savedPost);
        response.setAuthorNickname(nicknameMap.getOrDefault(authenticatedUserId, "알 수 없음"));
        return response;
    }

    @Transactional(readOnly = true)
    public Page<PostResponse> getAllPosts(Pageable pageable) {
        Page<Post> postPage = postRepository.findAll(pageable);
        return mapPostPageToResponse(postPage);
    }

    @Transactional(readOnly = true)
    public PostResponse getPostById(Long id) {
        Post post = postRepository.findById(id).orElseThrow(() -> new RuntimeException("게시글 없음"));
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(post.getAuthorId()));
        PostResponse response = PostResponse.fromEntity(post);
        response.setAuthorNickname(nicknameMap.getOrDefault(post.getAuthorId(), "알 수 없음"));
        return response;
    }

    public PostResponse updatePost(Long id, PostRequest request, String authenticatedUserId) {
        Post post = postRepository.findById(id).orElseThrow(() -> new RuntimeException("게시글 없음"));
        if (!post.getAuthorId().equals(authenticatedUserId)) throw new RuntimeException("권한 없음");

        post.setTitle(request.getTitle());
        post.setContent(request.getContent());

        if (request.getCategory() != null) {
            post.setCategory(categoryRepository.findByName(request.getCategory())
                .orElseGet(() -> categoryRepository.save(Category.builder().name(request.getCategory()).build())));
        }

        Post savedPost = postRepository.save(post);
        Map<String, String> nicknameMap = getAuthorNicknamesMap(List.of(authenticatedUserId));
        PostResponse response = PostResponse.fromEntity(savedPost);
        response.setAuthorNickname(nicknameMap.getOrDefault(authenticatedUserId, "알 수 없음"));
        return response;
    }

    public void deletePost(Long id, String authenticatedUserId) {
        Post post = postRepository.findById(id).orElseThrow(() -> new RuntimeException("게시글 없음"));
        if (!post.getAuthorId().equals(authenticatedUserId)) throw new RuntimeException("권한 없음");
        postRepository.delete(post);
    }

    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByCategory(String categoryName, Pageable pageable) {
        return mapPostPageToResponse(postRepository.findByCategory_Name(categoryName, pageable));
    }

    @Transactional(readOnly = true)
    public Page<PostResponse> getPostsByTag(String tagName, Pageable pageable) {
        return mapPostPageToResponse(postRepository.findByTags_Name(tagName, pageable));
    }

    @Transactional(readOnly = true)
    public List<CategoryResponse> getAllCategoriesWithCount() {
        return categoryRepository.findAll().stream()
                .map(cat -> CategoryResponse.fromEntity(cat, postRepository.countByCategory(cat)))
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public List<TagResponse> getAllTagsWithCount() {
        return tagRepository.findAll().stream()
                .map(tag -> TagResponse.builder()
                        .name(tag.getName())
                        .postCount(postRepository.countByTagsContaining(tag))
                        .build())
                .collect(Collectors.toList());
    }

    private Map<String, String> getAuthorNicknamesMap(List<String> authorIds) {
        if (authorIds.isEmpty()) return Collections.emptyMap();
        try {
            return webClient.post()
                    .uri(userServiceUrl + "/api/users/nicknames")
                    .bodyValue(authorIds)
                    .retrieve()
                    .bodyToMono(new ParameterizedTypeReference<Map<String, String>>() {})
                    .block();
        } catch (Exception e) {
            log.error("User Service 통신 실패: {}", e.getMessage());
            return Collections.emptyMap();
        }
    }

    private Page<PostResponse> mapPostPageToResponse(Page<Post> postPage) {
        List<String> authorIds = postPage.stream().map(Post::getAuthorId).distinct().collect(Collectors.toList());
        Map<String, String> nicknameMap = getAuthorNicknamesMap(authorIds);
        return postPage.map(post -> {
            PostResponse res = PostResponse.fromEntity(post);
            res.setAuthorNickname(nicknameMap.getOrDefault(post.getAuthorId(), "알 수 없음"));
            return res;
        });
    }
}