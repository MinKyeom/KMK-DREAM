n=int(input())
for x in range(1,10):
    format_a="{} * {} =".format(n,x)
    print(format_a,n*x)


"""
간단 오답 
"x={} {}".format(a,b)
print(x)
1 2 출력됨  
"""