package com.mk.demo.dto;

public record UserResponse (
        Long id,
        String email,
        String name
) {}
