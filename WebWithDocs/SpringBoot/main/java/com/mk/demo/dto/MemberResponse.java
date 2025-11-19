package com.mk.demo.dto;

public record MemberResponse (
        Long id,
        String email,
        String name
) {}
