package com.mk.post_service.repository;

import com.mk.post_service.entity.Comment;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface CommentRepository extends JpaRepository<Comment, Long> {
    
    // 특정 게시글의 모든 댓글을 최신 순으로 조회
    List<Comment> findByPost_IdOrderByCreatedAtDesc(Long postId);
}