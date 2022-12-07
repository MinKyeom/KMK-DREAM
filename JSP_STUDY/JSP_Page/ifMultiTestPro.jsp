<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <% request.setCharacterEncoding("utf-8"); %>
    
    <%
    String name =request.getParameter("name");
    /*request.getParameter("number")메소드는 이 페이지로 넘어오는 파라미터 변수 중 
    "number 변수를 찾아서 ㄱ그 값을 해당 코드의 경우 name이라는 변수에 넣어준다. 단 해당 변수가 없으면 예외가 발생한다.*/
    String local =request.getParameter("local");
    String tel =request.getParameter("tel");
    String localNum="";
    
    if(local.equals("서울")){ //local변수의 값이 서울일 경우
    	localNum="02";
    out.println("<b>"+name+"</b>님의 전화번호는"
    		+localNum+"-"+tel+"입니다");}
    else if(local.equals("경기")){ //local변수의 값이 서울일 경우
    	localNum="031";
    out.println("<b>"+name+"</b>님의 전화번호는"
    		+localNum+"-"+tel+"입니다");}
    else if(local.equals("강원")){ //local변수의 값이 서울일 경우
    	localNum="033";
    out.println("<b>"+name+"</b>님의 전화번호는"
    		+localNum+"-"+tel+"입니다");
    }
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>
