// src/index.js (사용되지 않는 경우 삭제해도 되나, 파일은 유지합니다.)

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './pages/App.jsx'; // 확장자 명시
import './index.css'; 
import { ThemeProvider } from './context/ThemeContext.jsx'; // 확장자 명시

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* ThemeProvider로 App 컴포넌트 감싸기 */}
    <ThemeProvider> 
      <App />
    </ThemeProvider>
  </React.StrictMode>
);