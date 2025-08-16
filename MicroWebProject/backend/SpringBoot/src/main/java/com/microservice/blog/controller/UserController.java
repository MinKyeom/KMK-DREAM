/*
 * 이해과정: 자바 스프링에서는 모든 파일은 패키지가 필요하다 default로 지정해버리면 파일 이름이 같으면 구분불가
 */
package com.microservice.blog.controller;


import com.microservice.blog.dto.UserSignupRequest;
import com.microservice.blog.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/*
 * 
이 클래스가 HTTP 요청을 처리하는 컨트롤러라는 것을 나타냄.

메서드에서 리턴하는 값이 **HTTP 응답 본문(response body)**에 직접 담기도록 해줌 (JSON, XML 등).

HTML 뷰를 반환하지 않고, 데이터(JSON 등)만 반환.
 */
@RestController

@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PostMapping("/signup")
    public ResponseEntity<String> signup(@RequestBody UserSignupRequest request) {
        try {
            userService.signup(request);
            return ResponseEntity.ok("Signup successful");
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}
