package com.example.demo.answer;
import org.springframework.data.jpa.repository.JpaRepository;;

public interface AnswerRepository extends JpaRepository<Answer, Integer> {
  
}
