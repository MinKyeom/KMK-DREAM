// src/main/java/com/mk/post_service/controller/PostController.java

package com.mk.post_service.controller;

import com.mk.post_service.dto.PostRequest;
import com.mk.post_service.dto.PostResponse;
import com.mk.post_service.dto.CategoryResponse; // ⭐ 추가
import com.mk.post_service.dto.TagResponse; // ⭐ 추가
import com.mk.post_service.entity.Post;
import com.mk.post_service.service.PostService;
import com.mk.post_service.security.SecurityUtils; 
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

import java.util.List; 

@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    // =========================================================================
    // 1. 전체 글 페이지 조회 (GET /api/posts) - 인증 불필요
    // =========================================================================
    @GetMapping
    public Page<PostResponse> getPosts(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPosts(pageable);
    }

    // =========================================================================
    // 2. 글 상세 조회 (GET /api/posts/{id}) - 인증 불필요
    // =========================================================================
    @GetMapping("/{id}")
    public PostResponse getPost(@PathVariable Long id) {
        return postService.getPost(id);
    }

    // =========================================================================
    // 3. 글 작성 (POST /api/posts) - 인증 필수
    // =========================================================================
    @PostMapping
    public Post createPost(@RequestBody PostRequest request) {
        // ⭐ 수정: 유틸리티 클래스 사용
        String authenticatedUserId = SecurityUtils.getAuthenticatedUserId();
        
        return postService.createPost(
            request.toEntity(), 
            request.getTags(), 
            request.getCategory(), 
            authenticatedUserId
        );
    }

    // =========================================================================
    // 4. 글 수정 (PUT /api/posts/{id}) - 인증 필수
    // =========================================================================
    @PutMapping("/{id}")
    public Post updatePost(@PathVariable Long id, @RequestBody PostRequest request) {
        // ⭐ 수정: 유틸리티 클래스 사용
        String authenticatedUserId = SecurityUtils.getAuthenticatedUserId();

        return postService.updatePost(
            id,
            request.toEntity(),
            request.getTags(),
            request.getCategory(),
            authenticatedUserId
        );
    }

    // =========================================================================
    // 5. 글 삭제 (DELETE /api/posts/{id}) - 인증 필수
    // =========================================================================
    @DeleteMapping("/{id}")
    public void deletePost(@PathVariable Long id) {
        // ⭐ 수정: 유틸리티 클래스 사용
        String authenticatedUserId = SecurityUtils.getAuthenticatedUserId();
        postService.deletePost(id, authenticatedUserId);
    }

    // =========================================================================
    // 6. 카테고리별 글 조회 (GET /api/posts/category?name=...) - 인증 불필요
    // =========================================================================
    @GetMapping("/category")
    public Page<PostResponse> getPostsByCategory(
            @RequestParam String name,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPostsByCategory(name, pageable);
    }

    // =========================================================================
    // 7. 태그별 글 조회 (GET /api/posts/tag?name=...) - 인증 불필요
    // =========================================================================
    @GetMapping("/tag")
    public Page<PostResponse> getPostsByTag(
            @RequestParam String name,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPostsByTag(name, pageable);
    }

    // =========================================================================
    // 8. 카테고리 목록 조회 (GET /api/posts/categories) - PostCount 포함
    // =========================================================================
    @GetMapping("/categories")
    public List<CategoryResponse> getCategoriesListWithCount() { 
        return postService.getAllCategoriesWithCount(); 
    }

    // =========================================================================
    // 9. 태그 목록 조회 (GET /api/posts/tags) - PostCount 포함
    // =========================================================================
    @GetMapping("/tags")
    public List<TagResponse> getTagsListWithCount() { 
        return postService.getAllTagsWithCount(); 
    }
}