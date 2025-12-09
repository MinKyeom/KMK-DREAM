// src/main.jsx

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./pages/App.jsx";
import { ThemeProvider } from "./context/ThemeContext.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    {/* 테마 컨텍스트로 앱 전체를 감싸줍니다. */}
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);