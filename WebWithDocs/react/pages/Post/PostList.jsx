// src/pages/Post/PostList.jsx

import React, { useState, useEffect } from "react";
import { fetchPosts } from "../../api/posts";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext.jsx"; 
import "../../App.css"; 

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
      {/* 글 작성 버튼: 인증된 사용자에게만 표시 */}
      <div style={{ textAlign: "right", margin: "20px 0" }}>
        {isAuthenticated && (
          <Link to="/write" className="btn-primary">
            <span role="img" aria-label="write">📝</span> 새 글 작성
          </Link>
        )}
      </div>

      <h1 className="section-title" style={{ display: 'block', textAlign: 'left', width: '100%', marginBottom: '40px' }}>
        전체 포스트 목록 ({pageInfo.totalPages > 0 ? `${pageInfo.totalPages} 페이지` : '0 페이지'})
      </h1>

      {loading ? (
        <p style={{ textAlign: 'center' }}>글 목록을 불러오는 중입니다...</p>
      ) : posts.length === 0 ? (
        <p style={{ textAlign: 'center' }}>작성된 글이 없습니다.</p>
      ) : (
        <div className="post-grid-list"> 
          {posts.map((post) => (
            <Link to={`/post/${post.id}`} key={post.id} className="post-list-card"> 
              <h3 style={{ margin: "0 0 5px 0", fontSize: "1.2em", color: "var(--color-text-main)" }}> 
                {post.title || "제목 없음"}
              </h3>
              <p className="post-list-meta"> 
                작성자: {post.authorNickname || "알 수 없음"} | 카테고리:{" "}
                <span className="tag-badge" style={{ backgroundColor: 'transparent', border: '1px solid var(--color-text-sub)'}}>
                    {post.categoryName || "미분류"}
                </span>
                <br/>
                태그:{" "}
                {post.tagNames?.map(tag => (
                    <span key={tag} className="tag-badge">{tag}</span>
                )) || "없음"}
              </p>
            </Link>
          ))}
        </div>
      )}

      {/* 페이지네이션 */}
      {pageInfo.totalPages > 1 && (
        <div
          className="pagination-controls"
          style={{ textAlign: "center", marginTop: "40px" }}
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
            {pageInfo.page + 1} / {pageInfo.totalPages}
          </span>
          <button
            onClick={() => handlePageChange(pageInfo.page + 1)}
            disabled={pageInfo.page === pageInfo.totalPages - 1}
            className="btn-secondary"
          >
            다음
          </button>
        </div>
      )}
    </div>
  );
}