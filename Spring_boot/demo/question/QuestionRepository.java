package com.example.demo.question;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

// import org.springframework.data.jpa.repository.JpaRepository;

public interface QuestionRepository extends JpaRepository<Question,Integer> {
  Question findBySubject(String subject);
  Question findBySubjectAndContent(String subject,String content);
  List<Question> findBySubjectLike(String subject);
  Page<Question> findAll(Pageable pageable);
}
