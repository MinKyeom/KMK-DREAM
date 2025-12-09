// src/pages/Post/WritePost.jsx

import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { createPost, fetchPostById, updatePost } from "../../api/posts";

// isEdit prop을 받아 수정 모드인지 확인합니다.
export default function WritePost({ isEdit = false }) {
  const { id } = useParams(); // URL에서 ID를 가져옴 (수정 모드일 때 사용)
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState(""); // 쉼표로 구분된 문자열
  const [loading, setLoading] = useState(false);

  // 수정 모드일 때 기존 글 불러오기
  useEffect(() => {
    if (isEdit && id) {
      setLoading(true);
      fetchPostById(id)
        .then((post) => {
          // 작성자 확인은 백엔드에서 수행하므로 여기서는 데이터 로딩만
          setTitle(post.title);
          setContent(post.content);
          setCategory(post.category?.name || "");
          // 태그 배열을 쉼표로 구분된 문자열로 변환하여 입력 필드에 설정
          setTags(post.tags?.map((tag) => tag.name).join(", ") || "");
        })
        .catch((error) => {
          alert("수정할 글을 불러오지 못했습니다. 권한을 확인하세요.");
          navigate("/");
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, [isEdit, id, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    // 태그 문자열을 쉼표, 공백 등을 기준으로 배열로 분리
    const tagsArray = tags
      .split(/,\s*|,\s*|\s+/)
      .map((tag) => tag.trim())
      .filter((tag) => tag.length > 0);

    const postData = {
      title,
      content,
      category: category.trim(),
      tags: tagsArray,
    };

    try {
      if (isEdit) {
        await updatePost(id, postData);
        alert("글이 성공적으로 수정되었습니다.");
      } else {
        await createPost(postData);
        alert("새 글이 성공적으로 작성되었습니다.");
      }
      navigate("/"); // 작성/수정 후 목록 페이지로 이동
    } catch (error) {
      const message =
        error.response?.data?.error ||
        "처리 실패: 로그인이 필요하거나 권한이 없습니다.";
      alert(message);
      console.error("Post operation error:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading && isEdit) {
    return <div style={{ textAlign: "center", padding: "50px" }}>글 불러오는 중...</div>;
  }

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "20px auto",
        padding: "30px",
        backgroundColor: "var(--color-primary)",
        borderRadius: "8px",
        boxShadow: "0 2px 10px var(--color-shadow)",
        textAlign: "left",
      }}
    >
      <h2 style={{ color: "var(--color-text-main)", marginBottom: "20px" }}>
        {isEdit ? "글 수정" : "새 글 작성"}
      </h2>
      <form
        onSubmit={handleSubmit}
        style={{ display: "flex", flexDirection: "column", gap: "5px" }}
      >
        <input
          type="text"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          style={{ fontSize: "1.2em", padding: "10px", marginBottom: "10px" }}
        />
        <textarea
          placeholder="내용 (Markdown 지원)"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="15"
          required
          style={{ padding: "10px", marginBottom: "10px" }}
        />
        <input
          type="text"
          placeholder="카테고리"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          required
          style={{ padding: "8px", marginBottom: "10px" }}
        />
        <input
          type="text"
          placeholder="태그 (쉼표로 구분하여 입력)"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          style={{ padding: "8px", marginBottom: "10px" }}
        />
        <button type="submit" className="btn-primary" disabled={loading}>
          {loading ? "처리 중..." : isEdit ? "수정 완료" : "작성 완료"}
        </button>
      </form>
    </div>
  );
}