// app/page.jsx (Server Component)

import { fetchPosts } from "../services/api/posts"; // API 경로 수정
import PostCard from "../components/Post/PostCard"; // PostCard 재사용 (Server Component)
import "../styles/globals.css"; // 공통 스타일 사용
import "../styles/HomePage.css"; // 홈 페이지 스타일 임포트
import Link from "next/link"; // Next.js Link 컴포넌트

// SEO 메타데이터 개선
export const metadata = {
  title: "홈", // layout.jsx의 템플릿에 따라 '홈 | Dev Blog'로 표시됨
  description:
    "Dev Blog에 오신 것을 환영합니다! 최신 개발 트렌드와 기술 스택에 대한 깊이 있는 글을 만나보세요.",
  keywords: ["최신 트렌드", "기술 스택", "IT", "개발 블로그"],
  alternates: {
    canonical: "https://your-blog-url.com/",
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

// 포스트 목록 데이터를 서버에서 미리 가져옵니다. (최신 6개만)
async function getRecentPosts() {
  try {
    // 홈에서는 최신 글 6개만 가져오도록 page=0, size=6으로 설정
    const data = await fetchPosts(0, 6);
    return data.content || [];
  } catch (error) {
    console.error("Failed to fetch posts on server for homepage:", error);
    return [];
  }
}

// HomePage Component
export default async function HomePage() {
  const recentPosts = await getRecentPosts();

  return (
    <div className="homepage-container">
      {/* 1. 히어로 섹션 */}
      <section className="hero-section">
        <h1 className="hero-title">Dev Blog</h1>
        <p className="hero-subtitle">
          개발자를 위한 깊이 있는 지식과 인사이트를 공유합니다.
        </p>
        <Link
          href="/post"
          className="btn-primary"
          style={{ marginTop: "20px", fontSize: "1.1em" }}
        >
          전체 포스트 보기 &rarr;
        </Link>
      </section>

      {/* 2. 최신 포스트 섹션 */}
      <section className="latest-posts-section">
        <h2 className="section-title">✨ 최신 포스트</h2>

        {recentPosts.length > 0 ? (
          <div className="post-list">
            {recentPosts.map((post) => (
              <PostCard key={post.id} post={post} />
            ))}
          </div>
        ) : (
          <p className="no-posts">아직 작성된 포스트가 없습니다.</p>
        )}
      </section>

      {/* 3. 카테고리/태그 섹션 (예시) */}
      <section className="category-section">
        <h2 className="section-title">📚 주요 카테고리</h2>
        <div className="category-links">
          {/* 실제 데이터 기반으로 변경 필요 */}
          <Link href="/post/category/frontend" className="category-link">
            Frontend (12)
          </Link>
          <Link href="/post/category/backend" className="category-link">
            Backend (25)
          </Link>
          <Link href="/post/category/devops" className="category-link">
            DevOps (5)
          </Link>
          <Link href="/post/category/ai" className="category-link">
            AI/ML (8)
          </Link>
        </div>
      </section>

      <div style={{ height: "50px" }}>{/* 공간 확보 */}</div>
    </div>
  );
}
