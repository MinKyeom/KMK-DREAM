<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
    String id= request.getParameter("id");
    String hobby=request.getParameter("hobby");%>
    
    포위딩되는 페이지 forwardToTest.jsp 입니다.<br>
    <b><%=id %></b> 님의<br>
    취미는 <b><%=hobby %></b> 입니다.
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>
