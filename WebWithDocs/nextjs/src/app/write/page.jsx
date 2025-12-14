// app/write/page.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import React, { useState, useEffect, useMemo } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import {
  createPost,
  fetchPostById,
  updatePost,
} from "../../services/api/posts";
import { useAuth } from "../../providers/AuthProvider";
import { useToast } from "../../hooks/useToast"; // ⭐ 추가
import "../../styles/globals.css";
// import "../../styles/PostForm.css"; // 포스트 폼 스타일 추가 (가정)

// Marked.js & DOMPurify 임포트 (Next.js 환경에서 별도 설치 필요)
import { marked } from "marked";
import DOMPurify from "dompurify";

// Marked.js 옵션 설정 (줄바꿈 자동 인식 활성화)
marked.setOptions({
  breaks: true,
});

// Markdown을 안전한 HTML로 변환하는 헬퍼 함수
const renderMarkdown = (markdown) => {
  if (!markdown) return "";
  const rawMarkup = marked.parse(markdown);
  // DOMPurify는 window 객체가 있어야 하므로 클라이언트 컴포넌트에서만 사용 가능
  if (typeof window !== "undefined") {
    return DOMPurify.sanitize(rawMarkup);
  }
  return rawMarkup; // 서버 렌더링 시에는 임시로 raw 반환 (주의: 클라이언트에서 hydration 시 다시 정제됨)
};

export default function WritePostPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { isAuthenticated, id: currentUserId } = useAuth();
  const { showToast } = useToast(); // ⭐ 추가

  // 쿼리 파라미터에서 'edit' ID 가져오기
  const editId = searchParams.get("edit");
  const isEdit = !!editId;

  // 상태 관리
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState(""); // 쉼표로 구분된 문자열
  const [submitLoading, setSubmitLoading] = useState(false);
  const [initialLoading, setInitialLoading] = useState(isEdit);

  // Markdown 프리뷰 (성능 최적화를 위해 useMemo 사용)
  const previewHtml = useMemo(() => renderMarkdown(content), [content]);

  // 수정 모드일 때 기존 데이터 로드
  useEffect(() => {
    if (isEdit && isAuthenticated) {
      const loadPost = async () => {
        try {
          const post = await fetchPostById(editId);
          // 작성자 권한 확인 (클라이언트 측)
          if (post.authorId !== currentUserId) {
            showToast({ message: "수정 권한이 없습니다.", type: "error" }); // ⭐ alert 대체
            router.push(`/post/${editId}`);
            return;
          }

          setTitle(post.title);
          setContent(post.content);
          setCategory(post.categoryName || "");
          setTags(post.tagNames ? post.tagNames.join(", ") : "");
        } catch (error) {
          showToast({ message: "포스트 로드 실패.", type: "error" }); // ⭐ alert 대체
          console.error("Failed to load post for editing:", error);
          router.push("/write"); // 로드 실패 시 새 글쓰기 모드로 전환
        } finally {
          setInitialLoading(false);
        }
      };
      loadPost();
    } else if (isEdit && !isAuthenticated) {
      // 비로그인 상태에서 수정 페이지 접근 시
      showToast({
        message: "로그인 후 포스트를 수정할 수 있습니다.",
        type: "warning",
      });
      router.push(`/signin?redirect=/write?edit=${editId}`);
    } else {
      setInitialLoading(false);
    }
  }, [isEdit, editId, isAuthenticated, currentUserId, router, showToast]);

  // 비인증 사용자 리디렉션 (CSR에서)
  useEffect(() => {
    if (typeof window !== "undefined" && !isAuthenticated && !isEdit) {
      showToast({
        message: "로그인 후 글쓰기를 할 수 있습니다.",
        type: "warning",
      });
      router.push("/signin?redirect=/write");
    }
  }, [isAuthenticated, isEdit, router, showToast]);

  // 제출 핸들러
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (submitLoading) return;

    setSubmitLoading(true);

    // 태그 문자열을 배열로 변환
    const tagList = tags
      .split(",")
      .map((tag) => tag.trim())
      .filter((tag) => tag.length > 0);

    const postData = {
      title,
      content,
      categoryName: category,
      tagNames: tagList,
    };

    try {
      let resultPost;
      if (isEdit) {
        // 수정 요청
        resultPost = await updatePost(editId, postData);
        showToast({
          message: "포스트가 성공적으로 수정되었습니다.",
          type: "success",
        }); // ⭐ alert 대체
      } else {
        // 생성 요청
        resultPost = await createPost(postData);
        showToast({
          message: "새 포스트가 성공적으로 작성되었습니다.",
          type: "success",
        }); // ⭐ alert 대체
      }

      // 작성/수정 후 상세 페이지로 이동
      router.push(`/post/${resultPost.id}`);
    } catch (error) {
      showToast({
        message: error.message || "포스트 작성/수정 실패: 권한 또는 서버 오류",
        type: "error",
      }); // ⭐ alert 대체
      console.error(error);
    } finally {
      setSubmitLoading(false);
    }
  };

  if (initialLoading) {
    return (
      <div
        className="container"
        style={{ textAlign: "center", padding: "50px" }}
      >
        <h1 className="page-title">
          {isEdit ? "포스트 로딩 중..." : "글 작성"}
        </h1>
      </div>
    );
  }

  // 비인증 상태에서 isEdit이 false일 때도 폼을 보여주지 않습니다 (useEffect에서 리디렉션 처리)
  if (!isAuthenticated && !isEdit) {
    return null;
  }

  return (
    <div className="container">
      <h1 className="page-title">
        {isEdit ? "포스트 수정" : "새 포스트 작성"}
      </h1>
      <form onSubmit={handleSubmit} className="post-form">
        <input
          type="text"
          placeholder="제목을 입력해주세요"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          className="post-form-title"
        />

        {/* 마크다운 에디터 및 미리보기 컨테이너 */}
        <div className="markdown-editor-container">
          {/* 에디터 영역 */}
          <div className="editor-pane">
            <label className="editor-label">Markdown Editor</label>
            <textarea
              placeholder="내용을 마크다운 문법으로 작성해주세요"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
              className="post-form-textarea"
            />
          </div>

          {/* 미리보기 */}
          <div className="preview-pane">
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
              ? "포스트 수정"
              : "포스트 작성"}
          </button>
        </div>
      </form>
    </div>
  );
}
