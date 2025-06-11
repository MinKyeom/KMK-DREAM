package com.example.demo;

import java.time.LocalDateTime;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;


@SpringBootTest
class DemoApplicationTests {
	@Autowired
	private QuestionRepository questionRepository;

	@Test
	void contextLoads() {
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
		List<Question> all = this.questionRepository.findAll();
		assertEquals( 8, all.size());

		Question q = all.get(0);
		assertEquals("sbb가 무엇인가요?", q.getSubject());

	}
}

