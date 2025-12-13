package com.mk.user_service.security;

import com.mk.user_service.entity.User;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.JwtException; 
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.Key;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.Date;

@Slf4j
@Service
public class TokenProvider {

    @Value("${jwt.secret}")
    private String secretKey;

    private Key getSigningKey() {
        // secretKey는 최소 256비트(32바이트) 길이여야 합니다.
        return Keys.hmacShaKeyFor(secretKey.getBytes(StandardCharsets.UTF_8));
    }

    public String create(User userEntity){
        String authorities = userEntity.getRole() != null ? userEntity.getRole().name() : User.Role.ROLE_USER.name(); 
        
        // ⭐ 수정: 토큰 만료 시간을 1시간에서 7일로 변경 (쿠키 만료 시간과 일치)
        Date expiryDate = Date.from(Instant.now().plus(7, ChronoUnit.DAYS));

        return Jwts.builder()
                .setSubject(userEntity.getId()) // 주체(Subject)를 사용자 ID로 설정
                .claim("roles", authorities) 
                .setIssuer("user_service app")
                .setIssuedAt(new Date())
                .setExpiration(expiryDate)
                .signWith(getSigningKey(), SignatureAlgorithm.HS512)
                .compact();
    }

    /**
     * 1. 토큰 유효성 검증 및 ID 반환. 예외 발생 시 null 반환 (403 오류 방지)
     */
    public String validateAndGetUserId(String token) {
        try {
            Claims claims = Jwts.parserBuilder()
                    .setSigningKey(getSigningKey())
                    .build()
                    .parseClaimsJws(token)
                    .getBody();
            return claims.getSubject();
        } catch (JwtException e) {
            // 토큰이 유효하지 않거나 만료된 경우 예외를 잡아 null 반환
            log.warn("JWT validation failed (returning null): {}", e.getMessage());
            return null; 
        }
    }
    
    /**
     * 2. 토큰에서 역할 추출. 예외 발생 시 null 반환 (403 오류 방지)
     */
    public String getRoleFromToken(String token) {
        try {
            Claims claims = Jwts.parserBuilder()
                    .setSigningKey(getSigningKey())
                    .build()
                    .parseClaimsJws(token)
                    .getBody();
            return claims.get("roles", String.class);
        } catch (JwtException e) {
            log.warn("JWT role extraction failed (returning null): {}", e.getMessage());
            return null; 
        }
    }
}