// src/api/posts.js

import axios from 'axios';
import { getAuthHeaders } from './auth'; 

const POSTS_API_URL = 'http://localhost:8080/api/posts'; 

// --- 조회 (인증 불필요) ---

/**
 * 전체 글 목록 조회 (GET /api/posts)
 */
export const fetchPosts = async (page = 0, size = 10) => {
    const response = await axios.get(POSTS_API_URL, {
        params: { page, size }
    });
    return response.data; // Page<Post> 객체
};

/**
 * 글 상세 조회 (GET /api/posts/{id})
 */
export const fetchPostById = async (id) => {
    const response = await axios.get(`${POSTS_API_URL}/${id}`);
    return response.data; // Post 객체
};


// --- CRUD (인증 필수: JWT 헤더 사용) ---

/**
 * 새 글 작성 (POST /api/posts)
 */
export const createPost = async (postRequestData) => {
    const headers = getAuthHeaders();
    if (!headers.Authorization) {
        throw new Error("글 작성을 위해서는 로그인이 필요합니다.");
    }
    // postRequestData는 {title, content, category, tags: string[]} 형태
    const response = await axios.post(POSTS_API_URL, postRequestData, { headers });
    return response.data;
};

/**
 * 글 수정 (PUT /api/posts/{id})
 */
export const updatePost = async (id, postRequestData) => {
    const headers = getAuthHeaders();
    if (!headers.Authorization) {
        throw new Error("글 수정 권한이 없습니다.");
    }
    const response = await axios.put(`${POSTS_API_URL}/${id}`, postRequestData, { headers });
    return response.data;
};

/**
 * 글 삭제 (DELETE /api/posts/{id})
 */
export const deletePost = async (id) => {
    const headers = getAuthHeaders();
    if (!headers.Authorization) {
        throw new Error("글 삭제 권한이 없습니다.");
    }
    await axios.delete(`${POSTS_API_URL}/${id}`, { headers });
    return true;
};