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
    private final AuthenticationManager authenticationManager; // ⭐ 주입

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@RequestBody SignupRequest request) {
        User user = User.builder()
                .username(request.username())
                .password(request.password()) 
                .build();

        try {
            User savedUser = userService.create(user);
            String token = tokenProvider.create(savedUser); 
            
            return ResponseEntity.ok(
                UserResponse.builder()
                    .id(savedUser.getId())
                    .username(savedUser.getUsername())
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
            // ⭐ AuthenticationManager로 인증 처리 (CustomUserDetailsService 호출)
            Authentication authentication = authenticationManager.authenticate(authToken);
            
            // String authenticatedUserId = (String) authentication.getPrincipal(); // ID 추출
            // User user = userService.loadUserById(authenticatedUserId); 

            // String token = tokenProvider.create(user);
            // principal을 UserDetails로 안전하게 사용
            String username = authentication.getName(); // ✅ username 추출
            User user = userService.loadUserByUsername(username); // ID 대신 username으로 조회

            String token = tokenProvider.create(user);
            
            UserResponse response = UserResponse.builder()
                    .id(user.getId())
                    .username(user.getUsername())
                    .token(token)
                    .build();
            return ResponseEntity.ok(response);

        } catch (Exception e) {
            return ResponseEntity.badRequest()
                    .body(UserResponse.builder().error("로그인 실패: 사용자 이름 또는 비밀번호가 올바르지 않습니다.").build());
        }
    }
}