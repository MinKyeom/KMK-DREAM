package com.example.demo.answer;


import com.example.demo.question.Question;
import com.example.demo.question.QuestionService;
import com.example.demo.user.SiteUser;
import com.example.demo.user.UserService;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.security.access.prepost.PreAuthorize;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;

import java.security.Principal;

@RequestMapping("/answer")
@RequiredArgsConstructor
@Controller

public class AnswerController {
  private final QuestionService questionService;
  private final AnswerService answerService;
  private final UserService userService;

  @PreAuthorize("isAuthenticated()")
  @PostMapping("/create/{id}")
  public String createAnswer(Model model, @PathVariable("id") Integer id, @Valid AnswerForm answerForm,
  BindingResult bindingResult, Principal principal){
    Question question = this.questionService.getQuestion(id);
    SiteUser siteUser = this.userService.getUser(principal.getName());

    if (bindingResult.hasErrors()) {
      model.addAttribute("question", question);
      return "question_detail";
    }
  this.answerService.create(question, answerForm.getContent(),siteUser);
  // @RequestParam(value="content") String content) {
  //   Question question = this.questionService.getQuestion(id);
  //   this.answerService.create(question,content);
    return String.format("redirect:/question/detail/%s",id);
  }
}

