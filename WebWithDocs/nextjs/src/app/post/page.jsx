// app/post/page.jsx (Server Component)

import Link from "next/link";
import { fetchPosts } from "../../services/api/posts"; 
import PostCard from "../../components/Post/PostCard"; 
import "../../styles/globals.css"; 
import { notFound } from "next/navigation"; 

// 🌟 수정: 한국어 우선 SEO 메타데이터
export const metadata = {
  // 🌟 UI 텍스트 한국어 우선: 전체 포스트 목록
  title: "전체 포스트 목록",
  description:
    "MinKowski 개발 블로그의 모든 포스트 목록입니다. 관심 있는 글을 찾아보세요.",
  keywords: ["전체 포스트", "개발 아티클", "기술 아카이브"], 
  alternates: {
    canonical: "https://your-blog-url.com/post", // 목록 페이지 정규 URL
  },
};

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
  // 🌟 수정: 한국어 포맷으로 변경
  return new Date(dateString).toLocaleDateString("ko-KR", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

// 동적 경로 세그먼트 (page, size)를 받아 데이터를 가져옵니다.
async function getPosts(page, size) {
  try {
    const data = await fetchPosts(page, size);
    return data; // Page<Post> 객체 반환
  } catch (error) {
    console.error("Failed to fetch posts on server:", error);
    // 404를 반환하는 대신 빈 목록을 반환하거나, 필요에 따라 notFound()를 호출할 수 있습니다.
    return { content: [], totalPages: 0, totalElements: 0, page: 0 };
  }
}

// Next.js SearchParams를 이용한 페이지네이션 지원
export default async function PostListPage({ searchParams }) {
  // URL에서 'page' 쿼리 파라미터를 가져오거나 기본값 0 사용
  const currentPage = parseInt(searchParams.page) || 0;
  // 페이지 크기는 10으로 고정
  const pageSize = 10; 

  const postData = await getPosts(currentPage, pageSize);
  const posts = postData.content;
  const pageInfo = postData; // pageInfo는 전체 응답 객체

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px 0" }}>
      {/* 🌟 UI 텍스트 한국어 우선: 전체 포스트 목록 */}
      <h1
        style={{
          fontSize: "2.5rem",
          fontWeight: 700,
          marginBottom: "40px",
          textAlign: "center",
          color: "var(--color-text-main)",
        }}
      >
        전체 포스트 목록
      </h1>

      {/* 포스트 목록 */}
      {posts && posts.length > 0 ? (
        <div
          className="post-list"
          style={{
            display: "grid",
            gridTemplateColumns: "1fr", // 단일 컬럼
            gap: "30px",
          }}
        >
          {posts.map((post) => (
            <PostCard key={post.id} post={post} />
          ))}
        </div>
      ) : (
        <div style={{ textAlign: "center", padding: "80px 0" }}>
          {/* 🌟 UI 텍스트 한국어 우선: 포스트가 없습니다. */}
          <p style={{ color: "var(--color-text-sub)", fontSize: "1.2em" }}>
            현재 페이지에 포스트가 없습니다.
          </p>
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
              // 첫 페이지에서는 비활성화 처리
              pointerEvents: currentPage === 0 ? "none" : "auto",
              opacity: currentPage === 0 ? 0.5 : 1,
            }}
          >
            {/* 🌟 UI 텍스트 한국어 우선: 이전 */}
            이전
          </Link>
          {/* 현재 페이지/전체 페이지 */}
          <span>
            {/* 🌟 UI 텍스트 한국어 우선: {pageInfo.page + 1} / {pageInfo.totalPages} */}
            {pageInfo.page + 1} / {pageInfo.totalPages} 페이지
          </span>
          {/* 다음 페이지 버튼 */}
          <Link
            href={`/post?page=${currentPage + 1}`}
            className="btn-secondary"
            style={{
              // 마지막 페이지에서는 비활성화 처리
              pointerEvents:
                currentPage === pageInfo.totalPages - 1 ? "none" : "auto",
              opacity: currentPage === pageInfo.totalPages - 1 ? 0.5 : 1,
            }}
          >
            {/* 🌟 UI 텍스트 한국어 우선: 다음 */}
            다음
          </Link>
        </div>
      )}
    </div>
  );
}