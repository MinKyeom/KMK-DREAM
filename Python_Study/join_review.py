#join 활용법1 #단순 문자열일때
a=["1","2","a","b","c"]
print(a)
result_join="".join(a)
print("join 실행 후:",result_join)

#join 활용법2
#문자열과 숫자가 섞여있는 list의 경우

b=[1,2] # 이 경우 단순히 join 할 경우 오류 발생생
#오류 예시:expected str instance, int found

result_1="".join(map(str,b)) #단순 문자열로 변경 후 join
result_2=int("".join(map(str,b)))

print("result_1 type",type(result_1))
print("result_1",result_1)

print("result_2 type",type(result_2))
print("result_2",result_2)

#Tip:문자와 숫자가 같이 있는 경우 나눠서 join 해야겠다 think