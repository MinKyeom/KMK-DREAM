// src/context/AuthContext.jsx

import React, { createContext, useContext, useState, useEffect } from 'react';
import { getAuthUser } from '../api/auth'; // auth.js에서 사용자 정보 가져오는 함수

// 1. Context 생성
const AuthContext = createContext();

// 2. Custom Hook
export const useAuth = () => useContext(AuthContext);

// 3. Provider 컴포넌트
export const AuthProvider = ({ children }) => {
  // 초기 상태는 getAuthUser()를 통해 설정
  const [authState, setAuthState] = useState(getAuthUser());

  // 인증 상태를 수동으로 새로고침하는 함수
  const refreshAuth = () => {
    // auth.js에서 최신 정보를 가져와 상태 업데이트
    setAuthState(getAuthUser());
  };
  
  // Context 값
  const contextValue = {
    ...authState, // isAuthenticated, id, nickname 포함
    refreshAuth,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};