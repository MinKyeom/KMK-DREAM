// app/post/[id]/PostActions.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../src/providers/AuthProvider"; 
import { deletePost } from "../../../src/services/api/posts"; 
import { useToast } from "../../../src/hooks/useToast"; // ⭐ useToast 추가

/**
 * 포스트 수정/삭제 버튼 컴포넌트 (Client Component)
 * @param {object} props - postId: 게시글 ID, postAuthorId: 작성자 ID
 */
export default function PostActions({ postId, postAuthorId }) {
    const { id: currentUserId } = useAuth();
    const router = useRouter();
    const { showToast } = useToast(); // ⭐ useToast 훅 호출

    // 현재 로그인 사용자가 작성자와 일치하는지 확인 (Client-side check)
    const isAuthor = currentUserId && (currentUserId.toString() === postAuthorId.toString());

    const handleDelete = async () => {
        // ⚠️ window.confirm 대체: 토스트는 confirm을 대체하지 않으므로, 커스텀 모달이 필요합니다.
        // 여기서는 UX를 개선하기 위해 confirm을 유지합니다. (실제 프로젝트에서는 커스텀 모달 사용 권장)
        if (window.confirm("정말로 이 포스트를 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")) { // ⭐ confirm 유지
            try {
                await deletePost(postId);
                showToast({ message: "포스트가 삭제되었습니다.", type: "success" }); // ⭐ alert 대체
                router.push("/post"); // 목록 페이지로 리디렉션
            } catch (error) {
                showToast({ message: error.message || "포스트 삭제 실패: 권한 또는 서버 오류", type: "error" }); // ⭐ alert 대체
                console.error(error);
            }
        }
    };

    if (!isAuthor) {
        return null; // 작성자가 아니면 버튼을 표시하지 않음
    }

    return (
        <div className="post-action-buttons" style={{ display: 'flex', justifyContent: 'flex-end', gap: '15px', marginBottom: '30px' }}>
            <Link
                href={`/write?editId=${postId}`}
                className="btn-secondary"
            >
                수정 ✏️
            </Link>
            <button
                onClick={handleDelete}
                className="btn-danger"
            >
                삭제 🗑️
            </button>
        </div>
    );
}