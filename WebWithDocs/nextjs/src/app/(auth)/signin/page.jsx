// app/(auth)/signin/page.jsx
// Next.js Signin Page (Server Component Wrapper)

import Link from "next/link";
import SignInForm from "../../../src/components/Auth/SignInForm"; // 새로 분리된 Client Component 임포트
import "../../../src/components/Auth/Signup.css"; // Auth Page 스타일 임포트

// ⭐ SEO 최적화: Server Component에서 고유 메타데이터 정의
export const metadata = {
  title: "로그인",
  description: "Dev Blog에 로그인하여 글 작성 및 다양한 기능을 사용하세요.",
  alternates: {
    canonical: "[https://your-blog-url.com/signin](https://your-blog-url.com/signin)",
  },
};

export default function SignInPage() {
  return (
    <div className="auth-page">
      <div className="auth-container">
        <h1 className="auth-title">로그인</h1>

        {/* ⭐ Client Component인 SignInForm을 Server Component Wrapper에서 렌더링 */}
        <SignInForm />

        <div className="auth-link">
          계정이 없으신가요? <Link href="/signup">회원가입</Link>
        </div>
      </div>
    </div>
  );
}