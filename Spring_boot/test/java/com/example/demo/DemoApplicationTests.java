package com.example.demo;

import java.time.LocalDateTime;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;


@SpringBootTest
class DemoApplicationTests {
	@Autowired
	private QuestionRepository questionRepository;

	@Test
	void contextLoads() {
		// DB 생성

		// Question q1 =new Question();
		// q1.setSubject("sbb가 무엇인가요?");
		// q1.setContent("sbb에 대해서 알고 싶습니다");
		// q1.setCreateDate(LocalDateTime.now());
		// this.questionRepository.save(q1);

		// Question q2 =new Question();
		// q2.setSubject("스프링 부트 모델 질문 입니다.");
		// q2.setContent("id는 자동으로 생성되나요?");
		// q2.setCreateDate(LocalDateTime.now());
		// this.questionRepository.save(q2);

		//Test 검증

		// List<Question> all = this.questionRepository.findAll();
		// assertEquals( 8, all.size());

		// Question q = all.get(0);
		// assertEquals("sbb가 무엇인가요?", q.getSubject());

		// 데이터베이스 내용이 제대로 적재된 지 확인 테스트

		// Optional<Question> oq = this.questionRepository.findById(1);
		// if(oq.isPresent()) {
		// 	Question q = oq.get();
		// 	assertEquals("sbb가 무엇인가요?",q.getSubject());
		
	/* 
	DELETE FROM question
	WHERE id IN (
    SELECT q1.id
    FROM question q1
    JOIN question q2
      ON q1.content = q2.content
     AND q1.id > q2.id
	);
	*/
	
		Question q = this.questionRepository.findBySubject("sbb가 무엇인가요?");
		assertEquals(1,q.getId());
		}
	}


