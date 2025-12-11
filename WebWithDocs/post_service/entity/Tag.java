// src/main/java/com/mk/post_service/entity/Tag.java

package com.mk.post_service.entity;

import com.fasterxml.jackson.annotation.JsonIgnore; // ⭐ 추가: 순환 참조 방지
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

@Entity
@Getter @Setter
public class Tag {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    // PostList에서 Tag를 불러올 때 posts 필드는 무시합니다.
    @JsonIgnore
    @ManyToMany(mappedBy = "tags")
    private Set<Post> posts = new HashSet<>();
}