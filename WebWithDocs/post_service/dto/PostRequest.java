package com.mk.post_service.dto;

import com.mk.post_service.entity.Post;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter @Setter
public class PostRequest {
    private String title;
    private String content;
    // private String author; // ⭐ 제거: 보안을 위해 요청에서 작성자 ID를 받지 않습니다.
    private String category;
    private List<String> tags;

    public Post toEntity() {
        Post post = new Post();
        post.setTitle(this.title);
        post.setContent(this.content);
        return post;
    }
}