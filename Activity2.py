def recur_factional(n):
    if n == 0:
        return 1
    else:
        return n * recur_factional(n - 1)
    
num = int(input("Enter a number"))

if num < 0:
    print("Sorry, factorial numbers does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factional(num))