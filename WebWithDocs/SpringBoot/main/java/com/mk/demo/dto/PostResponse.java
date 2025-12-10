package com.mk.demo.dto;

import com.mk.demo.entity.Post;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

@Getter @Setter
public class PostResponse {
    private Long id;
    private String title;
    private String content; 
    // private String author; // ⭐ 제거
    private String authorNickname; // ⭐ 추가: 닉네임으로 변경
    private LocalDateTime createdAt;
    
    private String categoryName; 
    private List<String> tagNames; 

    public static PostResponse fromEntity(Post post) {
        PostResponse dto = new PostResponse();
        dto.setId(post.getId());
        dto.setTitle(post.getTitle());
        dto.setContent(post.getContent()); 
        
        // ⭐ 수정: Post.user 엔티티에서 닉네임 추출
        if (post.getUser() != null) {
            dto.setAuthorNickname(post.getUser().getNickname());
        }
        
        dto.setCreatedAt(post.getCreatedAt());

        if (post.getCategory() != null) {
            dto.setCategoryName(post.getCategory().getName());
        }
        
        dto.setTagNames(post.getTags().stream()
                                    .map(tag -> tag.getName())
                                    .collect(Collectors.toList()));
        return dto;
    }
}