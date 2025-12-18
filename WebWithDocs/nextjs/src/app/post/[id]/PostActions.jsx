// app/post/[id]/PostActions.jsx
"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "../../../providers/AuthProvider";
import { deletePost } from "../../../services/api/posts";
import { useToast } from "../../../hooks/useToast";

export default function PostActions({ postId, postAuthorId }) {
  const { id: currentUserId } = useAuth();
  const router = useRouter();
  const { showToast } = useToast();

  const isAuthor =
    currentUserId && currentUserId.toString() === postAuthorId.toString();

  const handleDelete = async () => {
    if (window.confirm("정말로 이 포스트를 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")) {
      try {
        await deletePost(postId);
        showToast({ message: "포스트가 삭제되었습니다.", type: "success" });
        router.push("/post");
      } catch (error) {
        showToast({
          message: error.message || "포스트 삭제 실패: 권한 또는 서버 오류.",
          type: "error",
        });
        console.error(error);
      }
    }
  };

  if (!isAuthor) return null;

  return (
    <div className="post-action-buttons" style={{ display: "flex", justifyContent: "flex-end", gap: "15px" }}>
      {/* 🌟 경로를 /post/new로 수정하여 404 방지 */}
      <Link href={`/post/new?id=${postId}`} className="btn-secondary-small">
        수정
      </Link>
      <button onClick={handleDelete} className="btn-primary-small">
        삭제
      </button>
    </div>
  );
}