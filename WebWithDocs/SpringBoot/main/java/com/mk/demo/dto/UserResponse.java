package com.mk.demo.dto;

import lombok.Builder;

@Builder
public record UserResponse (
    String token,
    String username,
    String password,
    String id,
    String error
) {}
