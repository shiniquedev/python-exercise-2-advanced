import math
# Question 1: Multi-Step Arithmetic Operations
a = 5
b = 10
c = 7
a += 3
b *= 2
c %= 4
result = math.sqrt(a**2 + b**2 + c**2)
print("Question 1 result:", round(result, 2))

# Question 2: Complex Conditional Evaluation
x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = int(input("Enter an integer for z: "))
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = is_even and is_positive and is_in_range
print("Question 2 result: ", final_condition)

# Question 3: Grading with Adjustments
score = float(input("Enter your base score: "))
bonus = 5
penalty = -10
score = max(0, min(score, 100))

if score >= 80:
  grade = "A"
elif score >= 70:
   grade = "B"
elif score >= 60:
  grade = "C"
elif score >= 50:
  grade = "D" 
else:
  grade = "F"
print("Final score:", score)  
print("Grade:", grade)

# Question 4: Combining Operators and Conditionals
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation(+, -, *, /, %, **): ")

try:
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  elif operation == "%":
    result = num1 % num2
  elif operation == "**":
    result = num1 ** num2
  else:
    print("Invalid operation!") 
    result = None

  if result is not None:
    print("Result: ", result)

except ZeroDivisionError:
  print("Error: cannot divide or calculate modulus by zero.")