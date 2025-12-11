package com.mk.user_service.dto;

public record SigninRequest(
        String username,
        String password
) {}