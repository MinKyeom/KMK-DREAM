package com.mk.demo.service;

import com.mk.demo.dto.PostResponse;
import com.mk.demo.entity.Post;
import com.mk.demo.repository.PostRepository;
import com.mk.demo.entity.Category; 
import com.mk.demo.repository.CategoryRepository; 
import com.mk.demo.entity.Tag; 
import com.mk.demo.repository.TagRepository; 
import com.mk.demo.entity.User; // ⭐ 추가: User Entity 사용

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
    private final CategoryRepository categoryRepository;
    private final TagRepository tagRepository;
    private final UserService userService; // ⭐ 추가: User Service 주입

    @Transactional(readOnly = true)
    public Page<PostResponse> getPosts(Pageable pageable) {
        Page<Post> posts = postRepository.findAllWithDetails(pageable);
        return posts.map(PostResponse::fromEntity);
    }
    
    @Transactional(readOnly = true)
    public PostResponse getPost(Long id) {
        Post post = postRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));
                
        return PostResponse.fromEntity(post);
    }
    
    // =========================================================================
    // ⭐ 수정 1: createPost 메서드 (User Entity 연결로 변경)
    // =========================================================================
    @Transactional
    public Post createPost(Post newPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        // 1. User Entity 조회 및 연결
        User user = userService.findUserById(authenticatedUserId); 
        newPost.setUser(user); // ⭐ 수정: setAuthor(String) 대신 setUser(User)
        
        // 2. 카테고리 설정
        Category category = categoryRepository.findByName(categoryName)
            .orElseThrow(() -> new RuntimeException("유효하지 않은 카테고리입니다: " + categoryName));
        newPost.setCategory(category);
        
        // 3. 태그 설정
        Set<Tag> tags = tagNames.stream()
            .map(name -> tagRepository.findByName(name).orElseGet(() -> {
                Tag newTag = new Tag();
                newTag.setName(name);
                return tagRepository.save(newTag);
            }))
            .collect(Collectors.toSet());
        newPost.setTags(tags);
        
        return postRepository.save(newPost);
    }

    // =========================================================================
    // ⭐ 수정 2: updatePost 메서드 (권한 확인 로직 변경)
    // =========================================================================
    @Transactional
    public Post updatePost(Long postId, Post updatedPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인 
        // ⭐ 수정: post.getAuthor() 대신 post.getUser().getId()로 비교
        if (!post.getUser().getId().equals(authenticatedUserId)) {
            throw new RuntimeException("수정 권한이 없습니다.");
        }
        
        // 2. 내용 업데이트 (title, content)
        post.setTitle(updatedPost.getTitle());
        post.setContent(updatedPost.getContent());

        // 3. 카테고리 업데이트
        Category category = categoryRepository.findByName(categoryName)
            .orElseThrow(() -> new RuntimeException("유효하지 않은 카테고리입니다: " + categoryName));
        post.setCategory(category);
        
        // 4. 태그 업데이트
        post.getTags().clear();
        Set<Tag> tags = tagNames.stream()
            .map(name -> tagRepository.findByName(name).orElseGet(() -> {
                Tag newTag = new Tag();
                newTag.setName(name);
                return tagRepository.save(newTag);
            }))
            .collect(Collectors.toSet());
        post.setTags(tags);
        
        return post;
    }
    
    // =========================================================================
    // ⭐ 수정 3: deletePost 메서드 (권한 확인 로직 변경)
    // =========================================================================
    @Transactional
    public void deletePost(Long postId, String authenticatedUserId) {
        Post post = postRepository.findById(postId)
            .orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));

        // 1. 작성자 권한 확인
        // ⭐ 수정: post.getAuthor() 대신 post.getUser().getId()로 비교
        if (!post.getUser().getId().equals(authenticatedUserId)) {
            throw new RuntimeException("삭제 권한이 없습니다.");
        }
        
        // 2. 게시글 삭제
        postRepository.delete(post);
    }
}