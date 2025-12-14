// src/providers/ToastProvider.jsx
"use client";

import React, { createContext, useContext, useState, useCallback, useMemo } from 'react';
import { createPortal } from 'react-dom';
import { CSSTransition, TransitionGroup } from 'react-transition-group';
import "../styles/Toast.css"; // 토스트 스타일 임포트

// 1. Context 생성
export const ToastContext = createContext();

// 헬퍼 컴포넌트: 단일 토스트 아이템
const ToastItem = ({ message, type, id, onDismiss }) => {
    // 메시지 유형에 따른 배경색 설정
    const getStyle = (type) => {
        switch (type) {
            case 'success': return { backgroundColor: 'var(--color-success, #28a745)' };
            case 'error': return { backgroundColor: 'var(--color-error, #dc3545)' };
            case 'warning': return { backgroundColor: 'var(--color-warning, #ffc107)' };
            case 'info':
            default: return { backgroundColor: 'var(--color-info, #007bff)' };
        }
    };
    
    return (
        <div 
            className={`toast-item ${type}`} 
            style={getStyle(type)}
            onClick={() => onDismiss(id)}
        >
            {message}
        </div>
    );
};

// 3. Provider 컴포넌트
export const ToastProvider = ({ children }) => {
    const [toasts, setToasts] = useState([]);
    
    // 토스트 유형 정의
    const TOAST_TYPES = ['success', 'error', 'info', 'warning'];

    // 새 토스트를 추가하는 함수
    const showToast = useCallback(({ message, type = 'info', duration = 3000 }) => {
        const id = Date.now() + Math.random(); // 고유 ID 생성
        const validType = TOAST_TYPES.includes(type) ? type : 'info';
        const newToast = { id, message, type: validType };

        // 새로운 토스트를 목록에 추가
        setToasts((prev) => [...prev, newToast]);

        // 일정 시간 후 토스트 제거
        setTimeout(() => {
            setToasts((prev) => prev.filter(toast => toast.id !== id));
        }, duration);
    }, []);

    // 특정 토스트를 즉시 제거하는 함수 (클릭 시 사용)
    const dismissToast = useCallback((id) => {
        setToasts((prev) => prev.filter(toast => toast.id !== id));
    }, []);

    const contextValue = useMemo(() => ({ showToast }), [showToast]);

    return (
        <ToastContext.Provider value={contextValue}>
            {children}
            
            {/* 토스트를 DOM의 body에 포탈로 렌더링하여 z-index 문제 해결 */}
            {typeof window !== 'undefined' && document.body && createPortal(
                <div className="toast-container">
                    <TransitionGroup>
                        {toasts.map((toast) => (
                            // CSSTransition을 사용하여 class 기반 애니메이션 적용
                            <CSSTransition
                                key={toast.id}
                                timeout={300} // CSS의 transition 시간과 일치
                                classNames="toast-item"
                            >
                                <ToastItem
                                    {...toast}
                                    onDismiss={dismissToast}
                                />
                            </CSSTransition>
                        ))}
                    </TransitionGroup>
                </div>,
                document.body
            )}
        </ToastContext.Provider>
    );
};