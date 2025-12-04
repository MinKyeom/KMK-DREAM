package com.mk.demo.repository;

import com.mk.demo.entity.Post;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepository extends JpaRepository<Post, Long> {
    Page<Post> findByAuthor(String author, Pageable pageable);
    Page<Post> findByCategory_Name(String categoryName, Pageable pageable);
    Page<Post> findByTags_Name(String tagName, Pageable pageable);
}