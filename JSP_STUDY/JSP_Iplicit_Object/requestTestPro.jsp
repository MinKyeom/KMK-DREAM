<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
    <%
    String num =request.getParameter("num");
    String name =request.getParameter("name");
    String grade =request.getParameter("grade");
    String subject =request.getParameter("subject");
    %>
    <h2>학생정보</h2>
    <table border="1">
    <tr>
    <td widith="150">학번</td>
    <td width="150"><%=num %></td>
    </tr> 
    <tr>
    <td width="150">이름
    <td width="150"><%=name %></table>
    </tr>
        <tr>
    <td width="150">학년
    <td width="150"><%=grade %></table>
    </tr>
        <tr>
    <td width="150">선택과목
    <td width="150"><%=subject %></table>
    </tr>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>
