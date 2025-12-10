// src/pages/Post/WritePost.jsx

import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { createPost, fetchPostById, updatePost } from "../../api/posts";
import { useAuth } from "../../context/AuthContext.jsx"; 
import "../../App.css"; 

export default function WritePost({ isEdit = false }) {
  const { id } = useParams(); 
  const navigate = useNavigate();
  // useAuth 훅 사용
  const { isAuthenticated } = useAuth();

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState(""); 
  const [loading, setLoading] = useState(false);
  
  const pageTitle = isEdit ? "글 수정" : "새 글 작성";

  // 인증되지 않은 사용자 접근 방지
  useEffect(() => {
    // isEdit 상태에 따라 인증 상태만 체크하고 로딩은 별도 관리
    if (!isAuthenticated && !loading) { 
        alert("글 작성/수정을 위해서는 로그인이 필요합니다.");
        navigate("/signin");
    }
  }, [isAuthenticated, navigate, loading]);

  useEffect(() => {
    if (isEdit && id) {
      setLoading(true);
      fetchPostById(id)
        .then((post) => {
          setTitle(post.title);
          setContent(post.content);
          // PostResponse에서 categoryName, tagNames 필드를 사용하도록 수정
          setCategory(post.categoryName || "");
          setTags(post.tagNames?.join(", ") || "");
        })
        .catch((error) => {
          console.error("Error fetching post for edit:", error);
          alert("수정할 글을 불러오는 데 실패했습니다.");
          navigate("/post");
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, [isEdit, id, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isAuthenticated) {
      alert("로그인이 필요합니다.");
      return;
    }

    setLoading(true);
    
    // 태그 문자열을 배열로 변환
    const tagList = tags.split(',').map(tag => tag.trim()).filter(tag => tag.length > 0);

    const postRequestData = {
      title,
      content,
      categoryName: category, // 백엔드는 categoryName 필드를 사용
      tagNames: tagList, // 백엔드는 tagNames 필드를 사용
    };

    try {
      let result;
      if (isEdit) {
        // 글 수정
        result = await updatePost(id, postRequestData);
        alert("글이 성공적으로 수정되었습니다.");
      } else {
        // 새 글 작성
        result = await createPost(postRequestData);
        alert("글이 성공적으로 작성되었습니다.");
      }
      // 상세 페이지로 이동
      navigate(`/post/${result.id}`); 
    } catch (error) {
      const errorMessage = error.response?.data?.error || "글 저장에 실패했습니다.";
      console.error("Error saving post:", error);
      alert(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  if (!isAuthenticated || loading && isEdit) {
    return <div style={{padding: '40px', textAlign: 'center'}}>
      {loading ? "글을 불러오는 중..." : "인증 확인 중..."}
    </div>;
  }
  
  return (
    <div className="post-write-container">
      <h1 className="post-form-title">{pageTitle}</h1>
      <form className="post-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          className="post-form-input" 
        />
        <textarea
          placeholder="내용 (Markdown 지원)"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="15"
          required
          className="post-form-textarea" 
        />
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
          placeholder="태그 (쉼표로 구분하여 입력)"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          className="post-form-input" 
        />
        
        <div style={{ marginTop: "20px", textAlign: "right" }}>
          <button
            type="submit"
            className="btn-primary"
            disabled={loading}
          >
            {loading 
              ? "저장 중..." 
              : isEdit 
                ? <><span role="img" aria-label="save">💾</span> 수정 완료</>
                : <><span role="img" aria-label="write">✍️</span> 작성 완료</>
            }
          </button>
        </div>
      </form>
    </div>
  );
}