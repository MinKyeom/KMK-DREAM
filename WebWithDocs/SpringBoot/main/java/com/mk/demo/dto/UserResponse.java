package com.mk.demo.dto;

import lombok.Builder;

@Builder
public record UserResponse (
    String id,
    String username,
    String token,
    String error
) {}