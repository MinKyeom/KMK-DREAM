// src/pages/Post/PostList.jsx (새 디자인 적용)

import React, { useState, useEffect } from "react";
import { fetchPosts } from "../../api/posts";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext.jsx"; 
import "../../App.css"; 

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('ko-KR', {
        year: 'numeric', month: 'long', day: 'numeric'
    });
};

export default function PostList() {
  const [posts, setPosts] = useState([]);
  const [pageInfo, setPageInfo] = useState({
    page: 0,
    totalPages: 0,
    size: 10,
  });
  const [loading, setLoading] = useState(true);
  
  // useAuth 훅을 사용하여 인증 상태 확인
  const { isAuthenticated } = useAuth(); 

  useEffect(() => {
    const loadPosts = async () => {
      setLoading(true);
      try {
        // 현재 페이지와 사이즈를 사용하여 API 호출
        const data = await fetchPosts(pageInfo.page, pageInfo.size);
        setPosts(data.content || []);
        setPageInfo((prev) => ({ ...prev, totalPages: data.totalPages }));
      } catch (error) {
        console.error("Error fetching posts:", error);
        alert("게시글 목록을 불러오는 데 실패했습니다.");
        setPosts([]); 
      } finally {
        setLoading(false);
      }
    };
    loadPosts();
  }, [pageInfo.page, pageInfo.size]);

  const handlePageChange = (newPage) => {
    if (newPage >= 0 && newPage < pageInfo.totalPages) {
      setPageInfo((prev) => ({ ...prev, page: newPage }));
    }
  };

  return (
    <div className="post-list-container">
      <h1 className="section-title" style={{ textAlign: 'left' }}>전체 포스트</h1>
      
      {/* 글쓰기 버튼 (로그인 사용자에게만 표시) */}
      {isAuthenticated && (
        <div style={{ textAlign: 'right', marginBottom: '30px' }}>
          <Link to="/write" className="btn-primary">
            새 글 작성
          </Link>
        </div>
      )}

      {loading ? (
        <p className="loading-message">목록을 불러오는 중입니다...</p>
      ) : posts.length === 0 ? (
        <p className="error-message">작성된 게시글이 없습니다.</p>
      ) : (
        <div className="post-list">
          {posts.map((post) => (
            <Link key={post.id} to={`/post/${post.id}`} className="post-list-card">
              <h2>{post.title}</h2>
              {/* 내용 요약 */}
              <p>
                {post.content.substring(0, 180)}{post.content.length > 180 ? '...' : ''}
              </p>
              {/* 메타 정보 */}
              <div className="post-list-card-meta">
                <span>작성자: <span style={{ fontWeight: 600, color: 'var(--color-accent)' }}>{post.authorNickname || "알 수 없음"}</span></span>
                <span>작성일: {formatDate(post.createdAt)}</span>
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
        <div className="pagination-controls">
          <button
            onClick={() => handlePageChange(pageInfo.page - 1)}
            disabled={pageInfo.page === 0}
            className="btn-secondary"
          >
            이전
          </button>
          <span>
            {pageInfo.page + 1} / {pageInfo.totalPages}
          </span>
          <button
            onClick={() => handlePageChange(pageInfo.page + 1)}
            disabled={pageInfo.page >= pageInfo.totalPages - 1}
            className="btn-secondary"
          >
            다음
          </button>
        </div>
      )}
    </div>
  );
}