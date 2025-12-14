// src/components/common/Header.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import Link from "next/link"; // react-router-dom Link 대신 next/link 사용
import { logoutUser } from "../../services/api/auth"; // API 경로 수정
import { useAuth } from "../../providers/AuthProvider"; // Provider 경로 수정
import { useToast } from "../../hooks/useToast"; // ⭐ 추가
import HeaderThemeToggle from "./HeaderThemeToggle";

// 간단한 헤더 컴포넌트
export default function Header() {
  const { isAuthenticated, nickname, refreshAuth } = useAuth();
  const { showToast } = useToast(); // ⭐ 추가

  const handleLogout = async () => {
    try {
      await logoutUser();
      // ⭐ alert() 대신 showToast 사용
      showToast({ message: "로그아웃되었습니다.", type: "success" }); 
      refreshAuth();
    } catch (error) {
      // ⭐ alert() 대신 showToast 사용
      showToast({ message: "로그아웃 처리 중 오류가 발생했습니다.", type: "error" }); 
      console.error(error);
      refreshAuth(); // 혹시 모를 로컬 상태 강제 동기화
    }
  };

  return (
    <header>
      <div className="header-content">
        <div className="header-left">
          {/* 메인 로고/링크 */}
          <Link href="/" className="logo-text">
            DEV BLOG
          </Link>
          <HeaderThemeToggle /> {/* 테마 토글 컴포넌트 추가 */}
        </div>

        <nav className="header-nav">
          {/* 메인 내비게이션 링크 */}
          <Link href="/post" className="nav-link">
            POSTS
          </Link>
          {isAuthenticated && ( // 로그인 사용자에게만 글쓰기 버튼 표시
            <Link href="/write" className="nav-link btn-secondary-small">
              글쓰기 ✍️
            </Link>
          )}

          {isAuthenticated ? (
            <>
              {/* 로그인 사용자 */}
              <span className="user-nickname">{nickname} 님</span>
              <button
                onClick={handleLogout}
                className="nav-link btn-primary-small"
              >
                Logout
              </button>
            </>
          ) : (
            // 비로그인 사용자
            <Link
              href="/signin"
              className="nav-link btn-primary-small"
            >
              로그인
            </Link>
          )}
        </nav>
      </div>
    </header>
  );
}