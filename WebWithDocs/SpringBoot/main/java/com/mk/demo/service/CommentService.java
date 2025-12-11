package com.mk.demo.service;

import com.mk.demo.dto.CommentRequest;
import com.mk.demo.dto.CommentResponse;
import com.mk.demo.entity.Comment;
import com.mk.demo.entity.Post;
import com.mk.demo.entity.User;
import com.mk.demo.repository.CommentRepository;
import com.mk.demo.repository.PostRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
@Transactional
public class CommentService {
    private final CommentRepository commentRepository;
    private final PostRepository postRepository;
    private final UserService userService; 

    /**
     * 댓글 생성
     */
    public CommentResponse createComment(Long postId, CommentRequest request, String authenticatedUserId) {
        Post post = postRepository.findById(postId).orElseThrow(() -> new RuntimeException("게시글을 찾을 수 없습니다."));
        User user = userService.findUserById(authenticatedUserId); // 인증된 ID로 User Entity 조회

        Comment comment = new Comment();
        comment.setContent(request.getContent());
        comment.setPost(post);
        comment.setUser(user); // User Entity 연결
        
        post.getComments().add(comment); 
        
        return CommentResponse.fromEntity(commentRepository.save(comment));
    }

    /**
     * 댓글 목록 조회
     */
    @Transactional(readOnly = true)
    public List<CommentResponse> getCommentsByPostId(Long postId) {
        List<Comment> comments = commentRepository.findByPost_IdOrderByCreatedAtDesc(postId);
        return CommentResponse.fromEntityList(comments);
    }
    
    /**
     * 댓글 수정
     */
    @Transactional
    public CommentResponse updateComment(Long commentId, CommentRequest request, String authenticatedUserId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("댓글을 찾을 수 없습니다."));

        // 권한 확인: 댓글 작성자의 ID와 인증된 사용자 ID가 일치해야 함
        if (!comment.getUser().getId().equals(authenticatedUserId)) {
            throw new RuntimeException("댓글 수정 권한이 없습니다.");
        }
        
        comment.setContent(request.getContent());
        
        return CommentResponse.fromEntity(comment);
    }
    
    /**
     * 댓글 삭제
     */
    @Transactional
    public void deleteComment(Long commentId, String authenticatedUserId) {
        Comment comment = commentRepository.findById(commentId)
                .orElseThrow(() -> new RuntimeException("댓글을 찾을 수 없습니다."));

        // 권한 확인
        if (!comment.getUser().getId().equals(authenticatedUserId)) {
            throw new RuntimeException("댓글 삭제 권한이 없습니다.");
        }
        
        commentRepository.delete(comment);
    }
}