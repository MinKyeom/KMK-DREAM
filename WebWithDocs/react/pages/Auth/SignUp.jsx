// src/pages/Auth/SignUp.jsx

import { useState } from "react";
import SignupForm from "../../components/SignupForm.jsx";
import "../../components/Signup.css";
// ⭐ 수정: 로컬 상태 대신 전역 ThemeContext 훅 사용
import { useTheme } from "../../context/ThemeContext.jsx"; 

export default function SignUp() {
  // ⭐ 수정: 로컬 상태 제거, useTheme 훅 사용
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <div className={`signup-page ${isDarkMode ? "dark" : ""}`}>
      <div className="signup-container">
        <h1 className="signup-title">React Blog (회원가입)</h1>
        <SignupForm />

        {/* 라이트/다크 모드 토글 버튼 (전역 테마 토글 함수 사용) */}
        <button className="mode-toggle" onClick={toggleTheme}>
          {isDarkMode ? "라이트 모드 전환" : "다크 모드 전환"}
        </button>
      </div>
    </div>
  );
}