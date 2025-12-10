package com.mk.demo.dto;

import lombok.Builder;

@Builder
public record SignupRequest (
    String username,
    String password,
    String nickname // ⭐ 추가: 닉네임 필드
) {}