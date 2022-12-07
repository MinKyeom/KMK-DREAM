<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page import="java.util.Date" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>top.jsp</title>
</head>
<body>
<%
Date nowTime = new Date();
%>
top.jsp입니다.<p>
현재 날짜와 시간은 <%= nowTime %> 입니다.
<hr>
</body>
</html>