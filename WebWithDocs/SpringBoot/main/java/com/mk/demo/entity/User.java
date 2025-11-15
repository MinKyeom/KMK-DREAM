package com.mk.demo.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter @Setter
public class User {

  // id를 기본키로 설정 어노테이션, PK 값을 어떻게 생성할지 지정 어노테이션
  @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id; // 어노테이션 바로 아래에 있는 id 변수에만 어노테이션 적용 
  
  private String username;
  private String password;

}

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
