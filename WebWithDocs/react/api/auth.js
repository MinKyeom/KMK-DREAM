// src/api/auth.js

import axios from "axios";

const BASE_URL = "http://localhost:8080"; // API 기본 URL

// Axios 인스턴스를 생성하여 인증 쿠키가 자동으로 전송되도록 설정
// withCredentials: true를 설정하여 HTTP-only 쿠키를 포함합니다. (보안 강화)
const authAxios = axios.create({
  baseURL: BASE_URL,
  withCredentials: true, // ⭐ HTTP-only 쿠키 전송 활성화
});

/**
 * JWT 토큰을 직접 가져오지 않습니다. (HttpOnly 쿠키 사용 시 불필요)
 */
export const getAuthHeaders = () => {
  return {}; // 더 이상 JWT 토큰을 수동으로 관리하지 않습니다.
};

/**
 * 현재 로그인된 사용자 정보 (ID, 닉네임)를 가져오는 함수
 */
export const getAuthUser = () => {
  // 토큰 대신 ID와 닉네임의 존재 여부로 인증 상태를 간주합니다.
  const id = localStorage.getItem("currentUserId");
  const nickname = localStorage.getItem("currentUserNickname");

  return id && nickname
    ? { isAuthenticated: true, id, nickname }
    : { isAuthenticated: false, id: null, nickname: null };
};

/**
 * 회원가입 요청 (POST /user/signup)
 */
export const registerUser = async ({ username, password, nickname }) => {
  try {
    const response = await authAxios.post(`${BASE_URL}/user/signup`, {
      username,
      password,
      nickname,
    });

    // 서버가 회원가입 후 자동 로그인 처리했다고 가정하고 ID와 닉네임만 저장
    const { id, nickname: userNickname } = response.data;
    if (id && userNickname) {
      localStorage.setItem("currentUserId", id);
      localStorage.setItem("currentUserNickname", userNickname);
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
    const response = await authAxios.post(`${BASE_URL}/user/signin`, {
      username: username,
      password: password,
    });

    // 서버가 로그인 후 HTTP-only 쿠키에 토큰을 설정하고, ID와 닉네임을 응답에 담아준다고 가정합니다.
    const { id, nickname: userNickname } = response.data;
    if (id && userNickname) {
      localStorage.setItem("currentUserId", id);
      localStorage.setItem("currentUserNickname", userNickname);
    }
    return response.data;
  } catch (error) {
    console.error("로그인 오류:", error);
    throw error;
  }
};

/**
 * 로그아웃 요청 (POST /user/logout)
 */
export const logoutUser = async () => {
  try {
    // 서버에 로그아웃 요청 (서버는 HTTP-only 쿠키를 삭제해야 함)
    await authAxios.post(`${BASE_URL}/user/logout`);

    // 로컬 스토리지에서 사용자 정보 삭제
    localStorage.removeItem("currentUserId");
    localStorage.removeItem("currentUserNickname");

    return true;
  } catch (error) {
    // 로그아웃 실패 시에도 로컬 정보는 삭제 (오류 무시)
    localStorage.removeItem("currentUserId");
    localStorage.removeItem("currentUserNickname");
    console.error("로그아웃 오류 (쿠키 만료 실패 가능성):", error);
    return false;
  }
};