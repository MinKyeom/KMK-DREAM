def factorial(n):

    output=1

    for i in range(1,n+1):
        output *=i
    return output

print("factorial(1):",factorial(1))
print("factorial(2):",factorial(2))