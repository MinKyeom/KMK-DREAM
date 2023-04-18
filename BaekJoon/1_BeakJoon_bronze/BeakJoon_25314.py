n=int(input())
a=int(n/4)
if n%4==0:
    print("long "*(a)+"int")

elif not n%4==0:
    print("long " * (a + 1) + "int")
