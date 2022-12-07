<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%request.setCharacterEncoding("utf-8"); %>
    <%
    int localNum=Integer.parseInt(request.getParameter("localNum"));
    String localName="";
    
    switch(localNum){ //localNum변수의 값은 0~6사이의 값

    	case 0:
    		localName="종로,중구,용산";
    break;
	case 1:
		localName="은평";	
	break;
	case 2:
		localName="도봉";
	break;
	case 3:
		localName="동대문";
	break;
	case 4:
		localName="강동";
	break;
	case 5:
	localName="서초";
	break;
	case 6:
		localName="동작";
	break;
	
	default:
		localName="없는 권역";
		break;
		}
out.println("선택하신 지역은<b>"+localName+"</b>입니다");
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
