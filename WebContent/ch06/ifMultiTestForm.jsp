<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>이름과 전화번호를 입력하는 폼</title>
</head>
<body>
<h2>이름과 전화번호를 입력하세요</h2>
<form method="post" action="ifMultiTestPro.jsp">
<!-- HTML 태그인 <form>태그의 영역이다. <form>태그는 사용자로부터 입력 받기 위한 입력 폼을 작성할 때 사용된다.<form>태그의 
method 속성의 값을 post로 설정하면 입력한 값이 HTTP body를 통해 action 속성의 속성값에 기술된 __.jsp 페이지로 넘겨진다. -->
이름:<input type="text" name="name"><br>
전화번호:
<select name="local">
<option value="서울">서울</option>
<option value="경기">경기<option>
<option value="강원">강원</option>
</select>
-<input type="text" name="tel"><br>
<input type="submit" value="입력완료"></form>

</body>
</html>
