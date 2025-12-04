package com.mk.demo.dto;

import lombok.Builder;

@Builder
public record SignupRequest (
    String username,
    String password
) {}