package com.mk.user_service.controller;

import com.mk.user_service.dto.SigninRequest;
import com.mk.user_service.entity.User;
import com.mk.user_service.dto.SignupRequest;
import com.mk.user_service.dto.UserResponse;
import com.mk.user_service.exception.DuplicateResourceException; // ⭐ 변경: 새로 추가된 예외 import
import com.mk.user_service.security.TokenProvider;
import com.mk.user_service.service.UserService;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.*;

import java.util.Collections; // ⭐ 추가: Collections 임포트
import java.util.List;        // ⭐ 추가: List 임포트
import java.util.Map;         // ⭐ 추가: Map 임포트

@RestController
@RequestMapping("/user")
@RequiredArgsConstructor
@CrossOrigin(origins = "http://127.0.0.1:5173", allowCredentials = "true") // CORS 설정 확인
public class UserController {

    private final UserService userService;
    private final TokenProvider tokenProvider;
    private final AuthenticationManager authenticationManager;

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@RequestBody SignupRequest request, HttpServletResponse httpResponse) {
        // 닉네임 포함하여 User 객체 생성
        User user = User.builder()
                .username(request.username())
                .password(request.password())
                .nickname(request.nickname())
                .build();

        try {
            User registeredUser = userService.create(user);

            // 회원가입 성공 후 자동 로그인 및 토큰 발급
            // CustomUserDetailsService와 일관성을 위해 Principal을 ID로 설정
            Authentication authentication = new UsernamePasswordAuthenticationToken(
                    registeredUser.getId(), // ⭐ 수정: ID를 Principal로 사용
                    request.password()
            );

            Authentication result = authenticationManager.authenticate(authentication);
            final String token = tokenProvider.create(registeredUser);

            // HttpOnly 쿠키에 토큰 설정 (7일 유효기간)
            setTokenCookie(httpResponse, token, 60 * 60 * 24 * 7);

            // 프론트엔드에는 ID와 닉네임만 전달
            UserResponse response = UserResponse.builder()
                    .id(registeredUser.getId())
                    .nickname(registeredUser.getNickname())
                    .build();

            return ResponseEntity.ok(response);

        } catch (DuplicateResourceException e) {
            // ⭐ 수정: 중복 오류는 409 Conflict로 처리
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        } catch (RuntimeException e) {
            // 기타 런타임 오류 (예: 유효하지 않은 인수)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }
    }

    @PostMapping("/signin")
    public ResponseEntity<UserResponse> signin(@RequestBody SigninRequest request, HttpServletResponse httpResponse) {
        try {
            // 1. 인증 시도
            Authentication authentication = authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(request.username(), request.password())
            );

            // 2. 인증 성공 후 JWT 토큰 생성
            User user = userService.findUserByUsername(request.username());
            final String token = tokenProvider.create(user);

            // 3. HttpOnly 쿠키에 토큰 설정 (7일 유효기간)
            setTokenCookie(httpResponse, token, 60 * 60 * 24 * 7);

            // 4. 사용자 정보 조회 및 응답
            UserResponse response = UserResponse.builder()
                    .id(user.getId())
                    .nickname(user.getNickname())
                    .build();

            return ResponseEntity.ok(response);
        } catch (Exception e) {
            // 인증 실패 (BadCredentialsException 등)
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
        }
    }

    /**
     * 로그아웃 API: HttpOnly 쿠키(authToken)를 즉시 만료시켜 삭제합니다.
     */
    @PostMapping("/logout")
    public ResponseEntity<String> logout(HttpServletResponse httpResponse) {
        setTokenCookie(httpResponse, null, 0); // MaxAge = 0 설정으로 쿠키 삭제
        return ResponseEntity.ok("로그아웃 성공: 인증 쿠키가 삭제되었습니다.");
    }

    /**
     * Post Service에서 사용자 ID를 기반으로 닉네임 정보를 조회하는 API
     */
    @GetMapping("/info/{userId}")
    public ResponseEntity<UserResponse> getUserInfo(@PathVariable String userId) {
        try {
            User user = userService.findUserById(userId);

            UserResponse response = UserResponse.builder()
                    .id(user.getId())
                    .nickname(user.getNickname())
                    .build();

            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    /**
     * ⭐ 신규 추가: Post Service에서 사용자 ID 목록을 기반으로 닉네임 맵을 조회하는 벌크 API
     * URL: POST /user/api/users/nicknames
     */
    @PostMapping("/api/users/nicknames")
    public ResponseEntity<Map<String, String>> getNicknamesByIds(@RequestBody List<String> userIds) {
        if (userIds == null || userIds.isEmpty()) {
            return ResponseEntity.ok(Collections.emptyMap());
        }

        // 1. 서비스 호출
        Map<String, String> nicknamesMap = userService.getNicknamesByIds(userIds);

        // 2. 응답 (Map<String, String> 형태로 반환)
        return ResponseEntity.ok(nicknamesMap);
    }

    /**
     * HttpOnly 쿠키에 JWT 토큰을 설정하는 유틸리티 메서드
     */
    private void setTokenCookie(HttpServletResponse response, String token, int maxAge) {
        Cookie cookie = new Cookie("authToken", token);
        cookie.setPath("/");

        // ⭐ 수정: SameSite=Lax 속성 추가 및 Set-Cookie 헤더 수동 설정
        String sameSite = "Lax";
        response.setHeader("Set-Cookie", String.format("%s=%s; Max-Age=%d; Path=/; HttpOnly; SameSite=%s%s",
                "authToken",
                token == null ? "" : token,
                maxAge,
                sameSite,
                // 개발 환경을 위해 Secure는 false로 유지
                false ? "; Secure" : ""));
    }
}