// src/pages/Post/WritePost.jsx (새 디자인 적용)

import React, { useState, useEffect, useMemo } from "react"; // ⭐ useMemo 추가
import { useNavigate, useParams, Link } from "react-router-dom";
import { createPost, fetchPostById, updatePost } from "../../api/posts";
import { useAuth } from "../../context/AuthContext.jsx";
import "../../App.css";

// ====================================================================
// ⭐ [New] Marked.js & DOMPurify 임포트 (설치 필요)
// marked: Markdown을 HTML로 파싱
// DOMPurify: XSS 공격을 막기 위한 HTML Sanitization
import { marked } from 'marked';
import DOMPurify from 'dompurify';

// Marked.js 옵션 설정 (줄바꿈 자동 인식 활성화)
marked.setOptions({
    breaks: true,
});

// Markdown을 안전한 HTML로 변환하는 헬퍼 함수
const renderMarkdown = (markdown) => {
    if (!markdown) return "";
    const rawMarkup = marked.parse(markdown);
    return DOMPurify.sanitize(rawMarkup);
};
// ====================================================================


export default function WritePost({ isEdit = false }) {
  const { id } = useParams();
  const navigate = useNavigate();
  // useAuth 훅 사용
  const { isAuthenticated, id: currentUserId } = useAuth();
  
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState("");
  const [loading, setLoading] = useState(false);
  
  const pageTitle = isEdit ? "글 수정" : "새 글 작성";

  // ⭐ [New] content 상태가 변경될 때마다 미리보기 HTML을 계산 (useMemo로 최적화)
  const previewHtml = useMemo(() => {
    return renderMarkdown(content);
  }, [content]);


  // 인증되지 않은 사용자 접근 방지
  useEffect(() => {
    if (!isAuthenticated && !loading) {
        alert("글 작성/수정을 위해서는 로그인이 필요합니다.");
        navigate("/signin");
    }
  }, [isAuthenticated, navigate, loading]);

  useEffect(() => {
    // ... (기존 글 수정 로직 유지)
    if (isEdit && id) {
      setLoading(true);
      fetchPostById(id)
        .then((post) => {
          // 작성자 권한 확인 (프론트엔드 방어)
          if (post.authorId !== currentUserId) {
            alert("수정 권한이 없습니다.");
            navigate(`/post/${id}`);
            return;
          }
          setTitle(post.title);
          setContent(post.content);
          setCategory(post.categoryName || "");
          setTags(post.tagNames ? post.tagNames.join(", ") : "");
        })
        .catch((error) => {
          console.error("Error fetching post:", error);
          alert("글을 불러오지 못했습니다.");
          navigate("/post");
        })
        .finally(() => setLoading(false));
    }
  }, [isEdit, id, navigate, currentUserId]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    if (loading) return;

    setLoading(true);
    const postData = {
      title,
      content,
      category,
      tags: tags.split(",").map(tag => tag.trim()).filter(tag => tag.length > 0)
    };

    try {
      let postId;
      if (isEdit) {
        // 글 수정
        const updatedPost = await updatePost(id, postData);
        postId = updatedPost.id;
        alert("글이 성공적으로 수정되었습니다.");
      } else {
        // 새 글 작성
        const newPost = await createPost(postData);
        postId = newPost.id;
        alert("새 글이 성공적으로 작성되었습니다.");
      }
      navigate(`/post/${postId}`);
    } catch (error) {
      console.error("Post submission error:", error);
      alert(error.response?.data?.error || "글 저장에 실패했습니다.");
    } finally {
      setLoading(false);
    }
  };

  if (loading && isEdit) {
    return <div className="loading-message">글을 불러오는 중입니다...</div>;
  }
  
  // 로그인 안 된 상태 처리
  if (!isAuthenticated && !isEdit) {
      return null;
  }

  return (
    <div className="write-post-page">
      <h1 className="page-title">{pageTitle}</h1>

      <form className="post-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          className="post-form-input"
        />
        
        {/* ⭐ [New] 에디터와 미리보기 영역을 위한 컨테이너 */}
        <div className="markdown-editor-container">
          
          {/* A. 입력 필드 (Markdown Editor) */}
          <div className="editor-pane">
             <label className="editor-label">Markdown Editor</label>
             <textarea
                placeholder="내용 (Markdown 지원)"
                value={content}
                onChange={(e) => setContent(e.target.value)}
                rows="20" // 미리보기를 위해 행 높이 증가
                required
                className="post-form-textarea editor-input" // 새로운 클래스 적용
             />
          </div>

          {/* B. 미리보기 필드 (HTML Preview) */}
          <div className="editor-pane preview-pane">
            <label className="editor-label">Preview</label>
            <div
              className="post-form-preview"
              // ⭐ 중요: 파싱된 HTML을 삽입 (dangerouslySetInnerHTML 사용)
              dangerouslySetInnerHTML={{ __html: previewHtml }}
            />
          </div>
        </div>
        {/* End of markdown-editor-container */}

        <input
          type="text"
          placeholder="카테고리 (예: React, JS, AI)"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          required
          className="post-form-input"
        />
        <input
          type="text"
          placeholder="태그 (쉼표로 구분하여 입력: 예. tag1, tag2)"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          className="post-form-input"
        />
        
        <div style={{ marginTop: "20px", textAlign: "right", display: 'flex', gap: '15px', justifyContent: 'flex-end' }}>
          {isEdit && (
             <Link to={`/post/${id}`} className="btn-secondary">
                취소
             </Link>
          )}
          <button
            type="submit"
            className="btn-primary"
            disabled={loading}
          >
            {loading 
              ? "저장 중..." 
              : isEdit 
                ? <><span role="img" aria-label="save">📝</span> 수정 완료</>
                : <><span role="img" aria-label="write">💾</span> 글 작성</>
            }
          </button>
        </div>
      </form>
    </div>
  );
}