#3-1 이것이 코딩테스트 with python
n= input("넣을 돈을 입력하시오:")
a=int(n)
if a%10==0:

    count=0
    coin_type=[500,100,50,10]

    for coin in coin_type:
        count+=a//coin
        a %= coin
    print(count)
else:
    print("다시 입력하세요")





