package com.mk.demo.controller;

import org.springframework.web.bind.annotation.*;
import com.mk.demo.entity.User;
import com.mk.demo.repository.UserRepository;

import com.mk.demo.dto.UserResponse;
import com.mk.demo.dto.SignupRequest;
import com.mk.demo.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequiredArgsConstructor
@CrossOrigin(origins = "http://127.0.0.1:5173") // React dev 서버 허용
@RequestMapping("/user")
public class UserController {
  
  // 아직 안만듬
  private final UserRepository repo;

  private final UserService userService;
  
  // 생성자 초기화
  // public UserController(UserRepository repo){
  //   this.repo = repo;
  // }
  
  @PostMapping("/signup")
    public ResponseEntity<UserResponse> signup(@RequestBody SignupRequest request) {
        UserResponse response = userService.register(request);
        return ResponseEntity.ok(response);
    }

  // // 회원가입 API
  // @PostMapping("/signup")
  // public User signup(@RequestBody User user){
  //     return repo.save(user);
  // }

  
  
  
  
  @GetMapping("/{id}")
  public User getUserById(@PathVariable Long id) {
      return repo.findById(id).orElse(null); // 없으면 null 반환
}

}


// ex 예시
/*
package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;

@RestController
@RequestMapping("/users")
public class UserController {

    private final UserRepository repo;

    public UserController(UserRepository repo) {
        this.repo = repo;
    }

    // 회원가입 API
    @PostMapping("/signup")
    public User signup(@RequestBody User user) {
        return repo.save(user);
    }
}

 */