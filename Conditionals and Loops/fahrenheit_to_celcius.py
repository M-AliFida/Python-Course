# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W)
# You need to convert all Fahrenheit values from Start to End at the gap of W into their corresponding Celsius values and print the table.

# Read input as specified in the question
# Print output as specified in the question

# Note : For printing multiple values in one line, put them inside print separated by space.
# You can follow this syntax for printing values of two variables val1 and val2 separated by space - 
# print(val1, " ", val2)


start = int(input())
end = int(input())
step = int(input())

temp = start

while temp <= end:
    c = 5/9 * (temp - 32)
    print(temp, " -> ", int(c))
    temp = temp + step

 # Input: 
 # 5
 # 10
 # 2
 # Output:
 # 5  ->  -15
 # 7  ->  -13
 # 9  ->  -12