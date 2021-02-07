# Fizz Buzz

# Print numbers 1 to 100.
# Multiples of 3 replaced by "Fizz".
# Multiples of 5 replaced by Buzz.
# Multiles of 15 replaced by FizzBuzz

for j in range(100):
    i = j+1
    if i%15 == 0:
        p = "FizzBuzz"
    elif i%3 == 0:
        p = "Fizz"
    elif i%5 == 0:
        p = "Buzz"
    else:
        p = i
    if i == 100:
        print (p)
    else:
        print (p, end=", ")





