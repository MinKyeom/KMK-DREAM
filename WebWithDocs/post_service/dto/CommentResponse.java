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
                // .authorNickname(comment.getUser().getNickname()) 
                .authorId(comment.getAuthorId()) 
                .createdAt(comment.getCreatedAt())
                .build();
    }
    
    // ⬅️ 추가: CommentService에서 닉네임을 주입받는 호출을 처리하기 위한 오버로딩 메서드
    public static CommentResponse fromEntity(Comment comment, String authorNickname) {
        return CommentResponse.builder()
                .id(comment.getId())
                .content(comment.getContent())
                .authorNickname(authorNickname) // 닉네임 설정
                .authorId(comment.getAuthorId()) 
                .createdAt(comment.getCreatedAt())
                .build();
    }
    
    // 이 메서드는 CommentResponse::fromEntity (인수 1개)를 사용하므로 Service에서 닉네임 설정이 필요함
    public static List<CommentResponse> fromEntityList(List<Comment> comments) {
        return comments.stream()
                .map(CommentResponse::fromEntity)
                .collect(Collectors.toList());
    }
}