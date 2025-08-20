/*cf:그럼 그냥 entity로 지정한 클래스 안에 있으면 자동으로 만들어지는데 컬럼에 특정 제약 조건을 주고 싶을때만 컬럼 어노테이션을 쓴다는거지?
ChatGPT의 말:

맞아요! 핵심을 정확히 짚었어요. 👏

정리하면:

@Entity로 지정한 클래스 안의 필드는
→ 자동으로 DB 테이블 컬럼과 매핑됨

기본적인 매핑은
→ 필드명 그대로 컬럼명이 되고
→ 특별한 제약조건 없으면 @Column 안 써도 됨

컬럼에 특별한 제약조건을 주고 싶을 때만
→ @Column 어노테이션을 사용해서 세부 옵션 지정

예시로 다시 보면
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username;   // 그냥 자동 매핑

    @Column(nullable = false, unique = true, length = 50)
    private String email;      // 제약조건을 줄 때는 @Column 필요
}

그래서
상황	@Column 필요 여부
단순 필드명과 컬럼명이 같고 특별한 제약 없으면	필요 없음
컬럼명 변경, 길이 제한, null 불가, 유니크 등 제약 설정할 때	필요함 */


package com.microservice.blog.model; // 패키지 명시 클래스 충돌 방지

import jakarta.persistence.*; //Jpa 어노테이션 기능 존재
import lombok.*; // 여러 기능 함축

@Entity // 데이터베이스랑 연결될 테이블 명시
@Getter // 모든 필드에 대한 getter 자동 생성
@NoArgsConstructor(access =AccessLevel.PROTECTED) //기본 생성자 생성,외부에서 직접 생산 못하게 제한
@AllArgsConstructor // 모든 필드 생성자 자동 생성
@Builder //builder 패턴을 사용할 수 있게 해줌
public class User{

  @Id // 기본키 생성
  @GeneratedValue(strategy = GenerationType.IDENTITY) // 필드값 자동 증가 차후:Mysql DB 사용시 변경 X PostreSQL시 변경
  private Long id;

  private String name; //이름 중복 허용
  
  /*
   * 제약조건	의미
    nullable = false	컬럼에 null 값 저장 금지 (즉, 무조건 값이 있어야 함)
    unique = true	컬럼에 중복된 값 저장 금지 (유일한 값이어야 함)
   */
  
  @Column(nullable = false)
  private String password;

  @Column(nullable = false , unique= true)
  private String email;

}





// 예시1
// package com.microservice.blog.model;

// import jakarta.persistence.*;
// import lombok.*;

// @Entity
// @Table(name = "users")
// @Getter @Setter
// @NoArgsConstructor @AllArgsConstructor
// public class User {
    
//     @Id
//     @GeneratedValue(strategy = GenerationType.IDENTITY)
//     private Long id;

//     @Column(nullable = false, unique = true)
//     private String username;

//     @Column(nullable = false, unique = true)
//     private String email;

//     @Column(nullable = false)
//     private String password;
// }

//예시2
/*
 * package com.example.demo.domain;

import jakarta.persistence.*; // JPA 관련 어노테이션
import lombok.*; // Lombok 라이브러리: 코드 줄여주는 역할

// 데이터베이스 테이블과 매핑될 클래스임을 나타냄
@Entity
@Getter // 모든 필드에 대한 getter 자동 생성
@NoArgsConstructor(access = AccessLevel.PROTECTED) // 기본 생성자 생성, 외부에서 직접 생성 못하게 제한
@AllArgsConstructor // 모든 필드 생성자 자동 생성
@Builder // builder 패턴을 사용할 수 있게 해줌
public class User {

    // 기본 키 (id) 필드, 자동 증가 전략 사용
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // 이메일 필드: not null + 중복 불가
    @Column(nullable = false, unique = true)
    private String email;

    // 비밀번호 필드: not null
    @Column(nullable = false)
    private String password;

    // 이름 필드: null 허용
    private String name;
}
 */