package com.mk.demo.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.GenericGenerator;

import java.util.UUID;

@Entity
@Getter @Setter
// Lombok Builder, NoArgsConstructor, AllArgsConstructor 추가 (UserController 사용 방식에 맞춤)
@Builder 
@NoArgsConstructor 
@AllArgsConstructor
public class User {
    // String ID 사용 (UserRepository에 맞춤)
    @Id 
    @GeneratedValue(generator = "uuid2")
    @GenericGenerator(name = "uuid2", strategy = "uuid2")
    private String id; 
    
    @Column(nullable = false, unique = true)
    private String username; 
    
    private String password;
    
    // ⭐ 닉네임 추가 및 UNIQUE 설정 (요청 사항)
    @Column(nullable = false, unique = true) 
    private String nickname; 

    @Enumerated(EnumType.STRING)
    private Role role;

    public enum Role { ROLE_USER, ROLE_ADMIN }
}