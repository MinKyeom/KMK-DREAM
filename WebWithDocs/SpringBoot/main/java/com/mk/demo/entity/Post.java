package com.mk.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
@Getter @Setter
public class Post {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    @Lob
    private String content; // Markdown 원본

    // private String author; // ⭐ 제거: 작성자 ID (String) 대신 User Entity로 대체

    // ⭐ 수정: User 엔티티와 관계 설정 (작성자)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id") // DB 컬럼명을 user_id로 설정
    private User user; // Post 작성자를 User Entity로 직접 참조

    private LocalDateTime createdAt = LocalDateTime.now();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    private Category category; 

    @ManyToMany(cascade = {CascadeType.PERSIST, CascadeType.MERGE})
    @JoinTable(
        name = "post_tag",
        joinColumns = @JoinColumn(name="post_id"),
        inverseJoinColumns = @JoinColumn(name="tag_id")
    )
    private Set<Tag> tags = new HashSet<>();
    
    // ⭐ 추가: 댓글 관계 설정
    @OneToMany(mappedBy = "post", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Comment> comments = new ArrayList<>();
}