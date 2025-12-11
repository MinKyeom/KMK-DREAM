package com.mk.demo.dto;

import com.mk.demo.entity.Comment;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

@Builder
@Getter @Setter
public class CommentResponse {
    private Long id;
    private String content;
    private String authorNickname;
    private String authorId; // ⭐ 추가: 댓글 작성자의 ID
    private LocalDateTime createdAt;

    public static CommentResponse fromEntity(Comment comment) {
        return CommentResponse.builder()
                .id(comment.getId())
                .content(comment.getContent())
                .authorNickname(comment.getUser().getNickname())
                // ⭐ 추가: User 엔티티에서 ID를 가져와 설정
                .authorId(comment.getUser().getId()) 
                .createdAt(comment.getCreatedAt())
                .build();
    }
    
    public static List<CommentResponse> fromEntityList(List<Comment> comments) {
        return comments.stream()
                .map(CommentResponse::fromEntity)
                .collect(Collectors.toList());
    }
}