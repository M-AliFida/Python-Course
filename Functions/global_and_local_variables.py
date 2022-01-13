n1 = 1
def function_one():
    n1 = 2  
    print("n1 (local) :", n1) 
    print("n1 (local) ID:", id(n1)) 

print("n1 (global):", n1) # n1 (global): 1 

function_one()  # n1 (local): 2
                # n1 (local) ID: 4509090064

print("n1 (global):", n1)  # n1 (global): 1

print("n1 (global) ID:", id(n1)) # n1 (global) ID: 4509090032