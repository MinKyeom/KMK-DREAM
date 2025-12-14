package com.mk.user_service.controller;

import com.mk.user_service.dto.SigninRequest;
import com.mk.user_service.entity.User;
import com.mk.user_service.dto.SignupRequest;
import com.mk.user_service.dto.UserResponse;
import com.mk.user_service.exception.DuplicateResourceException;
import com.mk.user_service.security.TokenProvider;
import com.mk.user_service.service.UserService;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid; // ⭐ SignupRequest 유효성 검사를 위해 추가
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.Collections;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
// 프론트엔드와 통신을 위해 CORS 설정 확인
@CrossOrigin(origins = "http://127.0.0.1:5173", allowCredentials = "true") 
public class UserController {

    private final UserService userService;
    private final TokenProvider tokenProvider;
    private final AuthenticationManager authenticationManager; // 로그인 처리에 필요

    /**
     * 1. 회원가입 요청 (POST /user/signup)
     * - @Valid를 통해 DTO 유효성 검사 활성화
     */
    @PostMapping("/signup")
    public ResponseEntity<?> signup(
        // ⭐ 핵심: @Valid를 추가하여 SignupRequest의 유효성 검사 (@NotBlank 등)를 활성화합니다.
        @Valid @RequestBody SignupRequest request, 
        HttpServletResponse response
    ) {
        try {
            // DTO -> Entity 변환
            User user = User.builder()
                            .username(request.username())
                            .password(request.password())
                            .nickname(request.nickname())
                            .build(); 
                            
            User createdUser = userService.create(user);

            // 회원가입 성공 후 자동 로그인 처리 (토큰 생성 및 쿠키 설정)
            String token = tokenProvider.create(createdUser);
            setTokenCookie(response, token, 3600 * 24 * 7); // 7일 유효기간

            // 클라이언트에 ID와 닉네임을 반환하여 localStorage에 저장하도록 유도
            return ResponseEntity.ok(UserResponse.fromEntity(createdUser));

        } 
        // 아이디/닉네임 중복 예외 처리
        catch (DuplicateResourceException e) {
            // Bad Request (400)로 응답하고 오류 메시지를 담아 프론트에 전달
            return ResponseEntity.badRequest() 
                    .body(UserResponse.builder().error(e.getMessage()).build());
        }
        catch (Exception e) {
            // 그 외 알 수 없는 오류
            return ResponseEntity.badRequest() 
                    .body(UserResponse.builder().error("회원가입 중 알 수 없는 오류가 발생했습니다.").build());
        }
    }

    /**
     * 2. 로그인 요청 (POST /user/signin)
     */
    @PostMapping("/signin")
    public ResponseEntity<?> signin(@RequestBody SigninRequest request, HttpServletResponse response) {
        try {
            // 1. Spring Security의 AuthenticationManager를 사용하여 인증 시도
            Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(request.username(), request.password())
            );

            // 2. 인증 객체에서 User 정보 가져오기
            User user = userService.findUserByUsername(request.username());

            // 3. JWT 토큰 생성
            String token = tokenProvider.create(user);

            // 4. HttpOnly 쿠키에 토큰 설정
            setTokenCookie(response, token, 3600 * 24 * 7); // 7일 유효기간

            // 5. 응답 DTO 반환
            return ResponseEntity.ok(UserResponse.fromEntity(user));

        } catch (Exception e) {
            // 인증 실패 시 401 Unauthorized 반환
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED) 
                    .body(UserResponse.builder().error("로그인 정보가 올바르지 않습니다.").build());
        }
    }

    /**
     * 3. 로그아웃 (GET /user/logout)
     */
    @GetMapping("/logout")
    public ResponseEntity<?> logout(HttpServletResponse response) {
        // 토큰 쿠키 만료 (Max-Age를 0으로 설정하여 즉시 삭제)
        setTokenCookie(response, "", 0);
        
        return ResponseEntity.ok().build();
    }


    /**
     * 4. 현재 로그인된 사용자 정보 조회 (GET /user/me)
     */
    @GetMapping("/me")
    public ResponseEntity<UserResponse> getAuthUser(@RequestHeader(value = "Authorization", required = false) String token) {
        try {
            // 토큰에서 사용자 ID 추출 로직 (실제로는 SecurityContext에서 가져옴)
            String userId = tokenProvider.validateAndGetUserId(token.replace("Bearer ", ""));
            
            // 서비스에서 사용자 정보 조회
            User user = userService.findUserById(userId);
            
            return ResponseEntity.ok(UserResponse.fromEntity(user));
        } catch (RuntimeException e) {
            // 인증되지 않은 사용자 또는 토큰 만료
            return ResponseEntity.notFound().build();
        }
    }

    /**
     * 5. Post Service에서 사용자 ID 목록을 기반으로 닉네임 맵을 조회하는 벌크 API
     */
    @PostMapping("/api/users/nicknames")
    public ResponseEntity<Map<String, String>> getNicknamesByIds(@RequestBody List<String> userIds) {
        if (userIds == null || userIds.isEmpty()) {
            return ResponseEntity.ok(Collections.emptyMap());
        }

        Map<String, String> nicknamesMap = userService.getNicknamesByIds(userIds);

        return ResponseEntity.ok(nicknamesMap);
    }

    /**
     * 6. HttpOnly 쿠키에 JWT 토큰을 설정하는 유틸리티 메서드
     */
    private void setTokenCookie(HttpServletResponse response, String token, int maxAge) {
        Cookie cookie = new Cookie("authToken", token);
        cookie.setPath("/");
        cookie.setHttpOnly(true); 
        cookie.setMaxAge(maxAge);

        // 프론트엔드/백엔드 분리 환경에서 SameSite 속성 수동 설정 (크롬 브라우저 정책 대응)
        String sameSite = "Lax";
        
        response.setHeader("Set-Cookie", String.format(
            "%s=%s; Path=%s; Max-Age=%d; HttpOnly; SameSite=%s%s",
            "authToken", 
            token, 
            "/", 
            maxAge, 
            sameSite,
            // HTTPS 환경이 아닌 개발 환경에서는 Secure를 추가하지 않습니다.
            "" 
        ));
    }
}