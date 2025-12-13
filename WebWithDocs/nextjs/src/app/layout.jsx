// app/layout.jsx (Server Component)

import { ThemeProvider } from '../src/providers/ThemeProvider'; // Client Provider 임포트
import { AuthProvider } from '../src/providers/AuthProvider';   // Client Provider 임포트
import { ToastProvider } from '../src/providers/ToastProvider'; // ⭐ 추가: Toast Provider 임포트
import Header from '../src/components/common/Header';           // Client Component 임포트
import Chatbot from '../src/components/Chatbot/Chatbot';        // Client Component 임포트
import { useState } from 'react'; // ChatbotWrapper에서 사용

// 전역 스타일 임포트 (Next.js 권장)
import '../src/styles/globals.css'; 
import '../src/components/Chatbot/Chatbot.css'; // 챗봇 스타일 추가
import '../src/styles/Toast.css'; // ⭐ 추가: Toast 스타일 임포트

// SEO 최상위 메타데이터
export const metadata = {
  title: {
    default: 'Dev Blog | 최신 개발 트렌드와 기술 스택 공유', // 기본 타이틀 개선
    template: '%s | Dev Blog', // 개별 페이지 제목을 감싸는 템플릿
  },
  description: '최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다. 백엔드, 프론트엔드, AI/ML 등 다양한 주제를 다룹니다.', // 설명 상세화
  keywords: ['Next.js', 'Spring Boot', '개발 블로그', '프론트엔드', '백엔드', 'IT 기술', '코딩', 'DevBlog'], // 키워드 추가
  authors: [{ name: 'Your Name or Team Name' }], // 작성자 정보 추가
  alternates: {
    canonical: 'https://your-blog-url.com', // 정규 URL
  },
  // Open Graph/Twitter 카드 설정 (개선)
  openGraph: {
    title: 'Dev Blog | 최신 개발 트렌드와 기술 스택 공유',
    description: '최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다.',
    url: 'https://your-blog-url.com',
    siteName: 'Dev Blog',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Dev Blog',
    description: '최신 개발 트렌드, 기술 스택, 팁을 공유하는 개발자 블로그입니다.',
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

// Client Side Wrapper for Providers and Chatbot State
// Next.js에서 Client Side Provider는 별도의 Client Component로 분리하는 것이 일반적
const ProvidersWrapper = ({ children }) => (
    // ⭐ ToastProvider를 최상위에 추가
    <ToastProvider> 
        <ThemeProvider> 
            <AuthProvider> 
                {children}
            </AuthProvider>
        </ThemeProvider>
    </ToastProvider>
);

// Chatbot 상태 관리를 위한 Client Component (App.jsx의 Chatbot 로직 분리)
const ChatbotWrapper = () => {
    "use client";
    const [isChatOpen, setIsChatOpen] = useState(false);

    const toggleChat = () => {
        setIsChatOpen(prev => !prev);
    };
    
    return (
        <>
            {/* 챗봇 팝업 */}
            {isChatOpen && (
                <Chatbot setIsChatOpen={setIsChatOpen} />
            )}
            
            {/* 챗봇 플로팅 버튼 */}
            <button
                className="chatbot-float-btn btn-primary"
                onClick={toggleChat}
                aria-label={isChatOpen ? "챗봇 닫기" : "챗봇 열기"}
            >
                {isChatOpen ? "×" : "🤖"}
            </button>
        </>
    );
};