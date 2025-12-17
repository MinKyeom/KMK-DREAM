// src/services/api/categories-tags.js

import axios from "axios";

// Post 서버의 URL을 환경 변수에서 가져옵니다.
const POSTS_BASE_URL = process.env.NEXT_PUBLIC_POST_API_URL || "http://localhost:8082"; 
const POSTS_API_URL = `${POSTS_BASE_URL}/api/posts`;

/**
 * 카테고리 전체 목록 조회 (GET /api/posts/categories)
 * @returns {Promise<Array<{name: string, slug: string, postCount: number}>>} 카테고리 목록 (개수 포함)
 */
export const fetchCategoriesList = async () => {
  try {
    const response = await axios.get(`${POSTS_API_URL}/categories`);
    // DTO 변경: name, slug 외에 postCount를 포함
    return response.data; 
  } catch (error) {
    console.error("Error fetching categories list:", error);
    throw error;
  }
};

/**
 * 태그 전체 목록 조회 (GET /api/posts/tags)
 * @returns {Promise<Array<{name: string, postCount: number}>>} 태그 목록 (개수 포함)
 */
export const fetchTagsList = async () => {
  try {
    const response = await axios.get(`${POSTS_API_URL}/tags`);
    // DTO 변경: 문자열 배열이 아닌 TagResponse 객체 배열을 반환
    return response.data;
  } catch (error) {
    console.error("Error fetching tags list:", error);
    throw error;
  }
};