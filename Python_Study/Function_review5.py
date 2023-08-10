#제네레이터 함수

def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("a지점 통과")
test()

print("b지점 통과")
test()
print(test())

#제네레이터 객체와 next()함수

def test_2():
    print("a지점 통과")
    yield 1
    print("b지점 통과")
    yield 2
    print("C지점 통과")

output=test_2()

print("D지점 통과")
a=next(output)
print(a)
b=next(output)
print(b)
c=next(output)
print(c)
