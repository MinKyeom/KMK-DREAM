import React from "react";

const Home = () => {
  // 모의 데이터
  const mockPosts = [
    {
      title: "Understanding React Server Components",
      date: "2024-10-12",
      description: "A deep dive into RSC and how it changes the mental model.",
    },
    {
      title: "JavaScript Performance Optimization Tips",
      date: "2024-09-20",
      description: "Practical techniques to optimize your JS code.",
    },
    {
      title: "Building Accessible Forms in React",
      date: "2024-08-15",
      description: "Step-by-step guide to building accessible and user-friendly forms.",
    },
  ];

  // Header 컴포넌트
  const Header = () => (
    <header style={styles.header}>
      <h1 style={styles.logo}>Your Name</h1>
      <nav style={styles.nav}>
        <a href="/blog">Blog</a>
        <a href="/projects">Projects</a>
        <a href="/about">About</a>
      </nav>
    </header>
  );

  // Hero 컴포넌트
  const Hero = () => (
    <section style={styles.hero}>
      <h2 style={styles.heroTitle}>Hi, I'm Your Name 👋</h2>
      <p style={styles.heroSubtitle}>
        I write about React, JavaScript, and software engineering.
      </p>
    </section>
  );

  // PostCard 컴포넌트
  const PostCard = ({ title, date, description }) => (
    <article style={styles.postCard}>
      <h3 style={styles.postTitle}>{title}</h3>
      <p style={styles.postDate}>{date}</p>
      <p style={styles.postDesc}>{description}</p>
    </article>
  );

  // PostList 컴포넌트
  const PostList = () => (
    <section>
      {mockPosts.map((post, i) => (
        <PostCard key={i} {...post} />
      ))}
    </section>
  );

  // Footer 컴포넌트
  const Footer = () => (
    <footer style={styles.footer}>
      <p>© {new Date().getFullYear()} Your Name</p>
      <div style={styles.footerLinks}>
        <a href="https://github.com/yourname">GitHub</a>
        <a href="https://twitter.com/yourname">Twitter</a>
      </div>
    </footer>
  );

  return (
    <div style={styles.container}>
      <Header />
      <Hero />
      <PostList />
      <Footer />
    </div>
  );
};

// 스타일 객체
const styles = {
  container: {
    maxWidth: "760px",
    margin: "0 auto",
    padding: "0 20px",
    fontFamily: "Inter, sans-serif",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    padding: "24px 0",
    borderBottom: "1px solid #eee",
  },
  logo: {
    fontSize: "1.4rem",
    fontWeight: 700,
  },
  nav: {
    display: "flex",
    gap: "20px",
    fontSize: "1rem",
  },
  hero: {
    marginTop: "60px",
    marginBottom: "40px",
  },
  heroTitle: {
    fontSize: "2.6rem",
    fontWeight: 700,
    marginBottom: "10px",
  },
  heroSubtitle: {
    fontSize: "1.2rem",
    color: "#555",
  },
  postCard: {
    padding: "24px 0",
    borderBottom: "1px solid #eee",
  },
  postTitle: {
    fontSize: "1.4rem",
    fontWeight: 700,
    marginBottom: "6px",
  },
  postDate: {
    fontSize: "0.9rem",
    color: "#777",
    marginBottom: "10px",
  },
  postDesc: {
    color: "#444",
    lineHeight: "1.6",
  },
  footer: {
    marginTop: "60px",
    padding: "40px 0",
    borderTop: "1px solid #eee",
    display: "flex",
    justifyContent: "space-between",
    color: "#555",
  },
  footerLinks: {
    display: "flex",
    gap: "16px",
  },
};

export default Home;
