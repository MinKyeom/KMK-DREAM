package com.mk.demo.security;

import com.mk.demo.entity.User;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
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

    // application.yml -> jwt.secret 값을 주입받는다.
    @Value("${jwt.secret}")
    private String secretKey;

    private Key getSigningKey() {
        return Keys.hmacShaKeyFor(secretKey.getBytes(StandardCharsets.UTF_8));
    }

    // JWT 생성
    public String create(User userEntity){

        Date expiryDate = Date.from(
                Instant.now().plus(1, ChronoUnit.DAYS)
        );

        return Jwts.builder()
                .setSubject(userEntity.getId().toString())   // sub
                .setIssuer("demo app")                       // iss
                .setIssuedAt(new Date())                     // iat
                .setExpiration(expiryDate)                   // exp
                .signWith(getSigningKey(), SignatureAlgorithm.HS512)
                .compact();
    }

    // JWT 검증 + userId 반환
    public String validateAndGetUserId(String token) {

        Claims claims = Jwts.parserBuilder()
                .setSigningKey(getSigningKey())
                .build()
                .parseClaimsJws(token)
                .getBody();

        return claims.getSubject();
    }
}







//JWT 버전으로 인해 동작 안하는 버전 
// package com.mk.demo.security;

// import com.mk.demo.entity.User;
// import io.jsonwebtoken.Claims;
// import io.jsonwebtoken.Jwts;
// import io.jsonwebtoken.SignatureAlgorithm;
// import lombok.extern.slf4j.Slf4j;
// import org.springframework.stereotype.Service;

// import java.time.Instant;
// import java.time.temporal.ChronoUnit;
// import java.util.Date;


// @Slf4j
// @Service
// public class TokenProvider {
//   private static final String SECRET_KEY = "fjdshfkjhdsfjkhdfjkdsknjkvnxc";

//   public String create(User userEntity){

//     //기한 지금으로부터 1일로 설정
//     Date expiryDate = Date.from(
//       Instant.now()
//         .plus(1,ChronoUnit.DAYS)
//         );
    
//         /*
//         { // header
//         "aig":"H5512"
//       }.

//       { // payload
//         "sub":"fkjsdhfjkdshfjksd",
//         "iss":"demo app",
//         "iat" : 2595733657,
//         "exp" : 1596597657
//       }.
//       //SECRET_KEY를 이용해 서명한 부분
//       fndklsfjsdklfjsdlkfjksldfsdlkfjsdkl
//       */
//       // JWT Token 생성
//       return Jwts.builder()
//       //header에 들어갈 내용 및 서명을 하기 위한 SECRET_KEY
//       .signWith(SignatureAlgorithm.HS512, SECRET_KEY)
//       // payload에 들어갈 내용
//       .setSubject(userEntity.getId()) // sub
//       .setIssuer("demo app") // iss
//       .setIssuedAt(new Date()) //iat
//       .setExpiration(expiryDate) //exp
//       .compact();
//   }
//   
//   public String validateAndGetUserId(String token){

  //     Claims claims = Jwts.parser()
  //       .setSigningKey(SECRET_KEY
  //       .parseClaimsJws(token)
  //       .getBody();

  //       return claims.getSubject();
  //   }


  // }
