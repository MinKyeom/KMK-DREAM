// src/pages/Post/PostList.jsx

import React, { useState, useEffect } from "react";
import { fetchPosts } from "../../api/posts";
import { Link } from "react-router-dom";

export default function PostList() {
  const [posts, setPosts] = useState([]);
  const [pageInfo, setPageInfo] = useState({
    page: 0,
    totalPages: 0,
    size: 10,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadPosts = async () => {
      setLoading(true);
      try {
        const data = await fetchPosts(pageInfo.page, pageInfo.size);
        setPosts(data.content || []);
        setPageInfo((prev) => ({ ...prev, totalPages: data.totalPages }));
      } catch (error) {
        console.error("Error fetching posts:", error);
        alert("게시글 목록을 불러오는 데 실패했습니다.");
        setPosts([]); // 에러 발생 시 빈 배열로 설정하여 렌더링 오류 방지
      } finally {
        setLoading(false);
      }
    };
    loadPosts();
  }, [pageInfo.page, pageInfo.size]);

  const handlePageChange = (newPage) => {
    if (
      newPage >= 0 &&
      newPage < pageInfo.totalPages &&
      pageInfo.totalPages > 0
    ) {
      setPageInfo((prev) => ({ ...prev, page: newPage }));
    }
  };

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px 0" }}>
      <h2
        style={{
          color: "var(--color-text-main)",
          textAlign: "left",
          marginBottom: "20px",
        }}
      >
        전체 게시글 목록
      </h2>

      {loading && <p style={{ color: "var(--color-text-sub)" }}>로딩 중...</p>}
      {!loading && posts.length === 0 && (
        <p style={{ color: "var(--color-text-sub)" }}>게시글이 없습니다.</p>
      )}

      {posts.length > 0 && (
        <div className="post-list">
          {posts.map((post) => (
            <div
              key={post.id}
              className="post-item"
              style={{
                textAlign: "left",
                padding: "15px",
                borderBottom: "1px solid var(--color-border)",
                backgroundColor: "var(--color-primary)",
                borderRadius: "4px",
                marginBottom: "10px",
              }}
            >
              <Link
                to={`/post/${post.id}`}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <h3 style={{ margin: "0 0 5px 0", fontSize: "1.2em" }}>
                  {post.title || "제목 없음"}
                </h3>
              </Link>
              <p
                style={{
                  margin: 0,
                  fontSize: "0.9em",
                  color: "var(--color-text-sub)",
                }}
              >
                작성자 ID: {post.author || "알 수 없음"} | 카테고리:{" "}
                {post.category?.name || "미분류"} | 태그:{" "}
                {post.tags?.map((tag) => tag.name).join(", ") || "없음"}
              </p>
            </div>
          ))}
        </div>
      )}

      {/* 페이지네이션 */}
      <div
        className="pagination-controls"
        style={{ textAlign: "center", marginTop: "30px" }}
      >
        <button
          onClick={() => handlePageChange(pageInfo.page - 1)}
          disabled={pageInfo.page === 0}
          className="btn-secondary"
        >
          이전
        </button>
        <span
          style={{
            margin: "0 15px",
            fontWeight: "bold",
            color: "var(--color-text-main)",
          }}
        >
          {pageInfo.page + 1} / {pageInfo.totalPages || 1}
        </span>
        <button
          onClick={() => handlePageChange(pageInfo.page + 1)}
          disabled={pageInfo.page >= pageInfo.totalPages - 1}
          className="btn-secondary"
        >
          다음
        </button>
      </div>
    </div>
  );
}
