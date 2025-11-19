package com.mk.demo.dto;

public record SignupRequest (
    String email,
    String password,
    String name
) {}

