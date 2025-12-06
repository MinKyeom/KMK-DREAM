package com.mk.demo.controller;

import com.mk.demo.dto.PostRequest;
import com.mk.demo.entity.Post;
import com.mk.demo.service.PostService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    // 전체 글 페이지 조회
    @GetMapping
    public Page<Post> getPosts(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size
    ) {
        Pageable pageable = PageRequest.of(page, size);
        return postService.getPosts(pageable);
    }
    
    // ... (다른 조회 메서드 생략)

    // 글 상세 조회
    @GetMapping("/{id}")
    public Post getPost(@PathVariable Long id) {
        return postService.getPost(id);
    }

    // 글 작성 (인증 필수)
    @PostMapping
    public Post createPost(@RequestBody PostRequest request) {
        // ⭐ 보안: JWT에서 사용자 ID 추출
        String authenticatedUserId = getUserIdFromContext();
        
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
        // ⭐ 보안: JWT에서 사용자 ID 추출
        String authenticatedUserId = getUserIdFromContext();
        
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
        // ⭐ 보안: JWT에서 사용자 ID 추출
        String authenticatedUserId = getUserIdFromContext(); 
        
        postService.deletePost(id, authenticatedUserId);
    }

    /**
     * SecurityContextHolder에서 인증된 사용자 ID를 추출하는 헬퍼 메서드
     */
    private String getUserIdFromContext() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication == null || authentication.getPrincipal().equals("anonymousUser")) {
            throw new RuntimeException("인증되지 않은 사용자입니다. 로그인하십시오.");
        }
        return (String) authentication.getPrincipal(); 
    }
}