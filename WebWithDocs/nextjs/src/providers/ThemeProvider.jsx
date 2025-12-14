// src/providers/ThemeProvider.jsx
"use client";

import React, { createContext, useContext, useState, useEffect } from "react";

// 1. Context 생성
const ThemeContext = createContext();

// 2. Custom Hook
export const useTheme = () => useContext(ThemeContext);

// 3. Provider 컴포넌트
export const ThemeProvider = ({ children }) => {
  // ⭐ [수정] 초기 상태를 null로 설정하여, 로컬 스토리지 로딩 전까지는 UI 렌더링을 방지
  const [isDarkMode, setIsDarkMode] = useState(null); 

  // isDarkMode 상태를 토글하는 함수
  const toggleTheme = () => {
    setIsDarkMode(prev => !prev);
  };
  
  // ⭐ [수정] 컴포넌트 마운트 시 (클라이언트 환경에서) 실제 테마 상태를 로드
  useEffect(() => {
    const savedTheme = localStorage.getItem("isDarkMode");
    // 저장된 값이 없으면 기본값인 true (다크 모드) 사용
    setIsDarkMode(savedTheme !== null ? JSON.parse(savedTheme) : true);
  }, []);

  // isDarkMode 상태가 변경될 때마다 localStorage와 body 클래스를 업데이트
  useEffect(() => {
    if (isDarkMode === null) return; // 초기 로딩 중에는 실행하지 않음
    
    const body = document.body;

    // localStorage에 상태 저장
    localStorage.setItem("isDarkMode", JSON.stringify(isDarkMode));

    // body 클래스 토글: 전역 CSS 변수가 이에 반응합니다.
    if (isDarkMode) {
      body.classList.add("dark-mode");
      body.classList.remove("light-mode");
    } else {
      body.classList.add("light-mode");
      body.classList.remove("dark-mode");
    }
  }, [isDarkMode]);

  // ⭐ [수정] isDarkMode가 null인 동안 (클라이언트에서 localStorage를 읽어오는 동안)은 렌더링하지 않음
  // 이는 FOUC(Flash of Unstyled Content)를 방지하는 효과적인 방법입니다.
  if (isDarkMode === null) {
      return null;
  }

  const contextValue = {
    isDarkMode,
    toggleTheme,
  };

  return (
    <ThemeContext.Provider value={contextValue}>
      {children}
    </ThemeContext.Provider>
  );
};