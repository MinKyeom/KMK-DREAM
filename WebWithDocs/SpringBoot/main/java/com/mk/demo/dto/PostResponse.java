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
    private String author;
    private LocalDateTime createdAt;
    
    // 연관 관계 필드: DTO 내에서 필요한 데이터만 추출
    private String categoryName; 
    private List<String> tagNames; 

    // 엔티티를 DTO로 변환하는 정적 팩토리 메서드
    // 이 메서드는 Service 계층의 트랜잭션이 살아있을 때 호출되어야 합니다.
    public static PostResponse fromEntity(Post post) {
        PostResponse dto = new PostResponse();
        dto.setId(post.getId());
        dto.setTitle(post.getTitle());
        // 목록에서는 content 전체 대신 일부만 보낼 수 있으나, 일단 전체 포함
        dto.setContent(post.getContent()); 
        dto.setAuthor(post.getAuthor());
        dto.setCreatedAt(post.getCreatedAt());

        // LAZY 로딩된 category 접근 (Service에서 Fetch Join으로 미리 로딩했다고 가정)
        if (post.getCategory() != null) {
            dto.setCategoryName(post.getCategory().getName());
        }
        
        // LAZY 로딩된 tags 접근
        dto.setTagNames(post.getTags().stream()
                                    .map(tag -> tag.getName())
                                    .collect(Collectors.toList()));
        return dto;
    }
}

// package com.mk.demo.dto;

// public class PostResponse {
  
// }
