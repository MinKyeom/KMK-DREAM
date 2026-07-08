// app/post/new/page.jsx
"use client";

import React, { useState, useEffect, useMemo } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import {
  createPost,
  fetchPostById,
  updatePost,
} from "../../../services/api/posts";
import { useAuth } from "../../../providers/AuthProvider";
import { useToast } from "../../../hooks/useToast";
import "../../../styles/globals.css";

import { marked } from "marked";
import DOMPurify from "dompurify";

marked.setOptions({
  breaks: true,
});

const renderMarkdown = (markdown) => {
  if (!markdown) return "";
  const rawMarkup = marked.parse(markdown);
  if (typeof window !== "undefined") {
    return DOMPurify.sanitize(rawMarkup);
  }
  return rawMarkup;
};

export default function WritePage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { isAuthenticated, id: currentUserId } = useAuth();
  const { showToast } = useToast();

  const editId = searchParams.get("id");
  const isEdit = useMemo(() => !!editId, [editId]);

  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [submitLoading, setSubmitLoading] = useState(false);

  useEffect(() => {
    if (!isAuthenticated) {
      showToast({ message: "로그인이 필요합니다.", type: "warning" });
      router.replace("/signin");
      return;
    }

    if (isEdit) {
      const loadPost = async () => {
        try {
          const post = await fetchPostById(editId);
          if (post.authorId.toString() !== currentUserId.toString()) {
            showToast({ message: "수정 권한이 없습니다.", type: "error" });
            router.replace(`/post/${editId}`);
            return;
          }

          setTitle(post.title);
          setCategory(post.categoryName || "");
          setTags(post.tagNames ? post.tagNames.join(", ") : "");
          setContent(post.content);
        } catch (error) {
          showToast({
            message: "포스트를 불러오는 데 실패했습니다.",
            type: "error",
          });
          router.replace("/post");
        } finally {
          setIsLoading(false);
        }
      };
      loadPost();
    } else {
      setIsLoading(false);
    }
  }, [isEdit, editId, isAuthenticated, currentUserId, router, showToast]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !content || !category) {
      showToast({
        message: "필수 입력 필드를 모두 채워주세요.",
        type: "warning",
      });
      return;
    }

    setSubmitLoading(true);
    const tagList = tags
      .split(",")
      .map((tag) => tag.trim())
      .filter((tag) => tag.length > 0);

    const postRequestData = {
      title,
      content,
      categoryName: category,
      tagNames: tagList,
    };

    try {
      let result;
      if (isEdit) {
        result = await updatePost(editId, postRequestData);
        showToast({
          message: "포스트가 성공적으로 수정되었습니다.",
          type: "success",
        });
      } else {
        result = await createPost(postRequestData);
        showToast({
          message: "포스트가 성공적으로 작성되었습니다.",
          type: "success",
        });
      }
      router.push(`/post/${result.id}`);
    } catch (error) {
      const action = isEdit ? "수정" : "작성";
      showToast({
        message: `포스트 ${action} 실패: 권한 또는 서버 오류.`,
        type: "error",
      });
    } finally {
      setSubmitLoading(false);
    }
  };

  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: "100px 0" }}>
        불러오는 중...
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "1000px", margin: "0 auto", padding: "40px 0" }}>
      <h1
        style={{
          fontSize: "2.5rem",
          fontWeight: 700,
          marginBottom: "40px",
          color: "var(--color-text-main)",
          textAlign: "center",
        }}
      >
        {isEdit ? "글 수정 ✏️" : "새 글 작성 📝"}
      </h1>
      <form onSubmit={handleSubmit} className="post-form">
        <input
          type="text"
          placeholder="제목을 입력해주세요"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          className="post-form-input"
          style={{ marginBottom: "20px", fontSize: "1.5em", fontWeight: 700 }}
        />
        <input
          type="text"
          placeholder="카테고리 (예. Frontend, Backend)"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          required
          className="post-form-input"
          style={{ marginBottom: "15px" }}
        />
        <input
          type="text"
          placeholder="태그 (쉼표로 구분하여 입력: 예. tag1, tag2)"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          className="post-form-input"
          style={{ marginBottom: "15px" }}
        />
        <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
          <div style={{ flex: 1 }}>
            <h3
              style={{
                marginTop: 0,
                marginBottom: "10px",
                color: "var(--color-text-sub)",
              }}
            >
              마크다운 입력
            </h3>
            <textarea
              placeholder="내용을 마크다운으로 작성해주세요"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
              className="post-form-textarea"
              style={{
                minHeight: "500px",
                fontFamily: "monospace",
                fontSize: "1em",
              }}
            />
          </div>
          <div style={{ flex: 1 }}>
            <h3
              style={{
                marginTop: 0,
                marginBottom: "10px",
                color: "var(--color-text-sub)",
              }}
            >
              미리보기
            </h3>
            <div
              className="markdown-body"
              dangerouslySetInnerHTML={{ __html: renderMarkdown(content) }}
              style={{
                minHeight: "500px",
                padding: "15px",
                border: "1px solid var(--color-border)",
                borderRadius: "8px",
                backgroundColor: "var(--color-primary)",
                overflowY: "auto",
              }}
            ></div>
          </div>
        </div>
        <div
          style={{
            marginTop: "20px",
            textAlign: "right",
            display: "flex",
            gap: "15px",
            justifyContent: "flex-end",
          }}
        >
          {isEdit && (
            <Link href={`/post/${editId}`} className="btn-secondary">
              취소
            </Link>
          )}
          <button
            type="submit"
            className="btn-primary"
            disabled={submitLoading || !title || !content || !category}
          >
            {submitLoading
              ? isEdit
                ? "수정 중..."
                : "작성 중..."
              : isEdit
              ? "글 수정"
              : "글 작성"}
          </button>
        </div>
      </form>
    </div>
  );
}
