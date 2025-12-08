package com.mk.demo.service;

import com.mk.demo.entity.User;
import com.mk.demo.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Slf4j
@Service
@Transactional
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder; // ⭐ 추가: 비밀번호 인코더 주입

    /**
     * 회원가입 (사용자 생성)
     */
    public User create(final User user) {
        if (user == null || user.getUsername() == null) {
            throw new RuntimeException("유효하지 않은 인수입니다.");
        }
        final String username = user.getUsername();

        if (userRepository.existsByUsername(username)) {
            log.warn("이미 존재하는 사용자 이름: {}", username);
            throw new RuntimeException("이미 존재하는 사용자 이름입니다.");
        }

        // ⭐ 수정: 비밀번호 인코딩 및 기본 역할 부여
        String encodedPassword = passwordEncoder.encode(user.getPassword());
        user.setPassword(encodedPassword);
        
        // 기본 역할 부여
        if (user.getRole() == null) {
            user.setRole(User.Role.ROLE_USER);
        }
        
        return userRepository.save(user);
    }

    /**
     * 사용자 이름으로 사용자 조회 (로그인 시 토큰 생성에 사용)
     */
    public User findUserByUsername(String username) {
        return userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("사용자를 찾을 수 없습니다."));
    }

    // ... 다른 사용자 관련 로직 (필요하다면) ...
}