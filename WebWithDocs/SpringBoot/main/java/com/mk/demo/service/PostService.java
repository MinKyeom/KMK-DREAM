package com.mk.demo.service;

import com.mk.demo.entity.Category;
import com.mk.demo.entity.Post;
import com.mk.demo.entity.Tag;
import com.mk.demo.repository.CategoryRepository;
import com.mk.demo.repository.PostRepository;
import com.mk.demo.repository.TagRepository;
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
@Transactional(readOnly = true)
public class PostService {
    private final PostRepository postRepository;
    private final TagRepository tagRepository;
    private final CategoryRepository categoryRepository;

    // 글 작성
    @Transactional
    public Post createPost(Post post, List<String> tagNames, String categoryName, String authenticatedUserId) {
        // ⭐ JWT에서 추출한 ID로 작성자 설정
        post.setAuthor(authenticatedUserId);

        // 태그 처리: 없으면 새로 생성 후 저장
        Set<Tag> tags = tagNames.stream()
                .map(name -> tagRepository.findByName(name)
                        .orElseGet(() -> {
                            Tag t = new Tag();
                            t.setName(name);
                            return tagRepository.save(t);
                        })
                ).collect(Collectors.toSet());
        post.setTags(tags);

        // 카테고리 처리: 없으면 새로 생성 후 저장
        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> {
                    Category c = new Category();
                    c.setName(categoryName);
                    return categoryRepository.save(c);
                });
        post.setCategory(category);


        return postRepository.save(post);
    }
    
    // 전체 글 페이지 조회
    public Page<Post> getPosts(Pageable pageable) {
        return postRepository.findAll(pageable);
    }
    
    // ... (다른 조회 메서드 생략)

    // 글 상세 조회
    public Post getPost(Long id) {
        return postRepository.findById(id).orElseThrow(() -> new RuntimeException("글을 찾을 수 없습니다."));
    }

    // 글 수정
    @Transactional
    public Post updatePost(Long id, Post updatedPost, List<String> tagNames, String categoryName, String authenticatedUserId) {
        Post post = getPost(id);
        
        // ⭐ 보안 강화: 작성자 ID 검사
        if (!post.getAuthor().equals(authenticatedUserId)) {
            throw new RuntimeException("수정 권한이 없습니다."); 
        }

        post.setTitle(updatedPost.getTitle());
        post.setContent(updatedPost.getContent());

        // 태그 및 카테고리 처리 (생성 로직 재사용)
        Set<Tag> tags = tagNames.stream()
                .map(name -> tagRepository.findByName(name)
                        .orElseGet(() -> {
                            Tag t = new Tag();
                            t.setName(name);
                            return tagRepository.save(t);
                        })
                ).collect(Collectors.toSet());
        post.setTags(tags);

        Category category = categoryRepository.findByName(categoryName)
                .orElseGet(() -> {
                    Category c = new Category();
                    c.setName(categoryName);
                    return categoryRepository.save(c);
                });
        post.setCategory(category);

        return postRepository.save(post);
    }

    // 글 삭제
    @Transactional
    public void deletePost(Long id, String authenticatedUserId) {
        Post post = getPost(id);
        
        // ⭐ 보안 강화: 작성자 ID 검사
        if (!post.getAuthor().equals(authenticatedUserId)) {
            throw new RuntimeException("삭제 권한이 없습니다."); 
        }
        postRepository.delete(post);
    }
}