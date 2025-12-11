package com.mk.user_service.dto;

import lombok.Builder;

@Builder
public record SignupRequest (
    String username,
    String password,
    String nickname // ⭐ 추가: 닉네임 필드
) {}