package com.mk.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.mk.demo.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
  User findByUsername(String username);
}



/*
예시 > DB정보 가져오기! 추상화가 목적

package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
}
 */