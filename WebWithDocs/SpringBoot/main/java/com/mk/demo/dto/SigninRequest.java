package com.mk.demo.dto;

public record SigninRequest(
        String username,
        String password
) {}