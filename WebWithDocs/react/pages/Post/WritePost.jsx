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

  // 수정 모드일 때 기존 글 불러오기
  useEffect(() => {
    if (isEdit && id) {
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
        });
    }
  }, [isEdit, id, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 쉼표로 구분된 태그 문자열을 배열로 변환
    const tagsArray = tags
      .split(",")
      .map((tag) => tag.trim())
      .filter((tag) => tag.length > 0);

    // PostRequest DTO에 맞춘 데이터 구성
    const postData = {
      title,
      content,
      category,
      tags: tagsArray,
      // authorId는 백엔드에서 JWT 토큰을 통해 추출되므로 프론트에서 전송하지 않음
    };

    try {
      if (isEdit) {
        // 글 수정 API 호출
        await updatePost(id, postData);
        alert("글이 성공적으로 수정되었습니다.");
        navigate(`/post/${id}`);
      } else {
        // 새 글 작성 API 호출
        const newPost = await createPost(postData);
        alert("글이 성공적으로 작성되었습니다.");
        navigate(`/post/${newPost.id}`);
      }
    } catch (error) {
      // 백엔드에서 권한이 없으면 403 Forbidden 에러 발생
      const errorMessage =
        error.response?.data?.error ||
        "작성/수정 실패: 로그인이 필요하거나 권한이 없습니다.";
      alert(errorMessage);
      console.error("Post operation error:", error);
      if (error.message.includes("로그인이 필요")) {
        navigate("/signin"); // 로그인 페이지로 리다이렉트
      }
    }
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "50px auto",
        padding: "30px",
        backgroundColor: "var(--color-primary)",
        border: "1px solid var(--color-border)",
        borderRadius: "8px",
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
        <button
          type="submit"
          className="btn-primary"
          style={{ padding: "12px", marginTop: "10px", fontSize: "1.1em" }}
        >
          {isEdit ? "수정 완료" : "작성하기"}
        </button>
      </form>
    </div>
  );
}
