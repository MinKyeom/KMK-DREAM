package com.mk.demo.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.GenericGenerator;

@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor
@Builder
@Table(name = "users")
@Getter @Setter
public class User {

    @Id
    @GeneratedValue(generator = "system-uuid")
    @GenericGenerator(name ="system-uuid", strategy ="uuid")
    private String id;

    @Column(nullable = false, unique = true)
    private String username;

    private String password;

    private String nickname; 

    private String authProvider;

    @Enumerated(EnumType.STRING)
    @Column(nullable = true)
    private Role role; // ⭐ JWT를 위한 역할(Role) 필드 추가

    public enum Role {
        ROLE_USER, ROLE_ADMIN
    }
}