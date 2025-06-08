// package com.example.demo;
// import org.springframework.streotype.Controller;
// import org.springframework.web.bind.annotation.GetMapping;
// import org.springframework.web.bind.annotation.ResponseBody;

// // hellocontroller 클래스가 컨트롤러의 기능을 수행한다는 것을 알려 준다.
// @Controller 
// public class HelloController {
//   @GetMapping("/heoll")
//   @ResponseBody
//   public String hello() {
//     return "hello";

//   }
  
// }
/*
 * 127.0.0.1:8080/hello 입력 시 redirection으로 login 되는 현상 > 
 * 
 * # Spring Security 비활성화
    spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration
 */

package com.example.demo;

import org.springframework.stereotype.Controller;  // 수정된 부분
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

// HelloController 클래스가 컨트롤러의 기능을 수행한다는 것을 알려 준다.
@Controller
public class HelloController {

    @GetMapping("/hello")  // 수정된 부분 (URL 경로 오류 수정)
    @ResponseBody
    public String hello() {
        return "hello spring boot";
    }
}