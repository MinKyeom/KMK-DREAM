// src/pages/Post/PostDetail.jsx

import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
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
        // Post ID는 URL 파라미터로 문자열 형태이므로 그대로 전달
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
        // 백엔드에서 권한이 없으면 403 Forbidden 에러 발생
        alert(
          `삭제 실패: ${
            error.message || "로그인이 필요하거나 권한이 없습니다."
          }`
        );
        console.error("Delete error:", error);
      }
    }
  };

  if (loading) return <div>게시글 상세 로딩 중...</div>;
  if (!post) return <div>게시글을 찾을 수 없습니다.</div>;

  // 로그인된 사용자가 글 작성자인지 확인
  const isAuthor = currentUserId && post.authorId === currentUserId;

  return (
    <div
      className="post-detail-page"
      style={{
        maxWidth: "800px",
        margin: "50px auto",
        padding: "30px",
        backgroundColor: "var(--color-primary)",
        border: "1px solid var(--color-border)",
        borderRadius: "8px",
      }}
    >
      <h1
        style={{
          color: "var(--color-text-main)",
          borderBottom: "1px solid var(--color-border)",
          paddingBottom: "10px",
          marginBottom: "15px",
        }}
      >
        {post.title}
      </h1>
      <p style={{ color: "var(--color-text-sub)", fontSize: "0.9em" }}>
        작성자 ID: {post.author} | 작성일:{" "}
        {new Date(post.createdAt).toLocaleDateString()}
      </p>
      <p style={{ marginTop: "10px" }}>
        카테고리:{" "}
        <span style={{ fontWeight: "bold", color: "var(--color-accent)" }}>
          {post.category?.name || "미분류"}
        </span>
      </p>
      <p style={{ marginBottom: "20px" }}>
        태그:{" "}
        {post.tags?.map((tag) => (
          // ✨ 이전 오류 수정: 불필요한 주석/문자 없이 순수 JSX 요소만 반환
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
          <Link to={`/edit/${post.id}`}>
            <button className="btn-secondary" style={{ marginRight: "10px" }}>
              수정
            </button>
          </Link>
          <button onClick={handleDelete} className="btn-delete">
            삭제
          </button>
        </div>
      )}

      <div
        style={{
          marginTop: "30px",
          borderTop: "1px solid var(--color-border)",
          paddingTop: "20px",
        }}
      >
        <Link to="/">
          <button className="btn-primary">목록으로</button>
        </Link>
      </div>
    </div>
  );
}
