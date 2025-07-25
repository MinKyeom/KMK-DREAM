package com.example.demo.answer;

import java.time.LocalDateTime;

import java.util.Set;

import com.example.demo.question.Question;
import com.example.demo.user.SiteUser;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EntityListeners;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.ManyToMany;

import lombok.Getter;
import lombok.Setter;


@Getter
@Setter
@Entity

public class Answer {
  @Id
  @GeneratedValue( strategy = GenerationType.IDENTITY )
  private Integer id;

  
  @Column(length = 200)
  private String subject;

  @Column(columnDefinition = "TEXT")
  private String content;

  private LocalDateTime createDate;

  @ManyToOne
  private Question question;  

  @ManyToOne
  private SiteUser author;

  private LocalDateTime modifyDate;

  @ManyToMany
  Set<SiteUser> voter;
}
