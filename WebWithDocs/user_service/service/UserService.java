package com.mk.user_service.service;

import com.mk.user_service.entity.User;
import com.mk.user_service.repository.UserRepository;
import com.mk.user_service.exception.DuplicateResourceException; // ⭐ 변경: 새로 추가된 예외 import
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List; // ⭐ 추가
import java.util.Map;   // ⭐ 추가
import java.util.stream.Collectors; // ⭐ 추가

@Slf4j
@Service
@Transactional
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    /**
     * 회원가입 (사용자 생성)
     */
    public User create(final User user) {
        // ⭐ 수정: 닉네임 null 체크 추가
        if (user == null || user.getUsername() == null || user.getNickname() == null) {
            throw new RuntimeException("유효하지 않은 인수입니다.");
        }
        final String username = user.getUsername();
        final String nickname = user.getNickname();

        if (userRepository.existsByUsername(username)) {
            log.warn("이미 존재하는 사용자 이름: {}", username);
            // ⭐ 수정: DuplicateResourceException 사용
            throw new DuplicateResourceException("이미 존재하는 사용자 이름입니다.");
        }

        // ⭐ 추가: 닉네임 중복 확인
        if (userRepository.existsByNickname(nickname)) {
            log.warn("이미 존재하는 닉네임: {}", nickname);
            // ⭐ 수정: DuplicateResourceException 사용
            throw new DuplicateResourceException("이미 존재하는 닉네임입니다.");
        }

        String encodedPassword = passwordEncoder.encode(user.getPassword());
        user.setPassword(encodedPassword);

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

    /**
     * ID로 사용자 조회 (Post Service에서 닉네임 조회에 사용됨)
     */
    @Transactional(readOnly = true)
    public User findUserById(String id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("사용자를 찾을 수 없습니다."));
    }

    /**
     * ⭐ 신규 추가: ID 목록으로 사용자 닉네임 맵 조회 (Post Service용 벌크 API)
     */
    @Transactional(readOnly = true)
    public Map<String, String> getNicknamesByIds(List<String> userIds) {
        // ID 목록을 사용하여 모든 사용자 엔티티를 조회하고, ID와 닉네임을 매핑한 Map을 생성
        return userRepository.findAllById(userIds).stream()
                .collect(Collectors.toMap(User::getId, User::getNickname));
    }
}