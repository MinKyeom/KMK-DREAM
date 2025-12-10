package com.mk.demo.dto;

import lombok.Builder;

@Builder
public record UserResponse (
    String id,
    String username,
    String nickname, // ⭐ 추가: 닉네임 필드
    String token,
    String error
) {}