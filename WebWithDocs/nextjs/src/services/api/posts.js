// src/services/api/posts.js

import axios from "axios";
// import { getAuthHeaders } from "./auth"; // 🚫 수동 헤더 사용 안 함

// ⭐ 수정: Post 서버의 API URL로 변경 (8082) -> 환경 변수 사용
const POSTS_BASE_URL = process.env.NEXT_PUBLIC_POST_API_URL || "http://localhost:8082"; 
const POSTS_API_URL = `${POSTS_BASE_URL}/api/posts`;

// Axios 인스턴스를 생성하여 인증 쿠키가 자동으로 전송되도록 설정
// ⭐ 수정: baseURL을 설정하여 각 메서드에서 경로를 간결하게 사용
const authAxios = axios.create({
  baseURL: POSTS_BASE_URL, 
  withCredentials: true, // ⭐ HTTP-only 쿠키 전송 활성화
});

// --- 조회 (인증 불필요) ---

/**
 * 전체 글 목록 조회 (GET /api/posts)
 */
export const fetchPosts = async (page = 0, size = 10) => {
  // Server Component에서도 사용할 수 있도록 axios를 직접 사용
  try {
    // 조회는 인증 불필요. axios.get 사용
    const response = await axios.get(POSTS_API_URL, {
      params: { page, size },
    });
    return response.data; // Page<Post> 객체
  } catch (error) {
    console.error("Error fetching posts:", error);
    throw error;
  }
};

/**
 * 특정 글 조회 (GET /api/posts/{id})
 */
export const fetchPostById = async (id) => {
  try {
    const response = await axios.get(`${POSTS_API_URL}/${id}`);
    return response.data; // Post 객체
  } catch (error) {
    console.error(`Error fetching post with ID ${id}:`, error);
    throw error;
  }
};

// --- CRUD (인증 필수: HTTP-only 쿠키 사용) ---

/**
 * 새 글 작성 (POST /api/posts)
 */
export const createPost = async (postRequestData) => {
  // HttpOnly 쿠키가 자동으로 전송됩니다. (authAxios 사용)
  try {
    // ⭐ 수정: authAxios에 baseURL을 설정했으므로 상대 경로 사용
    const response = await authAxios.post("/api/posts", postRequestData); 
    return response.data;
  } catch (error) {
    console.error("Error creating post:", error);
    throw error;
  }
};

/**
 * 글 수정 (PUT /api/posts/{id})
 */
export const updatePost = async (id, postRequestData) => {
  // HttpOnly 쿠키가 자동으로 전송됩니다.
  try {
    // ⭐ 수정: authAxios에 baseURL을 설정했으므로 상대 경로 사용
    const response = await authAxios.put(
      `/api/posts/${id}`, 
      postRequestData
    );
    return response.data; // 수정된 Post 객체
  } catch (error) {
    console.error(`Error updating post ${id}:`, error);
    throw error;
  }
};

/**
 * 글 삭제 (DELETE /api/posts/{id})
 */
export const deletePost = async (id) => {
  // HttpOnly 쿠키가 자동으로 전송됩니다.
  try {
    // ⭐ 수정: authAxios에 baseURL을 설정했으므로 상대 경로 사용
    const response = await authAxios.delete(`/api/posts/${id}`);
    return response.data; // HTTP 200/204 응답 (반환 값 없을 수 있음)
  } catch (error) {
    console.error(`Error deleting post ${id}:`, error);
    throw error;
  }
};