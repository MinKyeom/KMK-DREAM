// src/services/api/auth.js

import axios from "axios";

// ⭐ [수정] 환경 변수에서 BASE_URL을 가져오도록 수정
// .env.local 파일에 NEXT_PUBLIC_API_URL=http://localhost:8081 와 같이 정의해야 함
const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8081"; // 기본값 설정

// Axios 인스턴스를 생성하여 인증 쿠키가 자동으로 전송되도록 설정
const authAxios = axios.create({
  baseURL: BASE_URL,
  withCredentials: true, // HTTP-only 쿠키 전송 활성화 (필수)
});

/**
 * JWT 토큰을 직접 가져오지 않습니다. (HttpOnly 쿠키 사용 시 불필요)
 */
export const getAuthHeaders = () => {
  return {};
};

/**
 * 현재 로그인된 사용자 정보 (ID, 닉네임)를 가져오는 함수
 */
export const getAuthUser = () => {
  // 토큰 대신 ID와 닉네임의 존재 여부로 인증 상태를 간주합니다.
  // 이 함수는 클라이언트(브라우저) 환경에서만 호출되어야 합니다.
  if (typeof window === 'undefined') {
    return { isAuthenticated: false, id: null, nickname: null };
  }

  const id = localStorage.getItem("currentUserId");
  const nickname = localStorage.getItem("currentUserNickname");

  // 쿠키의 유효성은 서버의 응답을 통해 간접적으로 확인됩니다. 
  // 여기서는 localStorage에 값이 있는 경우 유효하다고 간주합니다.
  return { isAuthenticated: !!id, id, nickname };
};


/**
 * 회원가입 요청 (POST /user/signup)
 */
export const registerUser = async ({ username, password, nickname }) => {
  try {
    const response = await authAxios.post(`${BASE_URL}/user/signup`, {
      username: username,
      password: password,
      nickname: nickname,
    });

    // 백엔드가 HttpOnly 쿠키에 토큰을 설정
    const { id, nickname: userNickname } = response.data;
    if (id && userNickname) {
      // 회원가입 후 자동 로그인 처리 (선택 사항)
      // localStorage.setItem("currentUserId", id);
      // localStorage.setItem("currentUserNickname", userNickname);
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

    // 백엔드가 HttpOnly 쿠키에 토큰을 설정
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
 * 로그아웃 (서버 호출로 HttpOnly 쿠키 삭제)
 */
export const logoutUser = async () => {
  try {
    // 백엔드에 로그아웃 요청을 보내 HttpOnly 쿠키를 삭제하도록 합니다.
    await authAxios.post(`${BASE_URL}/user/logout`);

    // 로컬 스토리지에 저장된 사용자 정보도 삭제
    localStorage.removeItem("currentUserId");
    localStorage.removeItem("currentUserNickname");

    return true;
  } catch (error) {
    console.error("로그아웃 오류:", error);
    throw error;
  }
};