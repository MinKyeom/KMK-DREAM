// src/components/SignupForm.jsx

import { useState } from "react";
import { registerUser } from "../api/auth";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx"; 
import "./Signup.css"; 

export default function SignupForm() {
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState("");
  // 닉네임 상태
  const [nickname, setNickname] = useState(""); 
  const [confirmPassword, setConfirmPassword] = useState(""); 

  const navigate = useNavigate();
  const { refreshAuth } = useAuth(); 

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }

    try {
      // 닉네임을 포함하여 API 호출
      await registerUser({ username, password, nickname });

      alert("회원가입 성공! 자동 로그인되었습니다.");
      navigate("/");
      refreshAuth(); 
    } catch (error) {
      // 서버에서 닉네임 중복 오류 등을 반환할 수 있도록 수정
      const message = error.response?.data?.error || "회원가입 실패: 서버 오류";
      alert(message);
      console.error(error);
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
        />
      </div>
      
      <button 
        type="submit" 
        className="btn-primary" 
        style={{ width: "100%", marginTop: "1rem" }}
      >
        회원가입
      </button>
    </form>
  );
}