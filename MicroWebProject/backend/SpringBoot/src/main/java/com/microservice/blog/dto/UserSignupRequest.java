package com.microservice.blog.dto;

import lombok.Getter;

@Getter
public class UserSignupRequest{
  private String email;
  private String password;
  private String name;
}


/*
 *package com.example.demo.dto;

import lombok.Getter;

// 클라이언트가 보내는 회원가입 요청 데이터를 담는 클래스
@Getter // 각 필드에 대해 getter 자동 생성
public class UserRequestDto {
    private String email;    // 이메일
    private String password; // 비밀번호
    private String name;     // 이름
} 
 * 
 */

// package com.microservice.blog.dto;

// import lombok.Data;

// @Data
// public class UserSignupRequest {
//     private String username;
//     private String email;
//     private String password;
// }

/*

package com.microservice.blog.dto;

public class UserSignupRequest {
    private String email;
    private String username;
    private String password;

    // getter, setter, 생성자 등 추가
}

 */