def Fibonacci(num):
    a=0
    b=1
    total = 0
    
    for _ in range(num):
        total+=a
        a,b = b,a+b
        
        
    return total


print(Fibonacci(5))    