// src/components/Auth/SignUpForm.jsx
"use client"; 

import { useState } from "react";
import { registerUser } from "../../services/api/auth"; 
import { useRouter } from "next/navigation"; 
import { useAuth } from "../../providers/AuthProvider"; 
import { useToast } from "../../hooks/useToast"; 
import "../../../src/components/Auth/Signup.css"; 

export default function SignupForm() {
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState("");
  const [nickname, setNickname] = useState(""); 
  const [confirmPassword, setConfirmPassword] = useState(""); 
  const [loading, setLoading] = useState(false); 

  const router = useRouter(); 
  const { refreshAuth } = useAuth(); 
  const { showToast } = useToast(); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    // 🌟 UI 텍스트 한국어 우선: 비밀번호가 일치하지 않습니다.
    if (password !== confirmPassword) {
        showToast({ message: "비밀번호가 일치하지 않습니다.", type: "warning" }); 
        setLoading(false);
        return;
    }
    
    try {
      await registerUser({ username, password, nickname });

      // 🌟 UI 텍스트 한국어 우선: 회원가입 성공!
      showToast({ message: "회원가입 성공! 로그인 페이지로 이동합니다.", type: "success" }); 
      router.push("/signin"); 
      refreshAuth(); 
    } catch (error) {
      // 🌟 UI 텍스트 한국어 우선: 회원가입 실패: 중복된 ID 또는 서버 오류.
      showToast({ message: error.message || "회원가입 실패: 중복된 ID 또는 서버 오류.", type: "error" }); 
      console.error(error);
    } finally {
        setLoading(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={handleSubmit}>
      <div className="form-group">
        {/* 🌟 UI 텍스트 한국어 우선: 아이디 */}
        <label>아이디</label>
        <input
          type="text"
          // 🌟 UI 텍스트 한국어 우선: ID를 입력해주세요
          placeholder="ID를 입력해주세요"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          disabled={loading}
        />
      </div>

      <div className="form-group">
        {/* 🌟 UI 텍스트 한국어 우선: 닉네임 */}
        <label>닉네임</label>
        <input
          type="text"
          // 🌟 UI 텍스트 한국어 우선: 블로그에 표시될 닉네임을 입력해주세요
          placeholder="블로그에 표시될 닉네임을 입력해주세요"
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
          required
          disabled={loading}
        />
      </div>
      
      <div className="form-group">
        {/* 🌟 UI 텍스트 한국어 우선: 비밀번호 */}
        <label>비밀번호</label>
        <input
          type="password"
          // 🌟 UI 텍스트 한국어 우선: 비밀번호를 입력해주세요
          placeholder="비밀번호를 입력해주세요"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          disabled={loading}
        />
      </div>

      <div className="form-group">
        {/* 🌟 UI 텍스트 한국어 우선: 비밀번호 확인 */}
        <label>비밀번호 확인</label>
        <input
          type="password"
          // 🌟 UI 텍스트 한국어 우선: 비밀번호를 다시 한번 입력해주세요
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
        disabled={loading}
        style={{ marginTop: '1rem' }}
      >
        {/* 🌟 UI 텍스트 한국어 우선: 회원가입 / 회원가입 중... */}
        {loading ? "회원가입 중..." : "회원가입"}
      </button>
    </form>
  );
}