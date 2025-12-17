// src/pages/Auth/SignIn.jsx (새 디자인 적용)

import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser } from "../../api/auth";
import { useAuth } from "../../context/AuthContext.jsx"; 
import "../../components/Signup.css"; // Auth Page 스타일 임포트

export default function SignIn() {
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { refreshAuth } = useAuth(); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await loginUser({ username, password });
      alert(`로그인 성공!`);
      navigate("/"); 
      refreshAuth(); 
    } catch (error) {
      const message =
        error.response?.data?.error ||
        "로그인 실패: 아이디 또는 비밀번호를 확인해주세요.";
      alert(message);
    }
  };

  return (
    <div className="auth-page"> 
      <div className="auth-container"> 
        <h2 className="auth-title">로그인</h2> 
        <form
          onSubmit={handleSubmit}
          className="auth-form" 
        >
          <div className="form-group">
            <label>아이디</label>
            <input
              type="text"
              placeholder="아이디를 입력하세요"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>비밀번호</label>
            <input
              type="password"
              placeholder="비밀번호를 입력하세요"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          
          <button
            type="submit"
            className="btn-primary"
            style={{ width: "100%", marginTop: "1rem" }}
          >
            로그인
          </button>
        </form>
        
        <div className="auth-link">
            계정이 없으신가요? <Link to="/signup">회원가입</Link>
        </div>
      </div>
    </div>
  );
}