package com.mk.post_service.dto;

import com.mk.post_service.entity.Comment;
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
    private String authorId; 
    private LocalDateTime createdAt;

    public static CommentResponse fromEntity(Comment comment) {
        return CommentResponse.builder()
                .id(comment.getId())
                .content(comment.getContent())
                // ⭐ 수정: 닉네임 설정 로직 제거 (Service Layer에서 설정)
                // .authorNickname(comment.getUser().getNickname()) 
                // ⭐ 수정: Comment Entity의 authorId로 변경
                .authorId(comment.getAuthorId()) 
                .createdAt(comment.getCreatedAt())
                .build();
    }
    
    public static List<CommentResponse> fromEntityList(List<Comment> comments) {
        return comments.stream()
                .map(CommentResponse::fromEntity)
                .collect(Collectors.toList());
    }
}