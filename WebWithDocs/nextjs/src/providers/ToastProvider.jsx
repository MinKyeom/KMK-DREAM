// src/providers/ToastProvider.jsx
"use client";

import React, {
  createContext,
  useState,
  useCallback,
  useMemo,
  useEffect, // ⭐ useEffect 임포트
  forwardRef, // ⭐ forwardRef 임포트
} from "react";
import { createPortal } from "react-dom";
import { CSSTransition, TransitionGroup } from "react-transition-group";
import "../styles/Toast.css"; // 토스트 스타일 임포트
// lucide-react 아이콘 임포트 (이전 문제 해결을 위해 포함)
import { Check, X, AlertTriangle, Info } from "lucide-react";

// 1. Context 생성
export const ToastContext = createContext();

// 헬퍼 함수: 토스트 유형에 따른 아이콘 반환
const getIcon = (type) => {
  switch (type) {
    case "success":
      return <Check size={20} />;
    case "error":
      return <X size={20} />;
    case "warning":
      return <AlertTriangle size={20} />;
    case "info":
    default:
      return <Info size={20} />;
  }
};

// 헬퍼 컴포넌트: 단일 토스트 아이템
// ⭐ 수정 1: forwardRef로 컴포넌트를 감싸 ref를 받을 준비
const ToastItem = forwardRef(({ message, type, id, onDismiss }, ref) => {
  // 메시지 유형에 따른 배경색 설정
  const getStyle = (type) => {
    switch (type) {
      case "success":
        return { backgroundColor: "var(--color-success, #28a745)" };
      case "error":
        return { backgroundColor: "var(--color-error, #dc3545)" };
      case "warning":
        return { backgroundColor: "var(--color-warning, #ffc107)" };
      case "info":
      default:
        return { backgroundColor: "var(--color-info, #007bff)" };
    }
  };

  return (
    <div
      // ⭐ 수정 2: forwardRef로 받은 ref를 div에 연결
      ref={ref}
      className={`toast-item ${type}`}
      style={getStyle(type)}
      onClick={() => onDismiss(id)}
    >
      <div className="toast-icon">{getIcon(type)}</div>
      <div className="toast-message">{message}</div>
    </div>
  );
});
ToastItem.displayName = "ToastItem"; // 디버깅을 위해 추가

// 3. Provider 컴포넌트
export const ToastProvider = ({ children }) => {
  const [toasts, setToasts] = useState([]);
  // ⭐ 수정 3: 하이드레이션 오류 방지를 위한 mounted 상태 추가 (Hooks 규칙 준수)
  const [mounted, setMounted] = useState(false);

  // ⭐ 수정 4: 컴포넌트 마운트 시 mounted를 true로 설정 (Hooks 규칙 준수)
  useEffect(() => {
    setMounted(true);
  }, []);

  // 토스트 유형 정의
  const TOAST_TYPES = ["success", "error", "info", "warning"];

  // 새 토스트를 추가하는 함수
  const showToast = useCallback(
    ({ message, type = "info", duration = 3000 }) => {
      const id = Date.now() + Math.random(); // 고유 ID 생성
      const validType = TOAST_TYPES.includes(type) ? type : "info";
      const newToast = { id, message, type: validType };

      // 새로운 토스트를 목록에 추가
      setToasts((prev) => [...prev, newToast]);

      // 일정 시간 후 토스트 제거
      setTimeout(() => {
        setToasts((prev) => prev.filter((toast) => toast.id !== id));
      }, duration);
    },
    []
  );

  // 특정 토스트를 즉시 제거하는 함수 (클릭 시 사용)
  const dismissToast = useCallback((id) => {
    setToasts((prev) => prev.filter((toast) => toast.id !== id));
  }, []);

  const contextValue = useMemo(() => ({ showToast }), [showToast]);

  return (
    <ToastContext.Provider value={contextValue}>
      {children}

      {/* ⭐ 수정 5: mounted 상태일 때만 createPortal 렌더링 (하이드레이션 오류 해결) */}
      {mounted &&
        document.body &&
        createPortal(
          <div className="toast-container">
            <TransitionGroup>
              {toasts.map((toast) => {
                // ⭐ 수정 6: Hook이 아닌 React.createRef()를 사용하여 Hooks 규칙 위반 방지
                const nodeRef = React.createRef();

                return (
                  // CSSTransition을 사용하여 class 기반 애니메이션 적용
                  <CSSTransition
                    key={toast.id}
                    timeout={300} // CSS의 transition 시간과 일치
                    classNames="toast-transition" // CSS 클래스명을 "toast-item"에서 "toast-transition"으로 변경 (일반적인 패턴)
                    nodeRef={nodeRef} // ⭐ nodeRef 전달
                  >
                    <ToastItem
                      toast={toast} // props 변경에 맞춰 다시 전달
                      onDismiss={dismissToast}
                      ref={nodeRef} // ⭐ ToastItem에 ref prop으로 전달
                    />
                  </CSSTransition>
                );
              })}
            </TransitionGroup>
          </div>,
          document.body
        )}
    </ToastContext.Provider>
  );
};
