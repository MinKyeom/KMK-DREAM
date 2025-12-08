package com.mk.demo.service;

import com.mk.demo.dto.PostResponse;
import com.mk.demo.entity.Post;
import com.mk.demo.repository.PostRepository;
import com.mk.demo.entity.Category; // Category Entity 가정
import com.mk.demo.repository.CategoryRepository; // CategoryRepository 가정
import com.mk.demo.entity.Tag; // Tag Entity 가정
import com.mk.demo.repository.TagRepository; // TagRepository 가정

import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;
    // ⭐ 가정: Category 및 Tag Repository가 필요합니다.
    // private final CategoryRepository categoryRepository;
    // private final TagRepository tagRepository;

    @Transactional(readOnly = true)
    public Page<PostResponse> getPosts(Pageable pageable) {
        // Fetch Join이 적용된 Repository 메서드 호출
        Page<Post> posts = postRepository.findAllWithDetails(pageable);
        
        // 트랜잭션 내에서 DTO로 변환
        return posts.map(PostResponse::fromEntity);
    }
    
    // =========================================================================
    // ⭐ 수정: getPost 메서드 (500 에러 해결)
    // =========================================================================
    @Transactional(readOnly = true)
    // ⭐ 반환 타입을 PostResponse로 변경
    public PostResponse getPost(Long id) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));
                
        // ⭐ 트랜잭션 내에서 DTO로 변환하여 LAZY 로딩 예외 방지
        return PostResponse.fromEntity(post);
    }
    
    // =========================================================================
    // ⭐ 추가 1: createPost 메서드 
    // =========================================================================
    @Transactional
    public Post createPost(Post newPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        newPost.setAuthor(authenticatedUserId);
        
        // 1. 카테고리 설정 (CategoryRepository 사용 가정)
        // Category category = categoryRepository.findByName(categoryName)
        //     .orElseThrow(() -> new RuntimeException("유효하지 않은 카테고리입니다."));
        // newPost.setCategory(category);
        
        // 2. 태그 설정 (TagRepository 사용 가정)
        // Set<Tag> tags = tagNames.stream()
        //     .map(name -> tagRepository.findByName(name).orElseGet(() -> {
        //         Tag newTag = new Tag();
        //         newTag.setName(name);
        //         return tagRepository.save(newTag);
        //     }))
        //     .collect(Collectors.toSet());
        // newPost.setTags(tags);
        
        return postRepository.save(newPost);
    }

    // =========================================================================
    // ⭐ 추가 2: updatePost 메서드 
    // =========================================================================
    @Transactional
    public Post updatePost(Long postId, Post updatedPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인
        if (!post.getAuthor().equals(authenticatedUserId)) {
            throw new RuntimeException("수정 권한이 없습니다.");
        }
        
        // 2. 내용 업데이트 (title, content)
        post.setTitle(updatedPost.getTitle());
        post.setContent(updatedPost.getContent());

        // 3. 카테고리 업데이트 (CategoryRepository 사용 가정)
        // Category category = categoryRepository.findByName(categoryName) ...
        // post.setCategory(category);
        
        // 4. 태그 업데이트 (TagRepository 사용 가정)
        // post.getTags().clear(); 
        // Set<Tag> tags = tagService.findOrCreateTags(tagNames);
        // post.setTags(tags);
        
        // JPA Dirty Checking에 의해 자동 저장됨
        return post;
    }
    
    // =========================================================================
    // ⭐ 추가 3: deletePost 메서드 
    // =========================================================================
    @Transactional
    public void deletePost(Long postId, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인
        if (!post.getAuthor().equals(authenticatedUserId)) {
            throw new RuntimeException("삭제 권한이 없습니다.");
        }
        
        // 2. 게시글 삭제
        postRepository.delete(post);
    }
    
    // 나머지 로직...
}