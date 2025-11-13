package com.mk.demo.controller;

import org.springframework.web.bind.annotation.*;
// import com.example.demo.entity.User;
// import com.example.demo.repository.UserRepository;

@RestController
@RequestMapping("/user")
public class UserController {
  
  // 아직 안만듬
  // private final UserRepository repo;

  // 생성자 초기화
  // public UserController(UserRepository repo){
    // this.repo = repo;
  //}
  
  // 회원가입 API
  // @PostMapping("/signup")
  // public User signup(@RequestBody User user){
      // return repo.save(user);
  //}
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