// src/app/(auth)/signup/page.jsx
// Next.js Signup Page (Server Component)

import Link from "next/link";
import SignupForm from "../../../components/Auth/SignUpForm"; // Client Component
import '../../../components/Auth/Signup.css'; 

// SEO 메타데이터
export const metadata = {
  title: '회원가입 | Dev Blog',
  description: 'Dev Blog에 가입하여 글을 작성하고 챗봇 기능을 사용해보세요.',
  alternates: {
    canonical: '[https://your-blog-url.com/signup](https://your-blog-url.com/signup)',
  },
};

export default function SignUpPage() {
  return (
    <div className="auth-page"> 
      <div className="auth-container"> 
        <h1 className="auth-title">회원가입</h1>
        {/* SignupForm은 Client Component이므로 문제없이 렌더링됩니다. */}
        <SignupForm />
        
        <div className="auth-link">
          이미 계정이 있으신가요? <Link href="/signin">로그인</Link>
        </div>
      </div>
    </div>
  );
}