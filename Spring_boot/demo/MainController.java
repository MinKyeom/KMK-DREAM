package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;;

@Controller
public class MainController {
  @GetMapping("/demo")
  @ResponseBody

  public String index() {
    return "스프링부트를 시작해봅시다";

  }


  @GetMapping("/")
  public String root(){
    return "redirect:/question/list";

  }
}
