package com.mk.demo.service;

import com.mk.demo.entity.User;
import com.mk.demo.entity.User.Role;
import com.mk.demo.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
@Transactional
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder; 

    // 회원가입
    public User create(final User user) {
        if(user == null || user.getUsername() == null) {
            throw new RuntimeException("Invalid arguments");
        }
        if(userRepository.existsByUsername(user.getUsername())) {
            throw new RuntimeException("Username already exists");
        }

        // 비밀번호 암호화 및 기본 역할 설정
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        user.setRole(Role.ROLE_USER); 
        user.setAuthProvider("LOCAL");
        
        return userRepository.save(user);
    }
    
    // ID로 사용자 찾기 (Controller에서 인증 후 토큰 생성을 위해 사용)
    @Transactional(readOnly = true)
    public User loadUserById(String userId) {
        return userRepository.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found: " + userId));
    }

    // 12_05 추가
    @Transactional(readOnly = true)
    public User loadUserByUsername(String username) {
        return userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found: " + username));
    }
}