// src/components/Post/PostCard.jsx
// ⭐ Server Component (기본값)

import Link from "next/link"; // next/link 사용

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('ko-KR', { 
        year: 'numeric', month: 'long', day: 'numeric' 
    });
};

// --- 서브 컴포넌트: 포스트 목록 카드 (Homepage용) --
export default function PostCard({ post }) {
    return (
        <Link href={`/post/${post.id}`} className="post-card">
            <h3>{post.title || "제목 없음"}</h3>
            <p>
                {/* 내용 요약 */}
                {post.content.substring(0, 120)}{post.content.length > 120 ? '...' : ''}
            </p>
            <div className="post-meta">
                <span style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
                    {/* 닉네임 표시 */}
                    <span style={{ fontWeight: 600, color: 'var(--color-text-main)' }}>
                        {post.authorNickname || "작성자 알 수 없음"}
                    </span>
                    <span style={{ fontSize: '0.9em', color: 'var(--color-text-sub)', marginTop: '4px' }}>
                        {formatDate(post.createdAt)}
                    </span>
                </span>
                <span className="tag-badge">
                    {post.categoryName || "미분류"}
                </span>
            </div>
        </Link>
    );
};