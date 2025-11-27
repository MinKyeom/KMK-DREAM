package com.mk.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.mk.demo.entity.User;
import java.util.List;


public interface UserRepository extends JpaRepository<User, Long> {
  // User findByUsername(String username);


  // // 이메일 중복 확인! >> id 중복 확인으로 변경
  // boolean existsByEmail(String email); 

  // 11.28 entity 변경에 따른 코드 수정
  User findByUsername(String username);
  Boolean existsByUsername(String username);
  User findByUsernameAndPassword(String username,String password);
}


/*
package com.example.member.repository;

import com.example.member.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member, Long> {

    boolean existsByEmail(String email);
}

*/


/*
예시 > DB정보 가져오기! 추상화가 목적

package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);
}
 */