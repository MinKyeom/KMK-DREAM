package com.mk.post_service.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import java.time.LocalDateTime;

@Entity
@Getter @Setter
public class Comment {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Lob
    @Column(nullable = false)
    private String content;

    private LocalDateTime createdAt = LocalDateTime.now();
    
    // 관계 1: Post (게시글) 유지
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id", nullable = false)
    private Post post;
    
    // ⭐ 수정: User 엔티티와의 관계 제거
    // @ManyToOne(fetch = FetchType.LAZY)
    // @JoinColumn(name = "user_id", nullable = false)
    // private User user; // 삭제

    // ⭐ 추가: 댓글 작성자의 ID만 저장
    @Column(name = "author_id", nullable = false)
    private String authorId;
}