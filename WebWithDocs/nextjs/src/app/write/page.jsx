// app/write/page.jsx
"use client"; 

import React, { useState, useEffect, useMemo } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import {
  createPost,
  fetchPostById,
  updatePost,
} from "../../services/api/posts";
import { useAuth } from "../../providers/AuthProvider";
import { useToast } from "../../hooks/useToast"; 
import "../../styles/globals.css";

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
    // HTML Sanitization 적용
    return DOMPurify.sanitize(rawMarkup);
  }
  // 서버 렌더링 환경을 위해 임시로 rawMarkup 반환
  return rawMarkup; 
};


export default function WritePage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { isAuthenticated, id: currentUserId } = useAuth();
  const { showToast } = useToast();

  // 수정 모드 ID
  const editId = searchParams.get("id");
  const isEdit = useMemo(() => !!editId, [editId]);

  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("");
  const [tags, setTags] = useState("");
  const [content, setContent] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [submitLoading, setSubmitLoading] = useState(false);

  // 수정 모드일 때 포스트 데이터 불러오기
  useEffect(() => {
    if (!isAuthenticated) {
        // 🌟 UI 텍스트 한국어 우선: 로그인이 필요합니다.
        showToast({ message: "로그인이 필요합니다.", type: "warning" });
        router.replace("/signin");
        return;
    }

    if (isEdit) {
      const loadPost = async () => {
        try {
          const post = await fetchPostById(editId);
          // 작성자 불일치 시 처리
          if (post.authorId.toString() !== currentUserId.toString()) {
            // 🌟 UI 텍스트 한국어 우선: 수정 권한이 없습니다.
            showToast({ message: "수정 권한이 없습니다.", type: "error" });
            router.replace(`/post/${editId}`);
            return;
          }

          setTitle(post.title);
          setCategory(post.categoryName || "");
          setTags(post.tagNames ? post.tagNames.join(", ") : "");
          setContent(post.content);
        } catch (error) {
          // 🌟 UI 텍스트 한국어 우선: 포스트를 불러오는 데 실패했습니다.
          showToast({ message: "포스트를 불러오는 데 실패했습니다.", type: "error" });
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


  // 폼 제출 핸들러 (작성/수정 공통)
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!title || !content || !category) {
        // 🌟 UI 텍스트 한국어 우선: 필수 입력 필드를 모두 채워주세요.
        showToast({ message: "필수 입력 필드를 모두 채워주세요.", type: "warning" });
        return;
    }
    
    setSubmitLoading(true);

    const tagList = tags.split(",").map(tag => tag.trim()).filter(tag => tag.length > 0);

    const postRequestData = {
      title,
      content,
      categoryName: category,
      tagNames: tagList,
    };

    try {
      let result;
      if (isEdit) {
        // 수정 모드
        result = await updatePost(editId, postRequestData);
        // 🌟 UI 텍스트 한국어 우선: 포스트가 성공적으로 수정되었습니다.
        showToast({ message: "포스트가 성공적으로 수정되었습니다.", type: "success" });
      } else {
        // 작성 모드
        result = await createPost(postRequestData);
        // 🌟 UI 텍스트 한국어 우선: 포스트가 성공적으로 작성되었습니다.
        showToast({ message: "포스트가 성공적으로 작성되었습니다.", type: "success" });
      }
      
      router.push(`/post/${result.id}`);

    } catch (error) {
      const action = isEdit ? "수정" : "작성";
      // 🌟 UI 텍스트 한국어 우선: 포스트 {action} 실패: 권한 또는 서버 오류
      showToast({ message: `포스트 ${action} 실패: 권한 또는 서버 오류.`, type: "error" });
      console.error(error);
    } finally {
      setSubmitLoading(false);
    }
  };

  if (isLoading) {
    // 🌟 UI 텍스트 한국어 우선: 불러오는 중...
    return <div style={{ textAlign: 'center', padding: '100px 0' }}>불러오는 중...</div>;
  }

  return (
    <div style={{ maxWidth: "1000px", margin: "0 auto", padding: "40px 0" }}>
        <h1 
            style={{ 
                fontSize: "2.5rem", 
                fontWeight: 700, 
                marginBottom: "40px", 
                color: "var(--color-text-main)",
                textAlign: "center"
            }}
        >
            {/* 🌟 UI 텍스트 한국어 우선: 글 수정 / 새 글 작성 */}
            {isEdit ? "글 수정 ✏️" : "새 글 작성 📝"}
        </h1>
        
        <form onSubmit={handleSubmit} className="post-form">
            {/* 제목 입력 */}
            <input
                type="text"
                // 🌟 UI 텍스트 한국어 우선: 제목을 입력해주세요
                placeholder="제목을 입력해주세요"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
                className="post-form-input"
                style={{ marginBottom: "20px", fontSize: "1.5em", fontWeight: 700 }}
            />
            
            {/* 카테고리/태그 입력 */}
            <input
                type="text"
                // 🌟 UI 텍스트 한국어 우선: 카테고리 (예. Frontend, Backend)
                placeholder="카테고리 (예. Frontend, Backend)"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                required
                className="post-form-input"
                style={{ marginBottom: "15px" }}
            />
            <input
                type="text"
                // 🌟 UI 텍스트 한국어 우선: 태그 (쉼표로 구분하여 입력: 예. tag1, tag2)
                placeholder="태그 (쉼표로 구분하여 입력: 예. tag1, tag2)"
                value={tags}
                onChange={(e) => setTags(e.target.value)}
                className="post-form-input"
                style={{ marginBottom: "15px" }}
            />

            <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
                {/* 마크다운 입력 영역 */}
                <div style={{ flex: 1 }}>
                    <h3 style={{ marginTop: 0, marginBottom: "10px", color: "var(--color-text-sub)" }}>
                        {/* 🌟 UI 텍스트 한국어 우선: 마크다운 입력 */}
                        마크다운 입력
                    </h3>
                    <textarea
                        // 🌟 UI 텍스트 한국어 우선: 내용을 마크다운으로 작성해주세요
                        placeholder="내용을 마크다운으로 작성해주세요"
                        value={content}
                        onChange={(e) => setContent(e.target.value)}
                        required
                        className="post-form-textarea"
                        style={{ minHeight: "500px", fontFamily: "monospace", fontSize: "1em" }}
                    />
                </div>

                {/* 미리보기 영역 */}
                <div style={{ flex: 1 }}>
                    <h3 style={{ marginTop: 0, marginBottom: "10px", color: "var(--color-text-sub)" }}>
                        {/* 🌟 UI 텍스트 한국어 우선: 미리보기 */}
                        미리보기
                    </h3>
                    <div 
                        className="markdown-body" // globals.css의 마크다운 스타일 적용
                        dangerouslySetInnerHTML={{ __html: renderMarkdown(content) }}
                        style={{
                            minHeight: "500px",
                            padding: "15px",
                            border: "1px solid var(--color-border)",
                            borderRadius: "8px",
                            backgroundColor: "var(--color-primary)",
                            overflowY: "auto"
                        }}
                    >
                    </div>
                </div>
            </div>


            {/* 버튼 영역 */}
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
                        {/* 🌟 UI 텍스트 한국어 우선: 취소 */}
                        취소
                    </Link>
                )}
                <button
                    type="submit"
                    className="btn-primary"
                    disabled={submitLoading || !title || !content || !category}
                >
                    {/* 🌟 UI 텍스트 한국어 우선: 수정 중.../작성 중.../수정/작성 */}
                    {submitLoading
                        ? (isEdit ? "수정 중..." : "작성 중...")
                        : (isEdit ? "글 수정" : "글 작성")
                    }
                </button>
            </div>
        </form>
    </div>
  );
}