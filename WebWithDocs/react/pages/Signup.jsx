import { useState } from "react";
import SignupForm from "../components/SignupForm";
import "../components/Signup.css";

export default function Signup() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={`signup-page ${darkMode ? "dark" : ""}`}>
      <div className="signup-container">
        <h1 className="signup-title">Miky</h1>
        <SignupForm />

        {/* 라이트/다크 모드 토글 버튼 */}
        <button className="mode-toggle" onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "라이트 모드" : "다크 모드"}
        </button>
      </div>
    </div>
  );
}

// // src/pages/Signup.jsx
// import SignupForm from "../components/SignupForm";
// import "../components/Signup.css";

// export default function Signup() {
//   return (
//     <div className="signup-page">
//       <div className="signup-container">
//         <h1 className="signup-title">회원가입</h1>
//         <SignupForm />
//       </div>
//     </div>
//   );
// }
