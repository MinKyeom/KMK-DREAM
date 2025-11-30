package com.mk.demo.dto;

// import lombok.AllArgsConstructor;
// import lombok.Data;
// import lombok.NoArgsConstructor;

public record SignupRequest (
    String token,
    String username,
    String password,
    String id
) {}



// 가변성이 뛰어난 버전
// @Data
// @Builder
// @NoArgsConstructor
// @AllArgsConstructor
// public class SignupRequest{
//     private String token;
//     private String username;
//     private String password;
//     private String id;
// }