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

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;

@Slf4j
@RestController
// @RequiredArgsConstructor
@CrossOrigin(origins = "http://127.0.0.1:5173") // React dev 서버 허용
@RequestMapping("/user")
public class UserController {
  
  // 아직 안만듬
//   private final UserRepository repo;

  @Autowired
  private UserService userService;
  
  // 생성자 초기화
  // public UserController(UserRepository repo){
  //   this.repo = repo;
  // }
  
  @PostMapping("/signup")
  public ResponseEntity<?> registerUser(@RequestBody SignupRequest userDTO){
    try{
        // record로 수정해서 password 부분 가져오는 방식 변경함
        if(userDTO == null || userDTO.password()==null){  
            throw new RuntimeException("Invalid Password value.");
        }
    
    // 요청을 이용해 저장할 유저 만들기
    User user = User.builder()
    .username(userDTO.username())
    .password(userDTO.password())
    .build();
    
    // 서비스를 이용해 리포지터리에 유저 저장
    User registeredUser = userService.create(user);
    SignupRequest responseUserDTO =SignupRequest.builder()
        .id(registeredUser.getId())
        .username(registeredUser.getUsername())
        .build();
        
        return ResponseEntity.ok().body(responseUserDTO);
    } catch (Exception e){
        // 유저 정보는 항상 하나이므로 리스트로 만들어야 하는 ResponseDTO를 사용하지 않고 그냥 UserDTO리턴.

        UserResponse responseDTO = UserResponse.builder().error(e.getLocalizedMessage()).build();
        return ResponseEntity
        .badRequest()
        .body(responseDTO);
    }

    }

    @PostMapping("/signin")
    public ResponseEntity<?> authenticate(@RequestBody UserResponse userDTO){
        User user = userService.getByCredentials(
        userDTO.username(),
        userDTO.password());
    
    if(user != null){
        final UserResponse responseUserDTO = UserResponse.builder()
        .username(user.getUsername())
        .id(user.getId())
        .build();
        return ResponseEntity.ok().body(responseUserDTO); 
    }
    else{
        UserResponse responseDTO = UserResponse.builder()
        .error("Login failed.")
        .build();
    return ResponseEntity
        .badRequest()
        .body(responseDTO);
    }
 } 

}


    // public ResponseEntity<UserResponse> signup(@RequestBody SignupRequest request) {
    //     UserResponse response = userService.register(request);
    //     return ResponseEntity.ok(response);
    // }

  // // 회원가입 API
  // @PostMapping("/signup")
  // public User signup(@RequestBody User user){
  //     return repo.save(user);
  // }
  
//   @GetMapping("/{id}")
//   public User getUserById(@PathVariable Long id) {
//       return repo.findById(id).orElse(null); // 없으면 null 반환
// }



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