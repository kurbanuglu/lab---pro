
# Fibonacci Loop and Recursive Functions
# Factorial Loop and Recursive Functions
# Power Loop and Recursive Functions





def FibonacciLoop(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a

result=FibonacciLoop(5)
print(result)


def FibonacciRecursive(n):
    if(n<=3):
        return 1
    else:
        return FibonacciRecursive(n-1)+FibonacciRecursive(n-2)

result_1=FibonacciRecursive(5)
print(result_1)


def FactorialLoop(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

result_2=FactorialLoop(5)
print(result_2)

def FactorialRecursive(n):
    if(n==1):
        return 1
    else:
        return n*FactorialRecursive(n-1)

result_3=FactorialRecursive(5)
print(result_3)


def PowerLoop(a,b):
    s=1
    for i in range(b):
        s=s*a
    return s

result_4=PowerLoop(5,2)
print(result_4)


def PowerRecursive(a,b):
    if(b==0):
        return 1
    elif(b==1):
        return a
    elif(b%2==0):
        return PowerRecursive(a*a,b//2)
    elif(b%2!=0):
        return PowerRecursive(a*a,b//2)*a

result_5=PowerRecursive(5,4)
print(result_5)
