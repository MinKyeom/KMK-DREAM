// src/components/Auth/SignInForm.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import { useState } from "react";
import { loginUser } from "../../services/api/auth"; // API 경로 수정
import { useRouter } from "next/navigation";
import { useAuth } from "../../providers/AuthProvider";
import { useToast } from "../../hooks/useToast"; // ⭐ 추가
import "../../../src/components/Auth/Signup.css"; // Auth Page 스타일 임포트

export default function SignInForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false); // 로딩 상태 추가

  const router = useRouter();
  const { refreshAuth } = useAuth();
  const { showToast } = useToast(); // ⭐ 추가

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await loginUser({ username, password });

      showToast({ message: "로그인 성공!", type: "success" }); // ⭐ alert 대체
      router.push("/"); // Next.js 라우터로 페이지 이동
      refreshAuth(); // AuthProvider 상태 갱신
    } catch (error) {
      // 서버에서 인증 오류 등을 반환할 수 있도록
      showToast({ message: error.message || "로그인 실패: ID 또는 비밀번호를 확인해주세요.", type: "error" }); // ⭐ alert 대체
      console.error(error);
    } finally {
        setLoading(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label>아이디</label>
        <input
          type="text"
          placeholder="ID를 입력해주세요"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          disabled={loading}
        />
      </div>

      <div className="form-group">
        <label>비밀번호</label>
        <input
          type="password"
          placeholder="비밀번호를 입력해주세요"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          disabled={loading}
        />
      </div>
      
      <button 
        type="submit" 
        className="btn-primary"
        style={{ marginTop: '20px' }}
        disabled={loading || !username || !password}
      >
        {loading ? "로그인 중..." : "로그인"}
      </button>
    </form>
  );
}