# 1. Read the problem out loud
# 2. Making assumptions, ask clarifying questions. (you are establishing good habits)
# 3. Coming up with the approach (drawing pictures) & make sure you don't leave us in the dust, verbalize your thought process)
#     - ideally you can come up with a COUPLE solutions, evaluate the complexities/efficiency/then make your pick
# 4. Write out the code (this should actually take a small amount of time)
# 5. Debug / re-evaluate


#Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number

# loop through a range of 1, to n - range(1, n) - maybe i'll do n +1 to make sure im including the last number
# check if each number is divisible by 3, 5, or 3 & 5 using the %
# i might have to be careful with the order of my conditionals

def fizzbuzz(n):
    # looping through a range of 1 to n
    for num in range(1, n+1):
        # checking if a number is divisible by 3
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 :
            print("Fizz")
        else:
            print(num)

# calling my function
fizzbuzz(30)
        

