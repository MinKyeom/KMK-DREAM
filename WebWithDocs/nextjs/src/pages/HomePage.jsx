// src/pages/HomePage.jsx (새 디자인 적용)

import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { fetchPosts } from "../api/posts";
import "../App.css"; 
import "./HomePage.css"; 

// --- 서브 컴포넌트: 포스트 목록 카드 (Homepage용) --
const PostCard = ({ post }) => (
    <Link to={`/post/${post.id}`} className="post-card">
        <h3>{post.title || "제목 없음"}</h3>
        <p>
            {/* 내용 요약 */}
            {post.content.substring(0, 120)}{post.content.length > 120 ? '...' : ''} 
        </p>
        <div className="post-meta">
            <span style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
                {/* 닉네임 표시 */}
                <span style={{ fontWeight: 600, color: 'var(--color-text-main)' }}>
                    {post.authorNickname || "작성자 알 수 없음"}
                </span>
                <span style={{ fontSize: '0.9em', color: 'var(--color-text-sub)', marginTop: '4px' }}>
                    {new Date(post.createdAt).toLocaleDateString('ko-KR', { year: 'numeric', month: 'long', day: 'numeric' })}
                </span>
            </span>
            <span className="tag-badge">
                {post.categoryName || "미분류"}
            </span>
        </div>
    </Link>
);

export default function HomePage() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    // 최신 글 3개만 불러옵니다.
    fetchPosts(0, 3) 
      .then(data => {
        setPosts(data.content || []);
      })
      .catch(error => {
        console.error("Error fetching featured posts:", error);
        setPosts([]); 
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="homepage-container">
      {/* 1. 히어로 섹션 (감성적인 타이포그래피 강조) */}
      <section className="hero-section">
        <h2 className="hero-title">
            당신의 개발 이야기,
            <br/>
            감성적으로 기록하세요.
        </h2>
        <p className="hero-subtitle">
            코드와 영감을 공유하는 공간. 다크/라이트 모드를 지원하는<br/>
            미니멀하고 깔끔한 개발 블로그 플랫폼입니다.
        </p>
        <Link to="/post" className="btn-primary start-button">
            개발 이야기 시작하기
        </Link>
      </section>

      {/* 2. 최근 포스트 섹션 (블로그 정보 찾아가기) */}
      <section className="featured-posts-section">
        <h2 className="section-title">최신 포스트 📚</h2>
        {loading ? (
          <p className="loading-message">포스트를 불러오는 중입니다...</p>
        ) : posts.length > 0 ? (
          <div className="post-grid">
            {posts.map((post) => (
              <PostCard key={post.id} post={post} />
            ))}
          </div>
        ) : (
          <p className="error-message">아직 작성된 글이 없습니다. 새로운 글을 작성해 보세요!</p>
        )}
        <div style={{ textAlign: 'center', marginTop: '30px' }}>
             <Link to="/post" className="btn-secondary">
                전체 포스트 목록으로 이동 →
             </Link>
        </div>
      </section>
      
      {/* 3. 주요 카테고리 섹션 */}
      <section className="category-section">
        <h2 className="section-title">주요 기술 스택</h2>
        <div className="category-links">
          {/* 실제 데이터가 없으므로 임시 링크를 사용합니다. */
          /* 실제 카테고리 데이터를 받으면 교체 필요 */}
          <Link to="/post?category=React" className="category-link">⚛️ React</Link>
          <Link to="/post?category=Spring" className="category-link">☕ Spring Boot</Link>
          <Link to="/post?category=AI" className="category-link">🤖 AI / LLM</Link>
          <Link to="/post?category=DevOps" className="category-link">☁️ DevOps</Link>
          <Link to="/post?category=Database" className="category-link">💾 Database</Link>
        </div>
      </section>
    </div>
  );
}