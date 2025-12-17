// src/pages/Auth/SignUp.jsx (새 디자인 적용)

import { Link } from "react-router-dom";
import SignupForm from "../../components/SignupForm.jsx";
import "../../components/Signup.css"; 

export default function SignUp() {
  return (
    <div className="auth-page"> 
      <div className="auth-container"> 
        <h1 className="auth-title">회원가입</h1>
        <SignupForm />
        
        <div className="auth-link">
          이미 계정이 있으신가요? <Link to="/signin">로그인</Link>
        </div>
      </div>
    </div>
  );
}