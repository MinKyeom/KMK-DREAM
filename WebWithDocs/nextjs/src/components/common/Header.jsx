// src/components/common/Header.jsx
"use client"; 

import Link from "next/link";
import { useState } from "react"; // 🌟 햄버거 토글 상태 추가
import { logoutUser } from "../../services/api/auth";
import { useAuth } from "../../providers/AuthProvider";
import { useToast } from "../../hooks/useToast"; 
import Sidebar from "./Sidebar"; // 🌟 Sidebar 컴포넌트 임포트
import HeaderThemeToggle from "./HeaderThemeToggle"; 
import "../../styles/Header.css"; // 🌟 Header.css 임포트

export default function Header() {
  const { isAuthenticated, nickname, refreshAuth } = useAuth();
  const { showToast } = useToast(); 
  
  // 🌟 햄버거 메뉴 상태 관리
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const handleLogout = async () => {
    try {
      await logoutUser();
      showToast({ message: "로그아웃 성공.", type: "success" }); // 🌟 한국어 우선
      refreshAuth();
    } catch (error) {
      showToast({ message: "로그아웃 실패: 서버 오류 발생.", type: "error" }); // 🌟 한국어 우선
      console.error(error);
      refreshAuth(); 
    }
  };

  return (
    <>
      {/* 🌟 햄버거 토글로 열리는 사이드바 */}
      <Sidebar 
          isSidebarOpen={isSidebarOpen} 
          closeSidebar={() => setIsSidebarOpen(false)} 
      />

      <header>
        <div className="header-content">
          <div className="header-left">
            {/* 🌟 햄버거 버튼 (모바일에서만 표시) */}
            <button 
                className="hamburger-button"
                onClick={() => setIsSidebarOpen(true)}
                aria-label="메뉴 열기"
            >
                ☰
            </button>

            {/* 🌟 로고 (회색/검정 테마 반응형) */}
            <Link href="/" className="logo-text">
              MinKowski
            </Link>

            {/* 🌟 HeaderThemeToggle을 여기에 위치 (모바일에서 자동으로 햄버거 메뉴 옆으로 이동) */}
            <HeaderThemeToggle />
          </div>

          {/* 데스크톱용 내비게이션 (모바일에서 숨김) */}
          <nav className="header-nav">
            <Link href="/post" className="nav-link">
              포스트 목록
            </Link>
            {isAuthenticated && ( 
              <Link href="/write" className="nav-link btn-secondary-small">
                글쓰기 ✍️
              </Link>
            )}

            {isAuthenticated ? (
              <>
                <span className="user-nickname">{nickname}님</span>
                <button
                  onClick={handleLogout}
                  className="nav-link btn-primary-small"
                >
                  로그아웃
                </button>
              </>
            ) : (
              // 비로그인 사용자
              <>
                <Link href="/signin" className="nav-link btn-primary-small">
                  로그인
                </Link>
                <Link href="/signup" className="nav-link btn-secondary-small">
                  회원가입
                </Link>
              </>
            )}
          </nav>
        </div>
      </header>
    </>
  );
}