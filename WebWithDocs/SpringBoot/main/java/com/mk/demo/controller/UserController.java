package com.mk.demo.controller;

import com.mk.demo.dto.SigninRequest;
import com.mk.demo.entity.User;
import com.mk.demo.dto.SignupRequest;
import com.mk.demo.dto.UserResponse;
import com.mk.demo.security.TokenProvider;
import com.mk.demo.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
@CrossOrigin(origins = "http://127.0.0.1:5173") 
public class UserController {

    private final UserService userService;
    private final TokenProvider tokenProvider;
    private final AuthenticationManager authenticationManager; 

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@RequestBody SignupRequest request) {
        // ⭐ 수정: 닉네임 필드를 포함하여 User 엔티티 생성
        User user = User.builder()
                .username(request.username())
                .password(request.password()) 
                .nickname(request.nickname()) // ⭐ 추가
                .build();

        try {
            User savedUser = userService.create(user);
            String token = tokenProvider.create(savedUser); 
            
            return ResponseEntity.ok(
                UserResponse.builder()
                    .id(savedUser.getId())
                    .username(savedUser.getUsername())
                    .nickname(savedUser.getNickname()) // ⭐ 추가
                    .token(token)
                    .build()
            );
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest()
                    .body(UserResponse.builder().error(e.getMessage()).build());
        }
    }

    @PostMapping("/signin")
    public ResponseEntity<?> signin(@RequestBody SigninRequest request) {
        
        UsernamePasswordAuthenticationToken authToken = 
            new UsernamePasswordAuthenticationToken(request.username(), request.password());

        try {
            Authentication authentication = authenticationManager.authenticate(authToken);
            
            String username = authentication.getName(); 
            
            User user = userService.findUserByUsername(username); 
            
            String token = tokenProvider.create(user);
            
            // ⭐ 수정: 닉네임 필드를 포함하여 응답 DTO 생성
            UserResponse response = UserResponse.builder()
                    .id(user.getId())
                    .username(user.getUsername())
                    .nickname(user.getNickname()) // ⭐ 추가
                    .token(token)
                    .build();
            return ResponseEntity.ok(response);

        } catch (Exception e) {
            return ResponseEntity.badRequest()
                    .body(UserResponse.builder().error("로그인 실패: 사용자 이름 또는 비밀번호가 올바르지 않습니다.").build());
        }
    }
}