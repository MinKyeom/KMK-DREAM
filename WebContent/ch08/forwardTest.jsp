<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
    <% request.setCharacterEncoding("utf-8"); %>
    포위딩하는 페이지 forwardTest.jsp로 절대 표시되지 않습니다.<br>
    
    <jsp:forward page="forwardToTest.jsp"/>
    
    forwardTest.jsp 페이지의 나머지 부분으로 표시도 실행도 되지 않습니다.
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>
