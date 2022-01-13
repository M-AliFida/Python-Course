# Nth term of fibonacci series F(n) is calculated using following formula -
# F(n) = F(n-1) + F(n-2), 
#  Where, F(1) = F(2) = 1
# Provided N you have to find out the Nth Fibonacci

def Fibonacci(n): 
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return Fibonacci(n - 1) + Fibonacci(n - 2) 
   
n=int(input())
print(Fibonacci(n)) 

# 10
# 55