package com.mk.post_service.repository;

import com.mk.post_service.entity.Post;
import com.mk.post_service.entity.Category;
import com.mk.post_service.entity.Tag;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface PostRepository extends JpaRepository<Post, Long> {
    
    @Query(value = "SELECT DISTINCT p FROM Post p JOIN FETCH p.category LEFT JOIN FETCH p.tags", 
           countQuery = "SELECT COUNT(p) FROM Post p")
    Page<Post> findAllWithDetails(Pageable pageable);
    
    Page<Post> findByCategory_Name(String categoryName, Pageable pageable);
    
    Page<Post> findByTags_Name(String tagName, Pageable pageable);

    // ⭐ PostService의 통계 기능을 위해 반드시 필요
    long countByCategory(Category category);
    long countByTagsContaining(Tag tag);
}