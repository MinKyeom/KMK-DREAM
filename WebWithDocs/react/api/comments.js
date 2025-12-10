// src/api/comments.js

import axios from "axios";
import { getAuthHeaders } from "./auth"; // 인증 헤더 유틸리티 가정

// API 기본 URL (다른 파일들과 동일하게 설정)
const BASE_URL = "http://localhost:8080";
// ⭐ 수정: 모든 댓글 API는 이 경로를 사용하도록 통일 (Controller 정의에 따름)
const POSTS_API_URL = `${BASE_URL}/api/posts`;

// -----------------------------------------------------------
// 1. 특정 글의 댓글 목록 조회 (GET /api/posts/{postId}/comments)
// -----------------------------------------------------------
/**
 * 특정 게시글의 모든 댓글 목록을 조회합니다.
 * @param {string | number} postId - 댓글을 조회할 게시글 ID
 * @returns {Promise<Comment[]>} 댓글 객체 목록을 담은 배열
 */
export const fetchCommentsByPostId = async (postId) => {
  try {
    const response = await axios.get(`${POSTS_API_URL}/${postId}/comments`);
    return response.data; // Comment DTO 배열 반환 가정
  } catch (error) {
    console.error(`Error fetching comments for post ID ${postId}:`, error);
    // throw error; // 오류 처리를 상위 컴포넌트에 위임
    throw new Error(error.response?.data?.message || "댓글 목록 조회 실패");
  }
};

// -----------------------------------------------------------
// 2. 새 댓글 작성 (POST /api/posts/{postId}/comments)
// -----------------------------------------------------------
/**
 * 특정 게시글에 새 댓글을 작성합니다. (인증 필수)
 * @param {string | number} postId - 댓글을 작성할 게시글 ID
 * @param {{ content: string }} requestData - 댓글 내용
 * @returns {Promise<Comment>} 생성된 댓글 객체
 */
export const createComment = async (postId, requestData) => {
  const headers = getAuthHeaders();
  if (!headers.Authorization) {
    throw new Error("댓글 작성을 위해서는 로그인이 필요합니다.");
  }
  try {
    const response = await axios.post(
      `${POSTS_API_URL}/${postId}/comments`,
      requestData,
      { headers }
    );
    return response.data; // 생성된 Comment 객체 반환 가정
  } catch (error) {
    console.error(`Error creating comment for post ID ${postId}:`, error);
    // 서버 응답 오류 메시지를 포함하여 오류 발생
    throw new Error(
      error.response?.data?.message ||
        "댓글 작성 실패: 로그인 상태를 확인하세요."
    );
  }
};

// -----------------------------------------------------------
// 3. 댓글 수정 (PUT /api/posts/comments/{commentId})
// -----------------------------------------------------------
/**
 * 댓글을 수정합니다. (인증 필수, 작성자 권한 확인은 백엔드에서 수행)
 * @param {string | number} commentId - 수정할 댓글 ID
 * @param {{ content: string }} requestData - 수정된 댓글 내용
 * @returns {Promise<Comment>} 수정된 댓글 객체
 */
export const updateComment = async (commentId, requestData) => {
  const headers = getAuthHeaders();
  if (!headers.Authorization) {
    throw new Error("댓글 수정 권한이 없습니다. 로그인이 필요합니다.");
  }
  try {
    // ⭐ 수정: 경로를 CommentController.java의 @PutMapping("/comments/{commentId}")에 맞춤
    const response = await axios.put(
      `${POSTS_API_URL}/comments/${commentId}`,
      requestData,
      { headers }
    );
    return response.data; // 수정된 Comment 객체 반환 가정
  } catch (error) {
    console.error(`Error updating comment with ID ${commentId}:`, error);
    throw new Error(
      error.response?.data?.message || "댓글 수정 실패: 권한 또는 서버 오류"
    );
  }
};

// -----------------------------------------------------------
// 4. 댓글 삭제 (DELETE /api/posts/comments/{commentId})
// -----------------------------------------------------------
/**
 * 댓글을 삭제합니다. (인증 필수, 작성자 권한 확인은 백엔드에서 수행)
 * @param {string | number} commentId - 삭제할 댓글 ID
 */
export const deleteComment = async (commentId) => {
  const headers = getAuthHeaders();
  if (!headers.Authorization) {
    throw new Error("댓글 삭제 권한이 없습니다. 로그인이 필요합니다.");
  }
  try {
    // ⭐ 수정: 경로를 CommentController.java의 @DeleteMapping("/comments/{commentId}")에 맞춤
    await axios.delete(`${POSTS_API_URL}/comments/${commentId}`, { headers });
  } catch (error) {
    console.error(`Error deleting comment with ID ${commentId}:`, error);
    // 백엔드에서 권한 오류 (403 Forbidden) 등을 처리한다고 가정
    throw new Error(
      error.response?.data?.message || "댓글 삭제 실패: 권한 또는 서버 오류"
    );
  }
};
