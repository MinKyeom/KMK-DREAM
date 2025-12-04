package com.mk.demo.repository;

import com.mk.demo.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, String> {
    Optional<User> findByUsername(String username); // ⭐ Optional 반환
    Boolean existsByUsername(String username);
}