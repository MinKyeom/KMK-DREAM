// src/components/Comments.jsx (수정 완료 코드)

import React, { useState, useEffect } from "react";
import { 
  fetchCommentsByPostId, 
  createComment, 
  updateComment, 
  deleteComment 
} from "../api/comments";
// ⭐ [CRITICAL FIX] getAuthUser 대신 useAuth 훅 임포트
import { useAuth } from "../context/AuthContext.jsx"; 
import { Link } from "react-router-dom";
import "../App.css"; // 공통 스타일 및 버튼 사용
import "./Comments.css"; // 댓글 전용 스타일 임포트

// --- 헬퍼 컴포넌트 1: 댓글 작성 폼 ---
const CommentForm = ({ postId, onCommentCreated }) => {
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (content.trim() === "" || loading) return;

    setLoading(true);
    try {
      // 서버에 댓글 생성 요청
      const newComment = await createComment(postId, { content: content });
      
      // 부모 컴포넌트에 새로운 댓글 전달
      onCommentCreated(newComment);
      
      // 폼 초기화
      setContent("");
      
    } catch (error) {
      alert(error.message || "댓글 작성 실패: 로그인 상태를 확인하세요.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="comment-form" onSubmit={handleSubmit}>
      <textarea
        placeholder="댓글을 입력하세요..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
        rows="4"
        maxLength="500" // 최대 길이 제한
        required
      />
      <div className="form-action">
        <span className="char-count">{content.length} / 500</span>
        <button 
          type="submit" 
          className="btn-primary" 
          disabled={loading || content.trim() === ""}>
          {loading ? "작성 중..." : "댓글 작성"}
        </button>
      </div>
    </form>
  );
};

// --- 헬퍼 컴포넌트 2: 댓글 아이템 ---
const CommentItem = ({ comment, currentUserId, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editContent, setEditContent] = useState(comment.content);

  const isAuthor = currentUserId === comment.authorId;
  const formatDate = (dateString) => new Date(dateString).toLocaleString();

  const handleEditSubmit = (e) => {
    e.preventDefault();
    if (editContent.trim() === "" || editContent === comment.content) return;
    
    // 부모 컴포넌트의 onUpdate 핸들러 호출
    onUpdate(comment.id, { content: editContent })
      .then(() => setIsEditing(false))
      .catch((error) => console.error("댓글 수정 실패:", error));
  };
  
  return (
    <div className="comment-item">
      <div className="comment-meta">
        <div>
          <span className="comment-author">{comment.authorNickname || "알 수 없음"}</span>
          <span className="comment-date">
             {formatDate(comment.createdAt)}
             {comment.updatedAt && comment.createdAt !== comment.updatedAt && (
                <span> (수정됨)</span>
             )}
          </span>
        </div>
      </div>
      
      {isEditing ? (
        <form onSubmit={handleEditSubmit} className="edit-form">
          <textarea
            value={editContent}
            onChange={(e) => setEditContent(e.target.value)}
            rows="3"
            maxLength="500"
            required
            className="edit-textarea"
          />
          <div className="comment-actions">
            <button type="submit" className="btn-primary btn-sm">저장</button>
            <button type="button" className="btn-secondary btn-sm" onClick={() => setIsEditing(false)}>취소</button>
          </div>
        </form>
      ) : (
        <div className="comment-content">
          {comment.content}
        </div>
      )}
      
      {/* 작성자만 수정/삭제 버튼 표시 */}
      {isAuthor && !isEditing && (
        <div className="comment-actions">
          <button onClick={() => setIsEditing(true)} className="btn-link">
            수정
          </button>
          <button onClick={() => onDelete(comment.id)} className="btn-link btn-danger">
            삭제
          </button>
        </div>
      )}
    </div>
  );
};


// --- 메인 컴포넌트: Comments ---
export default function Comments({ postId }) {
  // ⭐ [CRITICAL FIX] useAuth 훅을 사용하여 인증 상태에 반응하도록 변경
  const { id: currentUserId } = useAuth(); 
  
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);

  // 1. 댓글 목록 불러오기
  useEffect(() => {
    const loadComments = async () => {
      setLoading(true);
      try {
        const data = await fetchCommentsByPostId(postId);
        // 서버에서 최신 댓글 순으로 정렬되어 온다고 가정하고 상태 업데이트
        setComments(data); 
      } catch (error) {
        console.error("Error fetching comments:", error);
      } finally {
        setLoading(false);
      }
    };
    loadComments();
  }, [postId]);

  // 2. 새로운 댓글 생성 핸들러
  const handleCommentCreated = (newComment) => {
    // 가장 최근 댓글이 위로 올라오도록 추가
    setComments((prev) => [newComment, ...prev]); 
  };
  
  // 3. 댓글 수정 핸들러 (CommentItem에서 호출됨)
  const handleCommentUpdate = async (commentId, updateData) => {
    try {
      // 서버에서 댓글 수정
      const updatedComment = await updateComment(commentId, updateData);
      
      // 상태 업데이트: 댓글 목록에서 해당 댓글을 찾아서 교체
      setComments((prev) => 
        prev.map(c => c.id === commentId ? { ...c, content: updatedComment.content, updatedAt: updatedComment.updatedAt } : c)
      );
      alert("댓글이 수정되었습니다.");
      return updatedComment; // CommentItem에서 Promise 반환에 사용
    } catch (error) {
      alert(error.message || "댓글 수정 실패: 권한 또는 서버 오류");
      console.error(error);
      throw error;
    }
  };
  
  // 4. 댓글 삭제 핸들러
  const handleCommentDelete = async (commentId) => {
    if (window.confirm("정말로 이 댓글을 삭제하시겠습니까?")) {
      try {
        // 서버에서 댓글 삭제
        await deleteComment(commentId);
        // 목록에서 삭제
        setComments((prev) => prev.filter(c => c.id !== commentId));
        alert("댓글이 삭제되었습니다.");
      } catch (error) {
        alert(error.message || "댓글 삭제 실패: 권한 또는 서버 오류");
        console.error(error);
      }
    }
  };

  return (
    <div className="comments-section">
      <h2 className="section-title">댓글 ({comments.length})</h2> 
      
      {/* 댓글 작성 폼 (로그인 사용자에게만 표시) */}
      {currentUserId ? (
        <CommentForm postId={postId} onCommentCreated={handleCommentCreated} />
      ) : (
        <p className="login-prompt">
          <Link to="/signin" className="btn-link-primary">로그인</Link>
          하시면 댓글을 작성할 수 있습니다.
        </p>
      )}
      
      {/* 댓글 목록 */}
      <div className="comments-list">
        {loading ? (
          <p>댓글을 불러오는 중입니다...</p>
        ) : comments.length > 0 ? (
          comments.map((comment) => (
            <CommentItem 
              key={comment.id}
              comment={comment}
              currentUserId={currentUserId}
              onUpdate={handleCommentUpdate} 
              onDelete={handleCommentDelete}
            />
          ))
        ) : (
          <p className="no-comments">아직 작성된 댓글이 없습니다. 첫 댓글을 남겨보세요!</p>
        )}
      </div>
    </div>
  );
}