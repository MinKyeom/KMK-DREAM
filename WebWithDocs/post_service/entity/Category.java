// src/main/java/com/mk/post_service/entity/Category.java

package com.mk.post_service.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.Builder; // ⭐ 추가
import lombok.NoArgsConstructor; // ⭐ 추가
import lombok.AllArgsConstructor; // ⭐ 추가
import lombok.AccessLevel; // ⭐ 추가

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
@Builder // ⭐ 추가: 빌더 패턴 활성화
@NoArgsConstructor(access = AccessLevel.PROTECTED) // ⭐ 추가: JPA 요구 사항 (기본 생성자)
@AllArgsConstructor // ⭐ 추가: 빌더를 위한 전체 필드 생성자
public class Category {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    // PostList에서 Category를 불러올 때 posts 필드는 무시합니다.
    @JsonIgnore 
    @OneToMany(mappedBy = "category")
    private List<Post> posts = new ArrayList<>();
}