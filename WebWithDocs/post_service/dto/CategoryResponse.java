package com.mk.post_service.dto;

import com.mk.post_service.entity.Category;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

/**
 * Sidebar 메뉴에 표시할 카테고리 목록의 응답 DTO
 * (Category Entity의 name, slug, postCount를 포함)
 */
@Builder
@Getter @Setter
public class CategoryResponse {
    private String name;
    private String slug;
    private Long postCount; // ⭐ 추가: 해당 카테고리 포스트 개수

    /**
     * Category Entity를 CategoryResponse DTO로 변환 (Post Count를 인자로 받음)
     */
    public static CategoryResponse fromEntity(Category category, Long count) {
        // name을 URL-friendly한 slug로 변환한다고 가정합니다.
        String generatedSlug = category.getName()
                                       .toLowerCase()
                                       .replaceAll("[^a-z0-9\\s-]", "") // 영문, 숫자, 공백, 하이픈 외 제거
                                       .replaceAll("\\s+", "-"); // 공백을 하이픈으로 치환
        
        return CategoryResponse.builder()
                .name(category.getName())
                .slug(generatedSlug)
                .postCount(count) // ⭐ count 설정
                .build();
    }
}