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

        // ⭐ 수정: data.content가 null이나 undefined일 경우 안전하게 빈 배열([])로 설정
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
    // pageInfo.totalPages가 0인 경우(게시글이 없는 경우) 페이지 이동을 막음
    if (
      newPage >= 0 &&
      newPage < pageInfo.totalPages &&
      pageInfo.totalPages > 0
    ) {
      setPageInfo((prev) => ({ ...prev, page: newPage }));
    }
  };

  if (loading)
    return (
      <div
        style={{
          padding: "20px",
          textAlign: "center",
          color: "var(--color-text-sub)",
        }}
      >
        게시글 목록 로딩 중...
      </div>
    );

  return (
    <div
      className="post-list-container"
      style={{ maxWidth: "800px", margin: "40px auto", padding: "0 20px" }}
    >
      <h1 style={{ color: "var(--color-text-main)", marginBottom: "30px" }}>
        전체 게시글 목록
      </h1>

      {/* posts 상태가 초기화 시나 에러 시 항상 빈 배열([])이므로 안전하게 .length 사용 가능 */}
      {posts.length === 0 ? (
        <p style={{ color: "var(--color-text-sub)" }}>
          작성된 게시글이 없습니다.
        </p>
      ) : (
        posts.map((post) => (
          // key로 post.id를 사용하며, post.id가 없을 경우를 대비하여 Math.random()을 fallback으로 사용
          <div
            key={post?.id || Math.random()}
            className="post-list-item"
            style={{
              marginBottom: "15px",
              padding: "15px",
              border: "1px solid var(--color-border)",
              borderRadius: "8px",
              backgroundColor: "var(--color-primary)",
              textAlign: "left",
            }}
          >
            <Link
              to={`/post/${post.id}`}
              style={{
                textDecoration: "none",
                color: "var(--color-text-main)",
              }}
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
        ))
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
          {pageInfo.page + 1} / {pageInfo.totalPages || 1}{" "}
        </span>
        <button
          onClick={() => handlePageChange(pageInfo.page + 1)}
          // totalPages가 0일 때도 다음 버튼 비활성화
          disabled={
            pageInfo.page >= pageInfo.totalPages - 1 ||
            pageInfo.totalPages === 0
          }
          className="btn-secondary"
        >
          다음
        </button>
      </div>
    </div>
  );
}
