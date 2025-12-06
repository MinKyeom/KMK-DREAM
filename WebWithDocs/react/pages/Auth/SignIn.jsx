// src/pages/Auth/SignIn.jsx

import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser } from "../../api/auth";

export default function SignIn() {
  const [username, setUsername] = useState(""); // 백엔드는 username을 사용 (프론트에서는 이메일로 사용)
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // API 호출: username과 password 전달
      await loginUser({ username, password });
      alert(`로그인 성공!`);
      navigate("/"); // 홈으로 이동
      window.location.reload(); // 헤더 상태 업데이트를 위해 페이지 새로고침
    } catch (error) {
      const message =
        error.response?.data?.error ||
        "로그인 실패: 아이디 또는 비밀번호를 확인해주세요.";
      alert(message);
    }
  };

  return (
    <div
      style={{
        maxWidth: "400px",
        margin: "50px auto",
        padding: "30px",
        backgroundColor: "var(--color-primary)",
        border: "1px solid var(--color-border)",
        borderRadius: "8px",
      }}
    >
      <h2
        style={{
          color: "var(--color-text-main)",
          marginBottom: "20px",
          borderBottom: "1px solid var(--color-border)",
          paddingBottom: "10px",
        }}
      >
        로그인
      </h2>
      <form
        onSubmit={handleSubmit}
        style={{ display: "flex", flexDirection: "column", gap: "15px" }}
      >
        <input
          type="text"
          placeholder="아이디(이메일)"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={{
            padding: "10px",
            border: "1px solid var(--color-border)",
            borderRadius: "4px",
          }}
        />
        <input
          type="password"
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{
            padding: "10px",
            border: "1px solid var(--color-border)",
            borderRadius: "4px",
          }}
        />
        <button
          type="submit"
          className="btn-primary"
          style={{ marginTop: "15px" }}
        >
          로그인
        </button>
      </form>
      <div
        style={{ marginTop: "20px", textAlign: "center", fontSize: "0.9em" }}
      >
        <Link to="/signup" style={{ color: "var(--color-accent)" }}>
          회원가입
        </Link>
      </div>
    </div>
  );
}
