// src/pages/Post/PostDetail.jsx

import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
// posts.js에서 fetchPostById, deletePost를 가져옴
import { fetchPostById, deletePost } from "../../api/posts";
import { getAuthUser } from "../../api/auth";

export default function PostDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(true);

  // 로그인된 사용자 ID를 가져옴
  const { id: currentUserId } = getAuthUser();

  useEffect(() => {
    const loadPost = async () => {
      setLoading(true);
      try {
        const data = await fetchPostById(id);
        setPost(data);
      } catch (error) {
        console.error("Error fetching post:", error);
        alert("글을 찾을 수 없거나 불러오지 못했습니다.");
        navigate("/");
      } finally {
        setLoading(false);
      }
    };
    loadPost();
  }, [id, navigate]);

  const handleDelete = async () => {
    if (window.confirm("정말로 이 글을 삭제하시겠습니까?")) {
      try {
        await deletePost(id);
        alert("글이 성공적으로 삭제되었습니다.");
        navigate("/");
      } catch (error) {
        const message =
          error.response?.data?.error ||
          "삭제 권한이 없거나 서버 오류가 발생했습니다.";
        alert(message);
        console.error("Error deleting post:", error);
      }
    }
  };

  if (loading) {
    return <div style={{ textAlign: "center", padding: "50px" }}>로딩 중...</div>;
  }

  if (!post) {
    return (
      <div style={{ textAlign: "center", padding: "50px" }}>
        게시글을 찾을 수 없습니다.
      </div>
    );
  }

  // 로그인된 사용자가 게시글 작성자와 일치하는지 확인
  const isAuthor = post.author === currentUserId;

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "20px auto",
        padding: "30px",
        backgroundColor: "var(--color-primary)",
        borderRadius: "8px",
        boxShadow: "0 2px 10px var(--color-shadow)",
        textAlign: "left",
      }}
    >
      <h1
        style={{
          color: "var(--color-text-main)",
          borderBottom: "2px solid var(--color-accent)",
          paddingBottom: "10px",
          marginBottom: "15px",
        }}
      >
        {post.title}
      </h1>
      <p className="post-meta-info">
        작성자 ID:{" "}
        <span style={{ fontWeight: "bold" }}>
          {post.author || "알 수 없음"}
        </span>{" "}
        | 작성일: {new Date(post.createdAt).toLocaleDateString()}
      </p>
      <p style={{ marginBottom: "5px" }}>
        카테고리:{" "}
        <span style={{ color: "var(--color-accent)" }}>
          {post.category?.name || "미분류"}
        </span>
      </p>
      <p style={{ marginBottom: "20px" }}>
        태그:{" "}
        {post.tags?.map((tag) => (
          <span key={tag.id} className="tag-badge">
            {tag.name}
          </span>
        ))}
      </p>

      <div
        className="post-detail-content"
        style={{ borderTop: "1px solid var(--color-border)" }}
      >
        {/* 텍스트 줄바꿈을 위해 whiteSpace 스타일 적용 */}
        <div
          style={{
            whiteSpace: "pre-wrap",
            padding: "20px 0",
            minHeight: "100px",
            color: "var(--color-text-main)",
          }}
        >
          {post.content}
        </div>
      </div>

      {isAuthor && (
        <div style={{ marginTop: "30px", textAlign: "right" }}>
          <Link to={`/post/edit/${post.id}`}>
            <button className="btn-secondary">수정</button>
          </Link>
          <button onClick={handleDelete} className="btn-delete">
            삭제
          </button>
        </div>
      )}
      <div style={{ marginTop: "20px", textAlign: "left" }}>
        <Link to="/">
          <button className="btn-secondary">목록으로</button>
        </Link>
      </div>
    </div>
  );
}