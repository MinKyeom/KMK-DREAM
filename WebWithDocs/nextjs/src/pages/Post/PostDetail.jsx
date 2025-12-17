// src/pages/Post/PostDetail.jsx (전체 코드)

import React, { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { fetchPostById, deletePost } from "../../api/posts";
import { useAuth } from "../../context/AuthContext.jsx";
import Comments from "../../components/Comments.jsx";
import MarkdownRenderer from "../../components/MarkdownRenderer.jsx"; // ⭐ 추가
import "../../App.css";

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('ko-KR', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
    });
};

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

  // 글 작성자 확인
  const isAuthor = post && post.authorId === currentUserId;

  // 글 삭제 핸들러
  const handleDelete = async () => {
    if (window.confirm("정말로 이 글을 삭제하시겠습니까?")) {
      try {
        await deletePost(id);
        alert("글이 삭제되었습니다.");
        navigate("/post"); // 삭제 후 목록 페이지로 이동
      } catch (error) {
        alert(error.message || "글 삭제 실패: 권한 또는 서버 오류");
        console.error(error);
      }
    }
  };

  if (loading || !post) {
    return (
      <div className="container" style={{ textAlign: "center", padding: "100px 0" }}>
        <p className="loading-message">글 내용을 불러오는 중입니다...</p>
      </div>
    );
  }

  return (
    <div className="post-detail-container">
      {/* 1. 제목 및 메타 정보 */}
      <h1 className="post-detail-title">{post.title}</h1>
      <div className="post-meta-info" style={{ marginBottom: "30px", borderBottom: "1px solid var(--color-border)", paddingBottom: "15px" }}>
        <p className="post-meta" style={{ margin: "0" }}>
          <span style={{ fontWeight: 600, color: 'var(--color-accent)' }}>
            {post.authorNickname || "알 수 없음"}
          </span>
          <span style={{ marginLeft: "15px", color: "var(--color-text-sub)" }}>
            {formatDate(post.createdAt)}
          </span>
        </p>
        <p style={{ margin: "10px 0 0 0", fontSize: "0.95em", color: "var(--color-text-sub)" }}>
          카테고리: {" "}
          <span className="tag-badge" style={{ backgroundColor: 'var(--color-secondary)' }}>
            {post.categoryName || "미분류"}
          </span>
        </p>
      </div>

      {/* 2. 본문 내용 (마크다운 렌더링 적용) */}
      <div
        className="post-detail-content"
        style={{ padding: "40px 0", minHeight: "300px" }}
      >
        {/* ⭐ MarkdownRenderer 컴포넌트로 교체 */}
        <MarkdownRenderer content={post.content} />
      </div>

      {/* 3. 태그 리스트 */}
      <div style={{ margin: "20px 0 40px 0", borderTop: "1px solid var(--color-border)", paddingTop: "20px" }}>
        <p style={{ margin: "0", color: "var(--color-text-sub)", fontWeight: 600 }}>
          # 태그:{" "}
          {post.tagNames?.map((tagName) => (
            <span key={tagName} className="tag-badge">
              {tagName}
            </span>
          )) || "태그 없음"}
        </p>
      </div>


      {/* 4. 수정/삭제 버튼 */}
      {isAuthor && (
        <div className="post-action-buttons">
          <Link
            to={`/post/edit/${post.id}`}
            className="btn-secondary"
            style={{ minWidth: "100px" }}
          >
            수정
          </Link>
          <button
            onClick={handleDelete}
            className="btn-danger"
            style={{ minWidth: "100px" }}
          >
            삭제
          </button>
        </div>
      )}

      {/* 5. 댓글 섹션 */}
      <Comments postId={post.id} />
    </div>
  );
}