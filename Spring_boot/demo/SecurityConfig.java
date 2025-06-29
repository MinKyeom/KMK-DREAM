// package com.example.demo;

// import org.springframework.context.annotation.Bean;
// import org.springframework.context.annotation.Configuration;
// import org.springframework.security.config.annotation.web.builders.HttpSecurity;
// import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
// import org.springframework.security.web.SecurityFilterChain;
// import org.springframework.security.web.util.matcher.AndRequestMatcher;
// import org.springframework.util.AntPathMatcher;

// @Configuration
// @EnableWebSecurity
// public class SecurityConfig {
//   @Bean
//   SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//     http 
//         .authorizeHttpRequests((authorizeHttpRequests) -> authorizeHttpRequests
//           .requestMatchers(new AntPathMatcher("/**")).permitAll() )
          
//         .csrf((csrf) -> csrf
//         .ignoringRequestMatchers(new AntPathMatcher("/h2-console/**")));
        
//         return http.build();
//   }
  
// }

package com.example.demo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.header.writers.frameoptions.XFrameOptionsHeaderWriter;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configration.AuthenticationConfiguration;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@EnableWebSecurity
public class SecurityConfig {
  
  @Bean
  SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http 
        .authorizeHttpRequests((authorizeHttpRequests) -> authorizeHttpRequests
          .requestMatchers(new AntPathRequestMatcher("/**")).permitAll() ) // 올바르게 AntPathRequestMatcher 사용

        .csrf((csrf) -> csrf
        .ignoringRequestMatchers(new AntPathRequestMatcher("/h2-console/**"))) // 올바르게 AntPathRequestMatcher 사용
        
//         .authorizeHttpRequests((authorizeHttpRequests) -> authorizeHttpRequests
//           .requestMatchers(new AntPathMatcher("/**")).permitAll() )
          
//         .csrf((csrf) -> csrf
//         .ignoringRequestMatchers(new AntPathMatcher("/h2-console/**")));
        .headers((headers) -> headers
          .addHeaderWriter(new XFrameOptionsHeaderWriter(
            XFrameOptionsHeaderWriter.XFrameOptionsMode.SAMEORIGIN)))
          
        .formLogin( (formLogin) -> formLogin
          .loginPage("/user/login")
          .defaultSuccessUrl("/")) 
          ;
    return http.build();
  }

  @Bean
  PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
  }
  
}
