package com.mk.demo.repository;

import com.mk.demo.entity.Post;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface PostRepository extends JpaRepository<Post, Long> {
    
    // ⭐ 수정: SELECT 다음에 DISTINCT 키워드를 추가하여 중복 Post Row를 방지합니다.
    @Query(value = "SELECT DISTINCT p FROM Post p JOIN FETCH p.category LEFT JOIN FETCH p.tags", 
           countQuery = "SELECT COUNT(p) FROM Post p")
    Page<Post> findAllWithDetails(Pageable pageable);
    
    // Page<Post> findByAuthor(String author, Pageable pageable); // ⭐ 제거: Post 엔티티 변경으로 인해 필요 없어짐
    
    Page<Post> findByCategory_Name(String categoryName, Pageable pageable);
    Page<Post> findByTags_Name(String tagName, Pageable pageable);
}