// src/pages/Auth/SignUp.jsx

import { useState } from "react";
// 파일 확장자 변경 확인: SignUpForm.jsx
import SignupForm from "../../components/SignupForm.jsx";
import "../../components/Signup.css";

// 이 컴포넌트는 ThemeContext와 분리된 자체 다크 모드 토글을 가지고 있습니다.
// 이전에 작업했던 ThemeContext와 통합하려면 이 로직을 제거해야 합니다.
// 현재는 주어진 코드를 최대한 유지하고 확장자만 수정합니다.

export default function SignUp() {
  const [darkMode, setDarkMode] = useState(false); // 로컬 다크 모드 상태

  return (
    // signup-page 클래스는 Signup.css에 정의되어 있습니다.
    <div className={`signup-page ${darkMode ? "dark" : ""}`}>
      <div className="signup-container">
        <h1 className="signup-title">React Blog (회원가입)</h1>
        <SignupForm />

        {/* 라이트/다크 모드 토글 버튼 (Signup.css의 스타일을 사용) */}
        <button className="mode-toggle" onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "라이트 모드" : "다크 모드"}
        </button>
      </div>
    </div>
  );
}
