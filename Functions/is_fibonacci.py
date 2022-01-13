# Given a number N, figure out if it is a member of fibonacci series or not. 
# Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
# F(n) = F(n-1) + F(n-2)
# Where F(0) = 0 and F(1) = 1

f = 0
s = 1
t = 1

def is_fibonacci(n):
    global f
    global s
    global t
    while t <= n:
      t = f + s
      f = s
      s = t
      if f == n:
        return 1
    pass

n = int(input())
if(is_fibonacci(n)):
    print("true")
else:
    print("false")

# N = 55
# true