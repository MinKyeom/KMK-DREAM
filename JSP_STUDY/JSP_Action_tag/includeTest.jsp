<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%request.setCharacterEncoding("utf-8");%>
    <%
    String pageName = request.getParameter("pageName");
    pageName+=".jsp";
    %>
    포함하는 페이지 includeTest.jsp 입니다.<br>
    
    <hr>
    <jsp:include page="<%=pageName%>" flush="false"/>
    includeTest.jsp의 나머지 내용입니다.
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>

</body>
</html>
