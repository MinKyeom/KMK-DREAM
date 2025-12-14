// src/providers/AuthProvider.jsx
"use client";

import React, { createContext, useContext, useState, useEffect } from 'react';
import { getAuthUser, logoutUser } from '../services/api/auth'; // logoutUser 임포트 추가

// 1. Context 생성
const AuthContext = createContext();

// 2. Custom Hook
export const useAuth = () => useContext(AuthContext);

// 3. Provider 컴포넌트
export const AuthProvider = ({ children }) => {
  // ⭐ [수정] 초기 상태를 안전한 값으로 설정 (서버 렌더링 시 UI 불일치 방지)
  const [authState, setAuthState] = useState({
    isAuthenticated: false, 
    id: null, 
    nickname: null 
  });
  const [isAuthInitialized, setIsAuthInitialized] = useState(false); // 초기화 상태 추가

  // ⭐ [수정] 컴포넌트가 클라이언트에서 마운트된 후 (Hydration 후) 상태를 초기화
  useEffect(() => {
    // getAuthUser()는 localStorage에 접근하므로, 반드시 클라이언트 환경에서 실행
    setAuthState(getAuthUser());
    setIsAuthInitialized(true);
  }, []);

  // 인증 상태를 수동으로 새로고침하는 함수
  const refreshAuth = () => {
    // auth.js에서 최신 정보를 가져와 상태 업데이트
    setAuthState(getAuthUser());
  };

  // Context 값
  const contextValue = {
    ...authState, // isAuthenticated, id, nickname 포함
    refreshAuth,
    isAuthInitialized // ⭐ [추가] 인증 상태 초기화 여부 제공
  };

  // isAuthInitialized를 확인하여 초기화가 완료되기 전까지는 로딩 상태를 보여줄 수 있음
  // (여기서는 간단하게, 초기화가 안 되어도 자식 컴포넌트 렌더링을 허용)
  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};