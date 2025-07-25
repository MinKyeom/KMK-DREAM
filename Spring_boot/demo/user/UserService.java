package com.example.demo.user;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

import java.util.Optional;

import com.example.demo.DataNotFoundException;

@RequiredArgsConstructor
@Service


public class UserService {

  private final UserRepository userRepository;
  private final PasswordEncoder passwordEncoder;

  public SiteUser create(String username, String email, String password) {

    SiteUser user = new SiteUser();
    user.setUsername(username);
    user.setEmail(email);
    // BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
    user.setPassword(passwordEncoder.encode(password));
    this.userRepository.save(user);
    return user;
  }

  public SiteUser getUser(String username){
    Optional<SiteUser> siteUser = this.userRepository.findByUsername(username);
    if (siteUser.isPresent()){
      return siteUser.get();

    } else {
      throw new DataNotFoundException("siteuser not found");
    }

  }
  
}
