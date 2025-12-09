// src/components/SignupForm.jsx

import { useState } from "react";
import { registerUser } from "../api/auth";
import { useNavigate } from "react-router-dom";
import "./Signup.css";

export default function SignupForm() {
  const [email, setEmail] = useState(""); // Backend: username
  const [password, setPassword] = useState("");
  const [name, setName] = useState(""); // UI 전용 (현재 백엔드에서 사용하지 않음)

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // email을 username으로 매핑하여 API 호출
      await registerUser({ email, password });

      alert("회원가입 성공! 자동 로그인되었습니다.");
      navigate("/");
      window.location.reload();
    } catch (error) {
      const message = error.response?.data?.error || "회원가입 실패!";
      alert(message);
      console.error(error);
    }
  };

  return (
    <form className="signup-form" onSubmit={handleSubmit}>
      {" "}
      <div className="form-group">
        {" "}
        <label>이메일 (아이디)</label>{" "}
        <input
          type="email"
          placeholder="이메일을 입력하세요"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />{" "}
      </div>{" "}
      <div className="form-group">
        {" "}
        <label>비밀번호</label>{" "}
        <input
          type="password"
          placeholder="비밀번호를 입력하세요"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />{" "}
      </div>{" "}
      {/* 닉네임/이름 필드는 현재 백엔드 DTO(SignupRequest)에서 사용하지 않으므로, 백엔드 변경이 필요 없는 한 숨기거나 제거하는 것이 좋습니다. */}
      {/* <div className="form-group">
        <label>이름/닉네임</label>
        <input
          type="text"
          placeholder="이름을 입력하세요"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div> */}
      <button type="submit" className="signup-button">
        가입하기
      </button>
    </form>
  );
}