package com.mk.user_service.dto;

import lombok.Builder;

@Builder
public record UserResponse (
    String id,
    String username,
    String nickname, 
    String error // token 필드 제거
) {}