# Function to print prime numbers, starting from two

def isPrime(n):
    for i in range(2,n):
        if(n % i == 0):
            break
    else:
        return True
    return False

def prime_prime(n):
    for j in range(2, n + 1):
        if(isPrime(j)):
            print(j)

n = int(input())
prime_prime(n)  

# N = 13
# 2
# 3
# 5
# 7
# 11
# 13