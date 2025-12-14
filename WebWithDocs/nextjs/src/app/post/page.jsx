// app/post/page.jsx (Server Component)

import Link from "next/link";
import { fetchPosts } from "../../services/api/posts"; // API 경로 수정
import PostCard from "../../components/Post/PostCard"; // PostCard 재사용 (Server Component)
import "../../styles/globals.css"; // 공통 스타일 사용

// SEO 메타데이터
export const metadata = {
  title: "전체 포스트 목록",
  description:
    "Dev Blog의 모든 개발 포스트 목록입니다. 원하는 글을 찾아보세요.",
  keywords: ["전체 포스트", "개발 글 모음", "기술 아카이브"],
  alternates: {
    canonical: "https://your-blog-url.com/post", // 목록 페이지 정규 URL
  },
};

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString("ko-KR", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

// 포스트 목록 데이터를 서버에서 미리 가져옵니다.
async function getPosts(page = 0, size = 10) {
  try {
    const data = await fetchPosts(page, size);
    return data; // { content: [], totalPages: 1 }
  } catch (error) {
    console.error("Failed to fetch posts on server:", error);
    return { content: [], totalPages: 0, number: 0 };
  }
}

// PostList Component
export default async function PostListPage({ searchParams }) {
  // URL에서 현재 페이지 번호를 가져옵니다.
  // Next.js의 searchParams는 문자열이므로 숫자로 변환합니다.
  const currentPage = parseInt(searchParams.page) || 0;
  const size = 10; // 페이지당 표시 개수

  const postData = await getPosts(currentPage, size);
  const posts = postData.content;
  const pageInfo = {
    totalPages: postData.totalPages || 0,
    page: postData.number || 0,
  };

  return (
    <div className="homepage-container">
      <h1
        className="section-title"
        style={{ marginTop: "30px", marginBottom: "40px", fontSize: "2.5rem" }}
      >
        전체 포스트 ({postData.totalElements || 0}개)
      </h1>

      {posts.length === 0 ? (
        <p className="no-posts">아직 작성된 포스트가 없습니다.</p>
      ) : (
        <div
          className="post-list"
          style={{
            gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
          }}
        >
          {/* PostCard 재사용 대신 인라인으로 렌더링 (Server Component의 장점 활용) */}
          {posts.map((post) => (
            <Link key={post.id} href={`/post/${post.id}`} className="post-card">
              <h3>{post.title || "제목 없음"}</h3>
              <p>
                {/* 내용 요약 */}
                {post.content.substring(0, 120)}
                {post.content.length > 120 ? "..." : ""}
              </p>
              <div className="post-meta">
                <span
                  style={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "flex-start",
                  }}
                >
                  {/* 닉네임 표시 */}
                  <span
                    style={{ fontWeight: 600, color: "var(--color-text-main)" }}
                  >
                    {post.authorNickname || "작성자 알 수 없음"}
                  </span>
                  <span
                    style={{
                      fontSize: "0.9em",
                      color: "var(--color-text-sub)",
                      marginTop: "4px",
                    }}
                  >
                    {formatDate(post.createdAt)}
                  </span>
                </span>
                {/* 카테고리 배지 */}
                <span className="tag-badge">
                  {post.categoryName || "미분류"}
                </span>
              </div>
            </Link>
          ))}
        </div>
      )}

      {/* 페이지네이션 */}
      {pageInfo.totalPages > 1 && (
        <div
          className="pagination-controls"
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "20px",
            marginTop: "40px",
          }}
        >
          {/* 이전 페이지 버튼 */}
          <Link
            href={`/post?page=${currentPage - 1}`}
            className="btn-secondary"
            style={{
              pointerEvents: currentPage === 0 ? "none" : "auto",
              opacity: currentPage === 0 ? 0.5 : 1,
            }}
          >
            이전
          </Link>
          {/* 현재 페이지/전체 페이지 */}
          <span>
            {pageInfo.page + 1} / {pageInfo.totalPages}
          </span>
          {/* 다음 페이지 버튼 */}
          <Link
            href={`/post?page=${currentPage + 1}`}
            className="btn-secondary"
            style={{
              pointerEvents:
                currentPage === pageInfo.totalPages - 1 ? "none" : "auto",
              opacity: currentPage === pageInfo.totalPages - 1 ? 0.5 : 1,
            }}
          >
            다음
          </Link>
        </div>
      )}
      <div style={{ height: "50px" }}>{/* 공간 확보 */}</div>
    </div>
  );
}
