package com.mk.demo.repository;

import com.mk.demo.entity.Post;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface PostRepository extends JpaRepository<Post, Long> {
    
    // ⭐ 추가: Fetch Join을 사용하여 category와 tags를 즉시 로딩합니다. (N+1 문제 해결)
    // COUNT 쿼리는 최적화를 위해 별도로 정의해야 합니다. (JOIN FETCH는 카운팅 오류 유발 가능)
    @Query(value = "SELECT p FROM Post p JOIN FETCH p.category LEFT JOIN FETCH p.tags", 
           countQuery = "SELECT COUNT(p) FROM Post p")
    Page<Post> findAllWithDetails(Pageable pageable);
    
    Page<Post> findByAuthor(String author, Pageable pageable);
    Page<Post> findByCategory_Name(String categoryName, Pageable pageable);
    Page<Post> findByTags_Name(String tagName, Pageable pageable);
}