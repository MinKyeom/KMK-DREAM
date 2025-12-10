// src/pages/HomePage.jsx

import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { fetchPosts } from "../api/posts";
import "../App.css"; // 공통 버튼 스타일 사용
import "./HomePage.css"; 

// --- 서브 컴포넌트: 포스트 목록 카드 ---
const PostCard = ({ post }) => (
    <Link to={`/post/${post.id}`} className="post-card">
        <h3>{post.title || "제목 없음"}</h3>
        <p>
            {/* 내용 요약 */}
            {post.content.substring(0, 120)}{post.content.length > 120 ? '...' : ''} 
        </p>
        <div className="post-meta">
            <span>
                {/* 닉네임 표시 */}
                {post.authorNickname || "작성자 알 수 없음"} | {new Date(post.createdAt).toLocaleDateString()}
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
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="homepage-container">
      {/* 1. 히어로 섹션 */}
      <section className="hero-section">
        <h1 className="hero-title">나만의 개발 이야기를 기록하는 공간</h1>
        <p className="hero-subtitle">
          React, Spring Boot, AI 등 다양한 기술 스택을 탐험하고 기록하세요.
          <br />
          지식의 공유는 성장의 지름길입니다.
        </p>
        
        {/* 시작하기 버튼 클래스 사용 */}
        <Link to="/post" className="btn-primary start-button">
            개발 이야기 시작하기
        </Link>
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
             <Link to="/post" className="btn-secondary">
                전체 포스트 목록으로 이동
             </Link>
        </div>
      </section>
      
      {/* 3. 주요 카테고리 섹션 */}
      <section className="category-section">
        <h2 className="section-title">주요 기술 스택</h2>
        <div className="category-links">
          {/* 실제 데이터가 없으므로 임시 링크를 사용합니다. */}
          <Link to="/post?category=React" className="category-link">⚛️ React</Link>
          <Link to="/post?category=Spring" className="category-link">☕ Spring Boot</Link>
          <Link to="/post?category=AI" className="category-link">🤖 Artificial Intelligence</Link>
          <Link to="/post?category=Database" className="category-link">🗄️ Database</Link>
          <Link to="/post?category=DevOps" className="category-link">☁️ DevOps</Link>
        </div>
      </section>
    </div>
  );
}