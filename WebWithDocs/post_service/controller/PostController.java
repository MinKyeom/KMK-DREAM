package com.mk.post_service.controller;

import com.mk.post_service.dto.PostRequest;
import com.mk.post_service.dto.PostResponse;
import com.mk.post_service.entity.Post;
import com.mk.post_service.service.PostService;
import com.mk.post_service.security.SecurityUtils; // ⭐ SecurityUtils 임포트
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    // 전체 글 페이지 조회 (인증 불필요)
    @GetMapping
    public Page<PostResponse> getPosts(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPosts(pageable);
    }

    // 글 상세 조회 (인증 불필요)
    @GetMapping("/{id}")
    public PostResponse getPost(@PathVariable Long id) {
        return postService.getPost(id);
    }

    // 글 작성 (인증 필수)
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

    // 글 수정 (인증 필수)
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

    // 글 삭제 (인증 필수)
    @DeleteMapping("/{id}")
    public void deletePost(@PathVariable Long id) {
        // ⭐ 수정: 유틸리티 클래스 사용
        String authenticatedUserId = SecurityUtils.getAuthenticatedUserId();
        postService.deletePost(id, authenticatedUserId);
    }

    // 카테고리별 글 조회 (인증 불필요)
    @GetMapping("/category")
    public Page<PostResponse> getPostsByCategory(
            @RequestParam String name,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPostsByCategory(name, pageable);
    }

    // 태그별 글 조회 (인증 불필요)
    @GetMapping("/tag")
    public Page<PostResponse> getPostsByTag(
            @RequestParam String name,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPostsByTag(name, pageable);
    }
}