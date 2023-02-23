#예외처리1
#a=int(input("숫자를 입력하시오:"))

#print("반지름",a)
#print("원의 넓이",a*a*3.14) #이럴경우 정수가 아닌 경우에 오류 발생!

#조건문으로 예외처리

#b=input("숫자를 입력하시오:")
#if b.isdigit(): # isdigit의 경우 실수,소수도 모두 . 이 들어가서 문자로 취급한다!
#    b=int(b)
#    print(b)

#else:
#    print("다시 입력해주세요")

#print(b.isdigit())

#try exept 구문

#try:
#    c=int(input("정수를 입력하시오:"))

#    print(c)

#except:
#    print("다시 입력해주세요")

#try except _2

list_1=["52","273","32","사과"]

list_num=[]

for item in list_1:
    try:
        float(item)
        list_num.append(item)
    except:
        pass

print(list_1)
print()
print(list_num)

#try except else

#try:
#    d=int(input("정수를 입력하세요"))
#except:
    #print("정수를 다시 입력하세요")

#else:
#    print(d)


# finally

"""try:
    e=int(input("정수를 입력하세요~!"))

except:
    print("다시 입력 부탁드립니다.")

else:
    print(e)
finally:
    print("일단 종료합니다.")"""


#파일이 제대로 닫혔는지 확인하기

"""try:
    file=open("info.txt","w")
    file.close()
except Exception as e:
    print(e)

print(file.closed)"""

# 파일 중간에 예외 발생

try:
    file=open("info.txt","w")
    예외.발생구문()
    file.close

except Exception as e:
    print(e)

file.close()
print(file.closed)