// // src/App.jsx
// import SignupForm from "./components/SignupForm";

// function App() {
//   return (
//     <div style={{ maxWidth: "400px", margin: "0 auto", padding: "2rem" }}>
//       <h1>회원가입</h1>
//       <SignupForm />
//     </div>
//   );
// }

// export default App;

// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import SignupForm from "./components/SignupForm";

// function App() {
//   return (
//     <BrowserRouter>
//       <Routes>
//         {/* URL: /user/signup 일 때만 아래 화면 표시 */}
//         <Route
//           path="/user/signup"
//           element={
//             <div
//               style={{ maxWidth: "400px", margin: "0 auto", padding: "2rem" }}
//             >
//               <h1>회원가입</h1>
//               <SignupForm />
//             </div>
//           }
//         />
//       </Routes>
//     </BrowserRouter>
//   );
// }

// export default App;

// src/App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Signup from "./pages/Signup";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/user/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
