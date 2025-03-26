#Task 1: Calculate Factorial Using a Function 
def c_fact(n):
    f=1
    for i in range(1,n+1):
        f *= i
    print(f)
c_fact(5)
c_fact(6)



import math     
number = float(input("Enter a number: "))

# Perform calculations using the math module
square_root = math.sqrt(number)
natural_logarithm = math.log(number)
sine_value = math.sin(number)
# Display the results
print(f"Square root of {number}: {square_root}")
print(f"Natural logarithm (log base e) of {number}: {natural_logarithm}")
print(f"Sine of {number} (in radians): {sine_value}")
