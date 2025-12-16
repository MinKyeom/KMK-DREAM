// app/post/[id]/PostActions.jsx
"use client"; 

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../src/providers/AuthProvider"; 
import { deletePost } from "../../../src/services/api/posts"; 
import { useToast } from "../../../src/hooks/useToast"; 

/**
 * 포스트 수정/삭제 버튼 컴포넌트 (Client Component)
 * @param {object} props - postId: 게시글 ID, postAuthorId: 작성자 ID
 */
export default function PostActions({ postId, postAuthorId }) {
    const { id: currentUserId } = useAuth();
    const router = useRouter();
    const { showToast } = useToast(); 

    // 현재 로그인 사용자가 작성자와 일치하는지 확인
    const isAuthor = currentUserId && (currentUserId.toString() === postAuthorId.toString());

    // 포스트 삭제 핸들러
    const handleDelete = async () => {
        // 🌟 UI 텍스트 한국어 우선: 정말로 이 포스트를 삭제하시겠습니까? 되돌릴 수 없습니다.
        if (window.confirm("정말로 이 포스트를 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")) { 
            try {
                await deletePost(postId);
                // 🌟 UI 텍스트 한국어 우선: 포스트가 삭제되었습니다.
                showToast({ message: "포스트가 삭제되었습니다.", type: "success" }); 
                router.push("/post"); // 목록 페이지로 리디렉션
            } catch (error) {
                // 🌟 UI 텍스트 한국어 우선: 포스트 삭제 실패: 권한 또는 서버 오류
                showToast({ message: error.message || "포스트 삭제 실패: 권한 또는 서버 오류.", type: "error" }); 
                console.error(error);
            }
        }
    };

    if (!isAuthor) {
        return null; 
    }

    return (
        <div className="post-action-buttons" style={{ display: 'flex', justifyContent: 'flex-end', gap: '15px', marginBottom: '0' }}>
            <Link
                href={`/write?id=${postId}`}
                className="btn-secondary-small"
            >
                {/* 🌟 UI 텍스트 한국어 우선: 수정 */}
                수정
            </Link>
            <button
                onClick={handleDelete}
                className="btn-primary-small" 
            >
                {/* 🌟 UI 텍스트 한국어 우선: 삭제 */}
                삭제
            </button>
        </div>
    );
}