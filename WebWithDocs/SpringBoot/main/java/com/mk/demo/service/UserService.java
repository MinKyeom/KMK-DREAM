package com.mk.demo.service;

import com.mk.demo.dto.UserResponse;
import com.mk.demo.dto.SignupRequest;
import com.mk.demo.entity.User;
import com.mk.demo.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

//11.30
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Slf4j
@Service
// @RequiredArgsConstructor
public class UserService {

    @Autowired
    private final UserRepository userRepository;

    public User create(final User user) {
        if(user == null || user.getUsername()== null ){
            throw new RuntimeException("Invalid arguments");
        }
        final String username = user.getUsername();
        if(userRepository.existsByUsername(username)){
            log.warn( "Username already exists{}",username);
            throw new RuntimeException("Username already exists");
        }
        return userRepository.save(user);
    }

    public User getByCredentials(final String username,final String password){
        return userRepository.findByUsernameAndPassword(username,password);
    }
}



//     private final PasswordEncoder passwordEncoder;

//     public UserResponse register(SignupRequest dto) {

//         if (memberRepository.existsByEmail(dto.email())) {
//             throw new IllegalArgumentException("이미 존재하는 아이디 입니다.");
//         }

//         User user = User.builder()
//                 .email(dto.email())
//                 .password(passwordEncoder.encode(dto.password()))
//                 .name(dto.name())
//                 .build();

//         User saved = memberRepository.save(user);

//         return new UserResponse(
//                 saved.getId(),
//                 saved.getEmail(),
//                 saved.getName()
//         );
//     }
// }


