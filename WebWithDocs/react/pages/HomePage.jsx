// src/pages/HomePage.jsx (새 파일)

import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useTheme } from "../context/ThemeContext.jsx";
import { fetchPosts } from "../api/posts";
import "./HomePage.css"; 

// --- 서브 컴포넌트: 테마 토글 버튼 (메인 섹션 강조용) ---
const ThemeToggle = () => {
  const { isDarkMode, toggleTheme } = useTheme();
  return (
    <button 
      onClick={toggleTheme} 
      className="theme-toggle-button"
      style={{ padding: '8px 15px', borderRadius: '20px', fontSize: '0.9em' }}
    >
      {isDarkMode ? "🌞 라이트 모드로 보기" : "🌙 다크 모드로 보기"}
    </button>
  );
};

// --- 서브 컴포넌트: 포스트 목록 카드 ---
const PostCard = ({ post }) => (
    <Link to={`/post/${post.id}`} className="post-card">
        <h3>{post.title || "제목 없음"}</h3>
        <p>
            {post.content.substring(0, 120)}...
        </p>
        <div className="post-meta">
            <span>
                {new Date(post.createdAt).toLocaleDateString()}
            </span>
            <span className="category-tag">
                {post.category?.name || "미분류"}
            </span>
        </div>
    </Link>
);

// --- 메인 컴포넌트: HomePage ---
export default function HomePage() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // 최근 3개의 포스트를 불러옵니다.
  useEffect(() => {
    const loadRecentPosts = async () => {
      setLoading(true);
      try {
        // API에서 첫 페이지의 3개 포스트를 요청
        const data = await fetchPosts(0, 3); 
        setPosts(data.content || []);
      } catch (error) {
        console.error("Error fetching recent posts:", error);
        setPosts([]);
      } finally {
        setLoading(false);
      }
    };
    loadRecentPosts();
  }, []);

  return (
    <div className="homepage-container">
      {/* 1. 히어로 섹션 */}
      <section className="hero-section">
        <h1 className="hero-title">안녕하세요, **[Your Name]** 입니다 👋</h1>
        <p className="hero-subtitle">
          React, Spring Boot, AI/ML 기술을 중심으로 깊이 있는 지식과 경험을 공유합니다.
        </p>
        <ThemeToggle /> {/* 깔끔한 디자인을 위해 토글 버튼을 중앙에 배치 */}
      </section>

      {/* 2. 최근 포스트 섹션 (블로그 정보 찾아가기) */}
      <section className="featured-posts-section">
        <h2 className="section-title">최신 포스트 📚</h2>
        {loading ? (
          <p>포스트를 불러오는 중입니다...</p>
        ) : posts.length > 0 ? (
          <div className="post-grid">
            {posts.map((post) => (
              <PostCard key={post.id} post={post} />
            ))}
          </div>
        ) : (
          <p>아직 작성된 글이 없습니다. 새로운 글을 작성해 보세요!</p>
        )}
        <div style={{ textAlign: 'center', marginTop: '30px' }}>
             <Link to="/post" className="btn-primary start-button">
                전체 포스트 목록으로 이동
             </Link>
        </div>
      </section>
      
      {/* 3. 주요 카테고리 섹션 */}
      <section className="category-section">
        <h2 className="section-title">주요 기술 스택</h2>
        <div className="category-links">
          <Link to="/post?category=React" className="category-link">React</Link>
          <Link to="/post?category=SpringBoot" className="category-link">Spring Boot</Link>
          <Link to="/post?category=AI" className="category-link">AI / ML</Link>
          <Link to="/post?category=Database" className="category-link">Database</Link>
          <Link to="/post?category=Cloud" className="category-link">Cloud / DevOps</Link>
        </div>
      </section>
    </div>
  );
}