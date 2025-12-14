// uploaded:SignupRequest.java

package com.mk.user_service.dto;

import jakarta.validation.constraints.NotBlank; // ⭐ 추가
import lombok.Builder;

@Builder
public record SignupRequest (
    // ⭐ 수정: 빈 값/null 허용 안 함
    @NotBlank(message = "사용자 이름은 필수 입력 항목입니다.") 
    String username,
    
    // ⭐ 수정: 빈 값/null 허용 안 함 + 비밀번호 길이 조건 추가를 고려 (필요 시 @Size 추가)
    @NotBlank(message = "비밀번호는 필수 입력 항목입니다.") 
    String password,
    
    // ⭐ 수정: 빈 값/null 허용 안 함
    @NotBlank(message = "닉네임은 필수 입력 항목입니다.") 
    String nickname 
) {}