// src/api/auth.js

import axios from "axios";

const BASE_URL = "http://localhost:8080"; // API 기본 URL

/**
 * JWT 토큰을 localStorage에서 가져와 Authorization 헤더를 구성하는 헬퍼 함수
 */
export const getAuthHeaders = () => {
  const token = localStorage.getItem("jwtToken"); // 로컬 스토리지에서 JWT 토큰을 가져옵니다.
  if (!token) return {}; // 토큰이 없으면 빈 객체 반환
  return {
    Authorization: `Bearer ${token}`, // Authorization 헤더에 Bearer 타입으로 토큰 추가
  };
};

/**
 * 현재 로그인된 사용자 정보 (토큰 및 ID)를 가져오는 함수
 */
export const getAuthUser = () => {
  const token = localStorage.getItem("jwtToken"); // 로컬 스토리지에서 JWT 토큰을 가져옵니다.
  const id = localStorage.getItem("currentUserId"); // 로컬 스토리지에서 로그인된 사용자 ID를 가져옵니다.

  // 토큰이 있으면 로그인된 사용자로 간주하고, 해당 토큰과 ID를 반환
  return token
    ? { isAuthenticated: true, token, id }
    : { isAuthenticated: false, id: null };
};

/**
 * 로그아웃 (토큰 및 ID 제거)
 */
export const logoutUser = () => {
  localStorage.removeItem("jwtToken"); // 로컬 스토리지에서 JWT 토큰 제거
  localStorage.removeItem("currentUserId"); // 로컬 스토리지에서 사용자 ID 제거
};

/**
 * 회원가입 요청 (POST /user/signup)
 */
export const registerUser = async ({ email, password }) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/signup`, {
      username: email, // 백엔드에서 요구하는 username 필드에 email을 사용
      password: password,
    });

    // 회원가입 후 UserResponse에서 ID와 토큰 추출 및 저장 (자동 로그인)
    const { id, token } = response.data;
    if (token && id) {
      localStorage.setItem("jwtToken", token); // 토큰을 로컬 스토리지에 저장
      localStorage.setItem("currentUserId", id); // 사용자 ID를 로컬 스토리지에 저장
    }
    return response.data;
  } catch (error) {
    console.error("회원가입 오류:", error);
    throw error;
  }
};

/**
 * 로그인 요청 (POST /user/signin)
 */
export const loginUser = async ({ username, password }) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/signin`, {
      username,
      password,
    });

    // 로그인 후 UserResponse에서 ID와 토큰 추출 및 저장
    const { id, token } = response.data;
    if (token && id) {
      localStorage.setItem("jwtToken", token); // 토큰을 로컬 스토리지에 저장
      localStorage.setItem("currentUserId", id); // 사용자 ID를 로컬 스토리지에 저장
    }
    return response.data;
  } catch (error) {
    console.error("로그인 오류:", error);
    throw error;
  }
};