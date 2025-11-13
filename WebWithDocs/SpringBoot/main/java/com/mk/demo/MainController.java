package com.mk.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
public class MainController {
  @GetMapping("/start")
  public String start(){
    System.out.println("return과 차이가 있나 프린트문 start"); // CLI 라인에는 나오는 결과 웹 페이지에는 return값만 나옴
    return "Hello";
  }
}

//RestController json으로 불러오는 예시

/* 
@RestController
public class HelloController {

    @GetMapping("/user")
    public User getUser() {
        return new User("Kim", 25);
    }

    // 내부 static class (간단한 예시용)
    static class User {
        private String name;
        private int age;

        public User(String name, int age) {
            this.name = name;
            this.age = age;
        }

        // getter만 있어도 JSON 변환됨
        public String getName() { return name; }
        public int getAge() { return age; }
    }
}

*/
