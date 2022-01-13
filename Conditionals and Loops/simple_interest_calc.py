# Simple interest calculator

print("Enter Principal Amount: ")
p = float(input())
print("Enter Time (months): ")
t = float(input())
print("Enter Interest Rate: ")
r = float(input())
interest = (p * t * r) / 100
print(interest)