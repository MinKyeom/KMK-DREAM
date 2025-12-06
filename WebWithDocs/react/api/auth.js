// src/api/auth.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8080';

/**
 * JWT 토큰을 localStorage에서 가져와 Authorization 헤더를 구성하는 헬퍼 함수
 */
export const getAuthHeaders = () => {
    const token = localStorage.getItem('jwtToken');
    if (!token) return {};
    return {
        // Spring Security의 JWT 설정에 맞춥니다.
        'Authorization': `Bearer ${token}` 
    };
};

/**
 * 현재 로그인된 사용자 정보 (토큰 및 ID)를 가져오는 함수
 */
export const getAuthUser = () => {
    const token = localStorage.getItem('jwtToken');
    const id = localStorage.getItem('currentUserId'); // Post 권한 확인용 ID
    return token ? { isAuthenticated: true, token, id } : { isAuthenticated: false, id: null };
};

/**
 * 로그아웃 (토큰 및 ID 제거)
 */
export const logoutUser = () => {
    localStorage.removeItem('jwtToken');
    localStorage.removeItem('currentUserId');
};


// --- API 호출 함수 ---

/**
 * 회원가입 요청 (POST /user/signup)
 * Front: {email, password} -> Backend DTO: {username, password} 매핑
 */
export const registerUser = async ({ email, password }) => {
    // Front의 email을 Backend의 username으로 매핑하여 전송합니다.
    const response = await axios.post(`${BASE_URL}/user/signup`, {
        username: email, 
        password: password,
        // name 필드는 백엔드 SignupRequest.java에 없으므로 전송하지 않습니다.
    });
    
    // 회원가입 후 UserResponse에서 ID와 토큰 추출 및 저장 (자동 로그인)
    const { id, token } = response.data; 
    if (token && id) {
        localStorage.setItem('jwtToken', token);
        localStorage.setItem('currentUserId', id); 
    }
    return response.data; 
};

/**
 * 로그인 요청 (POST /user/signin)
 */
export const loginUser = async ({ username, password }) => {
    const response = await axios.post(`${BASE_URL}/user/signin`, { username, password }); 
    
    // UserResponse DTO에서 ID와 토큰 추출 및 저장
    const { id, token } = response.data; 
    if (token && id) {
        localStorage.setItem('jwtToken', token);
        localStorage.setItem('currentUserId', id); 
    }
    return response.data;
};