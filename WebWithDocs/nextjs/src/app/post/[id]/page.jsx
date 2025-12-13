// app/post/[id]/page.jsx (Server Component)

import Link from "next/link";
import { fetchPostById } from "../../../src/services/api/posts"; // API 경로 수정
import Comments from "../../../src/components/Comments/Comments"; // Client Component 임포트
import MarkdownRenderer from "../../../src/components/MarkdownRenderer"; // Client Component 임포트
import PostActions from "./PostActions"; // Client Component 임포트
import '../../../src/styles/globals.css';
import { notFound } from "next/navigation"; // Next.js의 404 처리

// 날짜 포맷팅 헬퍼 함수
const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('ko-KR', {
        year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit'
    });
};

// 동적 경로 세그먼트 (id)를 받아 데이터를 가져옵니다.
async function getPost(id) {
    try {
        const data = await fetchPostById(id);
        return data;
    } catch (error) {
        console.error("Failed to fetch post on server:", error);
        return null;
    }
}

// SEO 최적화: 동적 메타데이터 생성
export async function generateMetadata({ params }) {
    const post = await getPost(params.id);
    if (!post) {
        return {
            title: '포스트를 찾을 수 없음',
            description: '존재하지 않는 포스트입니다.'
        };
    }

    // 포스트 내용의 요약을 설명으로 사용
    const description = post.content.substring(0, 150) + (post.content.length > 150 ? '...' : '');
    // 태그를 키워드로 사용
    const keywords = post.tagNames ? [...post.tagNames, post.categoryName] : [post.categoryName];

    return {
        title: post.title, // 개별 포스트 제목
        description: description, // 포스트 내용 요약
        keywords: keywords,
        authors: [{ name: post.authorNickname || '익명 작성자' }],
        alternates: {
            canonical: `https://your-blog-url.com/post/${params.id}`, // 포스트 정규 URL
        },
    };
}

// Post Detail Component
export default async function PostDetailPage({ params }) {
    const postId = params.id;
    const post = await getPost(postId);

    if (!post) {
        // 포스트가 없으면 Next.js의 404 페이지를 렌더링합니다.
        notFound(); 
    }
    
    // PostActions 컴포넌트에서 권한 확인을 위해 문자열로 전달
    const postAuthorId = post.authorId; 

    return (
        <div className="homepage-container">
            <article className="post-detail-container">
                {/* 1. 제목 및 메타 정보 */}
                <h1 className="post-detail-title">{post.title}</h1>
                
                <div className="post-detail-meta" style={{ 
                    borderBottom: '1px solid var(--color-border)', 
                    paddingBottom: '20px', 
                    marginBottom: '30px',
                    display: 'flex', 
                    justifyContent: 'space-between',
                    alignItems: 'center',
                }}>
                    <span style={{ fontWeight: 600, color: 'var(--color-text-main)' }}>
                        {post.authorNickname || "작성자 알 수 없음"}
                    </span>
                    <span style={{ fontSize: '0.9em', color: 'var(--color-text-sub)' }}>
                        작성일: {formatDate(post.createdAt)}
                    </span>
                </div>
                
                {/* 4. 수정/삭제 버튼 (Client Component) */}
                <PostActions 
                    postId={post.id} 
                    postAuthorId={postAuthorId} 
                />

                {/* 2. 본문 내용 (마크다운 렌더링 적용 - Client Component) */}
                <div
                    className="post-detail-content"
                    style={{ padding: "40px 0", minHeight: "300px" }}
                >
                    {/* MarkdownRenderer는 Client Component입니다. */}
                    <MarkdownRenderer content={post.content} /> 
                </div>

                {/* 3. 태그 리스트 */}
                <div style={{ margin: "20px 0 40px 0", borderTop: "1px solid var(--color-border)", paddingTop: "20px" }}>
                    <p style={{ margin: "0", color: "var(--color-text-sub)", fontWeight: 600 }}>
                        # 카테고리: {" "}
                        <span className="tag-badge" style={{ backgroundColor: 'var(--color-secondary)', color: 'var(--color-accent)' }}>
                            {post.categoryName || "미분류"}
                        </span>
                    </p>
                    <p style={{ margin: "10px 0 0 0", color: "var(--color-text-sub)", fontWeight: 600 }}>
                        # 태그: {" "}
                        {post.tagNames?.length > 0 ? (
                            post.tagNames.map((tagName) => (
                                <span key={tagName} className="tag-badge">
                                    {tagName}
                                </span>
                            ))
                        ) : (
                            <span>태그 없음</span>
                        )}
                    </p>
                </div>

                {/* 5. 댓글 섹션 (Client Component) */}
                <Comments postId={postId} />
            </article>
        </div>
    );
}