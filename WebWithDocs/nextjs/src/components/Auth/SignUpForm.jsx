// src/components/Auth/SignUpForm.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import { useState } from "react";
import { registerUser } from "../../services/api/auth"; // API 경로 수정
import { useRouter } from "next/navigation"; 
import { useAuth } from "../../providers/AuthProvider"; 
import { useToast } from "../../hooks/useToast"; // ⭐ 추가
import "../../../src/components/Auth/Signup.css"; // 스타일 임포트

export default function SignupForm() {
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState("");
  const [nickname, setNickname] = useState(""); 
  const [confirmPassword, setConfirmPassword] = useState(""); 
  const [loading, setLoading] = useState(false); // 로딩 상태 추가

  const router = useRouter(); 
  const { refreshAuth } = useAuth(); 
  const { showToast } = useToast(); // ⭐ 추가

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    if (password !== confirmPassword) {
        showToast({ message: "비밀번호가 일치하지 않습니다.", type: "warning" }); // ⭐ alert 대체
        setLoading(false);
        return;
    }

    try {
      await registerUser({ username, password, nickname });

      showToast({ message: "회원가입 성공! 자동 로그인되었습니다.", type: "success" }); // ⭐ alert 대체
      router.push("/"); 
      refreshAuth(); 
    } catch (error) {
      showToast({ message: error.message || "회원가입 실패: 서버 오류 또는 ID/닉네임 중복", type: "error" }); // ⭐ alert 대체
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
          placeholder="로그인에 사용할 ID를 입력해주세요"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          disabled={loading}
        />
      </div>
      
      <div className="form-group">
        <label>닉네임</label>
        <input
          type="text"
          placeholder="블로그에 표시될 닉네임을 입력해주세요"
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
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

      <div className="form-group">
        <label>비밀번호 확인</label>
        <input
          type="password"
          placeholder="비밀번호를 다시 한번 입력해주세요"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
          disabled={loading}
        />
      </div>
      
      <button 
        type="submit" 
        className="btn-primary"
        style={{ marginTop: '20px' }}
        disabled={loading || !username || !nickname || !password || !confirmPassword}
      >
        {loading ? "가입 처리 중..." : "회원가입"}
      </button>
    </form>
  );
}