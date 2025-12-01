package com.mk.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.*;
import org.hibernate.annotations.GenericGenerator;

@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
@Builder
@Table(name = "users") // USER 대신 다른 이름 사용
@Getter @Setter
public class User {

  // id를 기본키로 설정 어노테이션, PK 값을 어떻게 생성할지 지정 어노테이션
  // 유저에게 고유하게 부여되는 id
  @Id 
  @GeneratedValue(generator = "system-uuid")
  @GenericGenerator(name ="system-uuid", strategy ="uuid")
  private String id; // 어노테이션 바로 아래에 있는 id 변수에만 어노테이션 적용 
  
  // 회원 가입에 필요한 정보
  @Column(nullable = false, unique = true)
  private String username; // 원래 이메일에서 변경 아이디로 사용할 유저네임. 이메일일 수도 그냥 문자열일 수도 있다

  private String password;

  private String nickname; // 화면에 표시될 로그인 후 닉네임

  private String authProvider; // 이후 OAuth에서 사용할 유저 정보

}

/*

package com.example.member.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
@Builder
@Table(name = "members")
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false)
    private String name;
}



 */


/*

package com.example.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter @Setter
public class User {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username;
    private String password;
}

 */
