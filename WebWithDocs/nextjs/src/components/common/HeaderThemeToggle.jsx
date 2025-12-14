// src/components/common/HeaderThemeToggle.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import { useTheme } from "../../providers/ThemeProvider"; // 경로 수정

// ⭐ 전역 테마 토글 컴포넌트
export default function HeaderThemeToggle() {
  const { isDarkMode, toggleTheme } = useTheme();
  
  return (
    <button 
      onClick={toggleTheme} 
      className="global-theme-toggle"
      title={isDarkMode ? "라이트 모드 전환" : "다크 모드 전환"}
    >
      {/* 감성적인 아이콘 사용 */}
      {isDarkMode ? "☀️" : "🌙"}
    </button>
  );
};