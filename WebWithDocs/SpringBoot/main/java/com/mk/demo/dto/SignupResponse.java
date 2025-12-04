package com.mk.demo.dto;

public record SignupResponse(
        String id,
        String username,
        String token
) {}
