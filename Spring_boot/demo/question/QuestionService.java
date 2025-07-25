package com.example.demo.question;

import java.util.List;
import java.util.ArrayList;
import java.util.Optional;
import java.time.LocalDateTime;

import com.example.demo.DataNotFoundException;
import com.example.demo.user.SiteUser;

import org.springframework.stereotype.Service;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import lombok.RequiredArgsConstructor;

// 검색 관련 모듈 모음
import com.example.demo.answer.Answer;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Join;
import jakarta.persistence.criteria.JoinType;
import jakarta.persistence.criteria.Predicate;
import jakarta.persistence.criteria.Root;
import org.springframework.data.jpa.domain.Specification;


@RequiredArgsConstructor
@Service
public class QuestionService {
  private final QuestionRepository questionRepository;
  //검색 부분 구현 시작

  private Specification <Question> search(String kw){
    return new Specification <>(){
      private static final long serialVersionUID = 1L;
      @Override
      public Predicate toPredicate(Root<Question> q, CriteriaQuery<?>
      query, CriteriaBuilder cb){
        query.distinct(true); // 중복을 제거
        Join<Question, SiteUser> u1 =q.join("author",JoinType.LEFT);
        Join<Question, Answer> a =q.join("answerList", JoinType.LEFT);
        Join<Answer,SiteUser> u2 = a.join("author", JoinType.LEFT);
        return cb.or(cb.like(q.get("subject"), "%" +kw +"%"),
        cb.like(q.get("content"),"%"+kw+"%"),
        cb.like(u1.get("username"),"%"+kw+"%"),
        cb.like(a.get("content"), "%"+kw+"%"),
        cb.like(u2.get("username"),"%"+kw+"%"));
      }
    };
  }

  //검색 부분 구현 끝
  public Page<Question> getList(int page,String kw) { 
    List<Sort.Order> sorts = new ArrayList<>();
    sorts.add(Sort.Order.desc("createDate"));
    Pageable pageable = PageRequest.of(page,10);
    // Specification<Question> spec = search(kw);
    // return this.questionRepository.findAll(spec,pageable);
    return this.questionRepository.findAllByKeyword(kw, pageable);
  }

  public Question getQuestion(Integer id) {
    Optional<Question> question = this.questionRepository.findById(id);
    if (question.isPresent())
    { return question.get();
    }
    else {
      throw new DataNotFoundException("question not found");

    }    
  }

  public void create(String subject, String content, SiteUser user) {
    Question q =new Question();
    q.setSubject(subject);
    q.setContent(content);
    q.setCreateDate(LocalDateTime.now());
    q.setAuthor(user);
    this.questionRepository.save(q);

  }

  public void modify(Question question, String subject, String content){
    question.setSubject(subject);
    question.setContent(content);
    question.setModifyDate(LocalDateTime.now());
    this.questionRepository.save(question);
  }

  public void delete(Question question){
    this.questionRepository.delete(question);
  }

  public void vote(Question question,SiteUser siteUser){
    question.getVoter().add(siteUser);
    this.questionRepository.save(question);
  }
}

