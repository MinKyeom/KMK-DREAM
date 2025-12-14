// src/components/Comments/Comments.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import React, { useState, useEffect } from "react";
import Link from "next/link"; 
import { 
  fetchCommentsByPostId, 
  createComment, 
  updateComment, 
  deleteComment 
} from "../../services/api/comments"; 
import { useAuth } from "../../providers/AuthProvider"; 
import { useToast } from "../../hooks/useToast"; // ⭐ 추가
import "../../styles/globals.css"; 
import "./Comments.css"; 

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('ko-KR', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
    });
};

// --- 헬퍼 컴포넌트 1: 댓글 작성 폼 (Client Component) --
const CommentForm = ({ postId, onCommentCreated }) => {
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);
  const { showToast } = useToast(); // ⭐ 추가

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (content.trim() === "" || loading) {
        showToast({ message: "댓글 내용을 입력해주세요.", type: "warning" });
        return;
    }

    setLoading(true);
    try {
      // API 호출
      const newComment = await createComment(postId, { content: content.trim() });
      
      // 부모 컴포넌트에 새 댓글 전달
      onCommentCreated(newComment);
      
      setContent(""); // 입력창 초기화
      showToast({ message: "댓글이 성공적으로 작성되었습니다.", type: "success" }); // ⭐ alert 대체
    } catch (error) {
      showToast({ message: error.message || "댓글 작성 실패: 로그인 또는 서버 오류", type: "error" }); // ⭐ alert 대체
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
        required
        disabled={loading}
      />
      <button 
        type="submit" 
        className="btn-primary" 
        disabled={loading || content.trim() === ""}
      >
        {loading ? "작성 중..." : "댓글 작성"}
      </button>
    </form>
  );
};

// --- 헬퍼 컴포넌트 2: 단일 댓글 아이템 (Client Component) --
const CommentItem = ({ comment, currentUserId, onDelete, onUpdate }) => {
    const isAuthor = currentUserId && (currentUserId.toString() === comment.authorId.toString());
    const [isEditing, setIsEditing] = useState(false);
    const [editedContent, setEditedContent] = useState(comment.content);
    const [loading, setLoading] = useState(false);
    const { showToast } = useToast(); // ⭐ 추가

    const handleEditSubmit = async (e) => {
        e.preventDefault();
        if (editedContent.trim() === comment.content || loading) {
            setIsEditing(false);
            return;
        }

        setLoading(true);
        try {
            const updatedComment = await updateComment(comment.id, { content: editedContent.trim() });
            onUpdate(updatedComment); // 부모 상태 업데이트
            setIsEditing(false); // 수정 모드 종료
            showToast({ message: "댓글이 수정되었습니다.", type: "success" });
        } catch (error) {
            showToast({ message: error.message || "댓글 수정 실패: 권한 또는 서버 오류", type: "error" });
            console.error(error);
        } finally {
            setLoading(false);
        }
    };
    
    const handleDeleteClick = () => {
        // window.confirm은 유지 (대체할 커스텀 모달이 없으므로)
        if (window.confirm("정말로 이 댓글을 삭제하시겠습니까?")) {
            onDelete(comment.id);
        }
    };

    return (
        <div className="comment-item">
            <div className="comment-meta">
                <span>
                    <span className="comment-author">{comment.authorNickname || "알 수 없음"}</span>
                    <span className="comment-date">{formatDate(comment.createdAt)}</span>
                </span>
                {isAuthor && (
                    <div className="comment-actions">
                        <button onClick={() => setIsEditing(true)} disabled={loading}>수정</button>
                        <button onClick={handleDeleteClick} disabled={loading}>삭제</button>
                    </div>
                )}
            </div>
            
            {isEditing ? (
                <form className="comment-edit-form" onSubmit={handleEditSubmit}>
                    <textarea
                        value={editedContent}
                        onChange={(e) => setEditedContent(e.target.value)}
                        rows="3"
                        required
                        disabled={loading}
                    />
                    <div style={{ display: 'flex', gap: '10px', marginTop: '10px', justifyContent: 'flex-end' }}>
                        <button type="button" onClick={() => setIsEditing(false)} className="btn-secondary-small">취소</button>
                        <button type="submit" className="btn-primary-small" disabled={loading}>
                            {loading ? "저장 중..." : "저장"}
                        </button>
                    </div>
                </form>
            ) : (
                <div className="comment-content">{comment.content}</div>
            )}
        </div>
    );
};


// --- 메인 컴포넌트: 댓글 목록 ---
export default function Comments({ postId }) {
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);
  const { id: currentUserId } = useAuth();
  const { showToast } = useToast(); // ⭐ 추가

  // 댓글 목록 불러오기
  useEffect(() => {
    const loadComments = async () => {
      try {
        setLoading(true);
        const data = await fetchCommentsByPostId(postId);
        setComments(data);
      } catch (error) {
        showToast({ message: "댓글 목록을 불러오는 데 실패했습니다.", type: "error" });
        console.error("Failed to fetch comments:", error);
      } finally {
        setLoading(false);
      }
    };

    loadComments();
  }, [postId, showToast]);

  // 새 댓글이 작성되었을 때 목록 업데이트
  const handleCommentCreated = (newComment) => {
    setComments((prev) => [...prev, newComment]);
  };
  
  // 댓글이 수정되었을 때 목록 업데이트
  const handleCommentUpdated = (updatedComment) => {
    setComments((prev) => prev.map(c => c.id === updatedComment.id ? updatedComment : c));
  };


  // 댓글 삭제 로직 (CommentItem에서 호출)
  const handleDelete = async (commentId) => {
    try {
      await deleteComment(commentId);
      setComments((prev) => prev.filter(c => c.id !== commentId));
      showToast({ message: "댓글이 삭제되었습니다.", type: "success" }); // ⭐ alert 대체
    } catch (error) {
      showToast({ message: error.message || "댓글 삭제 실패: 권한 또는 서버 오류", type: "error" }); // ⭐ alert 대체
      console.error(error);
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
          <Link href="/signin" className="btn-link-primary">로그인</Link>
          하시면 댓글을 작성할 수 있습니다.
        </p>
      )}
      
      {/* 댓글 목록 */}
      <div className="comments-list">
        {loading ? (
          <p className="loading-message">댓글을 불러오는 중입니다...</p>
        ) : comments.length > 0 ? (
          comments.map((comment) => (
            <CommentItem 
              key={comment.id}
              comment={comment}
              currentUserId={currentUserId}
              onDelete={handleDelete}
              onUpdate={handleCommentUpdated}
            />
          ))
        ) : (
          <p className="no-comments">아직 댓글이 없습니다.</p>
        )}
      </div>
    </div>
  );
}