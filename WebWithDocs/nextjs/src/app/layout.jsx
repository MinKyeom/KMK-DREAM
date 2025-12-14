// app/layout.jsx (Server Component)

import { ThemeProvider } from "../providers/ThemeProvider"; // Client Provider 임포트
import { AuthProvider } from "../providers/AuthProvider"; // Client Provider 임포트
import { ToastProvider } from "../providers/ToastProvider"; // ⭐ 추가: Toast Provider 임포트
import Header from "../components/common/Header"; // Client Component 임포트

// ✅ 수정: ChatbotWrapper를 별도 파일에서 임포트합니다.
import ChatbotWrapper from "../components/Chatbot/ChatbotWrapper";

// 전역 스타일 임포트 (Next.js 권장)
import "../styles/globals.css";
// ✅ 오류 해결: '../src/components/Chatbot/Chatbot.css' -> '../components/Chatbot/Chatbot.css'로 경로 수정
import "../components/Chatbot/Chatbot.css"; // 챗봇 스타일 추가
import "../styles/Toast.css"; // ⭐ 추가: Toast 스타일 임포트

// SEO 최상위 메타데이터
export const metadata = {
  title: {
    default: "Dev Blog | 최신 개발 트렌드와 기술 스택 공유", // 기본 타이틀 개선
    template: "%s | Dev Blog", // 개별 페이지 제목을 감싸는 템플릿
  },
  description:
    "최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다. 백엔드, 프론트엔드, AI/ML 등 다양한 주제를 다룹니다.", // 설명 상세화
  keywords: [
    "Next.js",
    "Spring Boot",
    "개발 블로그",
    "프론트엔드",
    "백엔드",
    "IT 기술",
    "코딩",
    "DevBlog",
  ], // 키워드 추가
  authors: [{ name: "Your Name or Team Name" }], // 작성자 정보 추가
  alternates: {
    canonical: "https://your-blog-url.com", // 정규 URL
  },
  // Open Graph/Twitter 카드 설정 (개선)
  openGraph: {
    title: "Dev Blog | 최신 개발 트렌드와 기술 스택 공유",
    description:
      "최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다.",
    url: "https://your-blog-url.com",
    siteName: "Dev Blog",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Dev Blog",
    description:
      "최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다.",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="ko">
      <body>
        {/* 모든 페이지를 Provider로 감싸 전역 상태 사용 가능하도록 함 */}
        <ProvidersWrapper>
          <div className="App">
            <Header /> {/* Client Component */}
            <main>
              {children} {/* Page Content */}
            </main>
            <ChatbotWrapper /> {/* 챗봇 플로팅 버튼 및 팝업 */}
          </div>
        </ProvidersWrapper>
      </body>
    </html>
  );
}

// Client Side Wrapper for Providers
const ProvidersWrapper = ({ children }) => (
  // ⭐ ToastProvider를 최상위에 추가
  <ToastProvider>
    <ThemeProvider>
      <AuthProvider>{children}</AuthProvider>
    </ThemeProvider>
  </ToastProvider>
);

// ❌ 기존 layout.jsx에 있던 ChatbotWrapper 함수는 제거하고 별도 파일로 이동합니다.
