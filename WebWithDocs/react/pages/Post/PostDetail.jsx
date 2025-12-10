// src/pages/Post/PostDetail.jsx

import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { fetchPostById, deletePost } from "../../api/posts";
import { useAuth } from "../../context/AuthContext.jsx"; 
import Comments from "../../components/Comments.jsx"; 
import "../../App.css"; 

export default function PostDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);

  // 현재 로그인된 사용자 ID를 가져옵니다.
  const { id: currentUserId } = useAuth(); 

  useEffect(() => {
    const loadPost = async () => {
      setLoading(true);
      try {
        const data = await fetchPostById(id);
        setPost(data);
      } catch (error) {
        console.error("Error fetching post:", error);
        alert("글을 찾을 수 없거나 불러오지 못했습니다.");
        // 글을 찾지 못하거나 오류 발생 시 목록 페이지로 리다이렉트
        navigate("/post"); 
      } finally {
        setLoading(false);
      }
    };
    loadPost();
  }, [id, navigate]);

  // 게시글 작성자와 현재 로그인 사용자가 동일한지 확인
  const isAuthor = post && post.authorId === currentUserId; 

  const handleDelete = async () => {
    if (window.confirm("정말로 이 글을 삭제하시겠습니까?")) {
      try {
        await deletePost(id);
        alert("글이 삭제되었습니다.");
        navigate("/post");
      } catch (error) {
        console.error("Error deleting post:", error);
        alert(error.response?.data?.error || "글 삭제에 실패했습니다.");
      }
    }
  };

  if (loading) {
    return <div className="post-detail-container">로딩 중...</div>;
  }

  if (!post) {
    return <div className="post-detail-container">글을 찾을 수 없습니다.</div>;
  }
  
  const formatDate = (dateString) => new Date(dateString).toLocaleDateString();

  return (
    <div className="post-detail-container" style={{ padding: '0 20px', backgroundColor: 'var(--color-primary)', borderRadius: '12px', boxShadow: '0 4px 15px var(--color-shadow)' }}>
      <div className="post-detail-header" style={{ paddingTop: '30px', paddingBottom: '20px', borderBottom: '1px solid var(--color-border)' }}>
        <h1 className="post-detail-title" style={{ fontSize: '2.5rem', marginBottom: '10px' }}>
            {post.title}
        </h1>
        <p className="post-detail-meta-info" style={{ color: 'var(--color-text-sub)', fontSize: '0.95em' }}>
          <span style={{fontWeight: 'bold', color: 'var(--color-accent)'}}>{post.authorNickname || "알 수 없음"}</span>
          <span style={{ margin: '0 8px' }}>|</span> 
          <span>작성일: {formatDate(post.createdAt)}</span>
          <span style={{ margin: '0 8px' }}>|</span>
          <span>카테고리: {post.categoryName || "미분류"}</span>
        </p>
        <p style={{ margin: "15px 0 5px 0" }}>
          태그:{" "}
          {post.tagNames?.map((tagName) => ( 
            <span key={tagName} className="tag-badge"> 
              {tagName}
            </span>
          ))}
        </p>
      </div>

      <div
        className="post-detail-content"
        style={{ padding: "40px 0", minHeight: "300px" }}
      >
        <div
          style={{
            whiteSpace: "pre-wrap",
            color: "var(--color-text-main)",
            lineHeight: "1.7",
            fontSize: "1.1em"
          }}
        >
          {post.content}
        </div>
      </div>

      {isAuthor && (
        // 수정/삭제 버튼 그룹화
        <div className="post-action-buttons">
          <Link to={`/post/edit/${post.id}`} className="btn-secondary">
            <span role="img" aria-label="edit">✏️</span> 수정
          </Link>
          <button onClick={handleDelete} className="btn-danger">
            <span role="img" aria-label="delete">🗑️</span> 삭제
          </button>
        </div>
      )}

      <div style={{ margin: '60px 0 20px 0' }}>
        {/* 댓글 컴포넌트 추가 */}
        <Comments postId={id} /> 
      </div>
    </div>
  );
}