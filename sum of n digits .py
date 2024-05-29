def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# Test the function
number = int(input("Enter a number to calculate the sum of its digits: "))
print("Sum of digits in", number, "is", sum_of_digits(number))
