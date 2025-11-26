import { useState } from "react";
import axios from "axios";
import "./Signup.css";

export default function SignupForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8080/user/signup", {
        email,
        password,
        name,
      });

      alert("회원가입 성공!");
      console.log(response.data);
    } catch (error) {
      alert("회원가입 실패!");
      console.error(error);
    }
  };

  return (
    <form className="signup-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label>이메일</label>
        <input
          type="email"
          placeholder="이메일을 입력하세요"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
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

      <div className="form-group">
        <label>이름</label>
        <input
          type="text"
          placeholder="이름을 입력하세요"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>

      <button type="submit" className="signup-button">
        회원가입
      </button>
    </form>
  );
}

// // src/components/SignupForm.jsx
// import { useState } from "react";
// import axios from "axios";
// import "./Signup.css";

// export default function SignupForm() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [name, setName] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await axios.post("http://localhost:8080/user/signup", {
//         email,
//         password,
//         name,
//       });

//       alert("회원가입 성공!");
//       console.log(response.data);
//     } catch (error) {
//       alert("회원가입 실패!");
//       console.error(error);
//     }
//   };

//   return (
//     <form className="signup-form" onSubmit={handleSubmit}>
//       <div className="form-group">
//         <label>이메일</label>
//         <input
//           type="email"
//           placeholder="이메일을 입력하세요"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           required
//         />
//       </div>

//       <div className="form-group">
//         <label>비밀번호</label>
//         <input
//           type="password"
//           placeholder="비밀번호를 입력하세요"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           required
//         />
//       </div>

//       <div className="form-group">
//         <label>이름</label>
//         <input
//           type="text"
//           placeholder="이름을 입력하세요"
//           value={name}
//           onChange={(e) => setName(e.target.value)}
//           required
//         />
//       </div>

//       <button type="submit" className="signup-button">
//         회원가입
//       </button>
//     </form>
//   );
// }

// // src/components/SignupForm.jsx
// import { useState } from "react";
// import axios from "axios";
// import "./Signup.css"; // 스타일 적용

// export default function SignupForm() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [name, setName] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await axios.post("http://localhost:8080/user/signup", {
//         email,
//         password,
//         name,
//       });

//       alert("회원가입 성공!");
//       console.log(response.data);
//     } catch (error) {
//       alert("회원가입 실패!");
//       console.error(error);
//     }
//   };

//   return (
//     <form className="signup-form" onSubmit={handleSubmit}>
//       <div className="form-group">
//         <label>이메일</label>
//         <input
//           type="email"
//           placeholder="이메일을 입력하세요"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           required
//         />
//       </div>

//       <div className="form-group">
//         <label>비밀번호</label>
//         <input
//           type="password"
//           placeholder="비밀번호를 입력하세요"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           required
//         />
//       </div>

//       <div className="form-group">
//         <label>이름</label>
//         <input
//           type="text"
//           placeholder="이름을 입력하세요"
//           value={name}
//           onChange={(e) => setName(e.target.value)}
//           required
//         />
//       </div>

//       <button className="signup-button" type="submit">
//         회원가입
//       </button>
//     </form>
//   );
// }

// // src/components/SignupForm.jsx
// import { useState } from "react";
// import axios from "axios";

// export default function SignupForm() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [name, setName] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const response = await axios.post(
//         "http://localhost:8080/user/signup", // Spring Boot 회원가입 API
//         { email, password, name } // DTO에 맞춘 데이터
//       );
//       alert("회원가입 성공!");
//       console.log(response.data);
//     } catch (error) {
//       alert("회원가입 실패!");
//       console.error(error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <div>
//         <label>이메일:</label>
//         <input
//           type="email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           required
//         />
//       </div>

//       <div>
//         <label>비밀번호:</label>
//         <input
//           type="password"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           required
//         />
//       </div>

//       <div>
//         <label>이름:</label>
//         <input
//           type="text"
//           value={name}
//           onChange={(e) => setName(e.target.value)}
//           required
//         />
//       </div>

//       <button type="submit">회원가입</button>
//     </form>
//   );
// }
