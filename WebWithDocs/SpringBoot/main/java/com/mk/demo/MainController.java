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
