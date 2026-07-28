// src/main.jsx

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./pages/App.jsx";
import { ThemeProvider } from "./context/ThemeContext.jsx";
import { AuthProvider } from "./context/AuthContext.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ThemeProvider>
      {/* ThemeProvider 내부에 AuthProvider 추가 */}
      <AuthProvider> 
        <App />
      </AuthProvider>
    </ThemeProvider>
  </React.StrictMode>
);