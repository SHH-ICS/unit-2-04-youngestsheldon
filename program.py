# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for number in range(1,32):
    if((number % 3 == 0) & (number % 15 != 0)):
      print("Fizz")
    if((number % 5 == 0) & (number % 15 != 0)):
      print("Buzz")
    if(number % 15 == 0):
       print("FizzBuzz")
    if((number % 3 != 0) & (number % 5 != 0)):
       print(number)
