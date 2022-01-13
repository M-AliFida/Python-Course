# Function to check prime numbers

def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        return True
    return False

n = int(input())
if is_prime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")

# N = 13
# 13 is prime