// src/services/api/posts.js
import axios from "axios";

const POSTS_BASE_URL =
  process.env.NEXT_PUBLIC_POST_API_URL || "http://localhost:8082";
const POSTS_API_URL = `${POSTS_BASE_URL}/api/posts`;

// 인증용 Axios 인스턴스
const authAxios = axios.create({
  baseURL: POSTS_BASE_URL,
  withCredentials: true, // 🌟 중요: 쿠키 전송 활성화
});

/**
 * 전체 글 목록 조회 (인증 불필요)
 */
export const fetchPosts = async (page = 0, size = 10) => {
  try {
    const response = await axios.get(POSTS_API_URL, {
      params: { page, size },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching posts:", error);
    throw error;
  }
};

/**
 * 포스트 상세 조회 (인증 불필요)
 */
export const fetchPostById = async (id) => {
  try {
    const response = await axios.get(`${POSTS_API_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching post with ID ${id}:`, error);
    throw error;
  }
};

/**
 * 새 글 작성 (인증 필수)
 */
export const createPost = async (postRequestData) => {
  try {
    // 🌟 baseURL이 설정되어 있으므로 /api/posts 상대경로만 사용
    const response = await authAxios.post("/api/posts", postRequestData);
    return response.data;
  } catch (error) {
    console.error("Error creating post:", error);
    throw error;
  }
};

/**
 * 글 수정 (인증 필수)
 */
export const updatePost = async (id, postRequestData) => {
  try {
    const response = await authAxios.put(`/api/posts/${id}`, postRequestData);
    return response.data;
  } catch (error) {
    console.error(`Error updating post ${id}:`, error);
    throw error;
  }
};

/**
 * 글 삭제 (인증 필수)
 */
export const deletePost = async (id) => {
  try {
    const response = await authAxios.delete(`/api/posts/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error deleting post ${id}:`, error);
    throw error;
  }
};
