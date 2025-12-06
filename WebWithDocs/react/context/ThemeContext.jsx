// src/context/ThemeContext.jsx

import React, { createContext, useContext, useState, useEffect } from "react";

// 1. Context 생성
const ThemeContext = createContext();

// 2. Custom Hook
export const useTheme = () => useContext(ThemeContext);

// 3. Provider 컴포넌트
export const ThemeProvider = ({ children }) => {
  // 로컬 저장소에서 테마 상태를 불러오거나 기본값(다크 모드)으로 설정
  const [isDarkMode, setIsDarkMode] = useState(() => {
    const savedTheme = localStorage.getItem("isDarkMode");
    // 저장된 값이 없으면 기본값인 true (다크 모드) 사용
    return savedTheme !== null ? JSON.parse(savedTheme) : true;
  });

  // isDarkMode 상태가 변경될 때마다 localStorage와 body 클래스를 업데이트
  useEffect(() => {
    const body = document.body;

    // localStorage에 상태 저장
    localStorage.setItem("isDarkMode", JSON.stringify(isDarkMode));

    // body 클래스 토글
    if (isDarkMode) {
      body.classList.add("dark-mode");
      body.classList.remove("light-mode");
    } else {
      body.classList.add("light-mode");
      body.classList.remove("dark-mode");
    }
  }, [isDarkMode]);

  // 토글 함수
  const toggleTheme = () => {
    setIsDarkMode((prevMode) => !prevMode);
  };

  return (
    <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
