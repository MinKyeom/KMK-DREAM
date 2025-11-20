package com.mk.demo.service;

import com.mk.demo.dto.UserResponse;
import com.mk.demo.dto.SignupRequest;
import com.mk.demo.entity.User;
import com.mk.demo.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository memberRepository;
    private final PasswordEncoder passwordEncoder;

    public UserResponse register(SignupRequest dto) {

        if (memberRepository.existsByEmail(dto.email())) {
            throw new IllegalArgumentException("이미 존재하는 이메일입니다.");
        }

        User user = User.builder()
                .email(dto.email())
                .password(passwordEncoder.encode(dto.password()))
                .name(dto.name())
                .build();

        User saved = memberRepository.save(user);

        return new UserResponse(
                saved.getId(),
                saved.getEmail(),
                saved.getName()
        );
    }
}


