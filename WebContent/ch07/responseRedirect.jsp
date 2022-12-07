<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Reponse 내장객체</title>
</head>
<body>
<h2>Response내장객체-리다이렉트 예제</h2>
현재 페이지는 <b>respnseRedirected.jsp</b>페이지 입니다.

<%
response.sendRedirect("responseRedirected.jsp");
%>

</body>
</html>
