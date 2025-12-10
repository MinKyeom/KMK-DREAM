// src/api/posts.js

import axios from "axios";
// import { getAuthHeaders } from "./auth"; // 🚫 수동 헤더 사용 안 함

const POSTS_API_URL = "http://localhost:8080/api/posts";

// Axios 인스턴스를 생성하여 인증 쿠키가 자동으로 전송되도록 설정
const authAxios = axios.create({
  withCredentials: true, // ⭐ HTTP-only 쿠키 전송 활성화
});

// --- 조회 (인증 불필요) ---

/**
 * 전체 글 목록 조회 (GET /api/posts)
 */
export const fetchPosts = async (page = 0, size = 10) => {
  try {
    // 조회는 인증 불필요. axios.get 사용 (헤더 수동 설정 제거)
    const response = await axios.get(POSTS_API_URL, {
      params: { page, size },
      // headers: getAuthHeaders(), // JWT 헤더 수동 포함 불필요 (쿠키 자동 전송)
    });
    return response.data; // Page<Post> 객체
  } catch (error) {
    console.error("Error fetching posts:", error);
    throw error;
  }
};

/**
 * 글 상세 조회 (GET /api/posts/{id})
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
    const response = await authAxios.post(POSTS_API_URL, postRequestData);
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
    const response = await authAxios.put(
      `${POSTS_API_URL}/${id}`,
      postRequestData
    );
    return response.data;
  } catch (error) {
    console.error(`Error updating post with ID ${id}:`, error);
    throw error;
  }
};

/**
 * 글 삭제 (DELETE /api/posts/{id})
 */
export const deletePost = async (id) => {
  // HttpOnly 쿠키가 자동으로 전송됩니다.
  try {
    await authAxios.delete(`${POSTS_API_URL}/${id}`);
    return true;
  } catch (error) {
    console.error(`Error deleting post with ID ${id}:`, error);
    throw error;
  }
};