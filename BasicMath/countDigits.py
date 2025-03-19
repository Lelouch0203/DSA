def count_digits(number):
    count = 0
    while number != 0:
        number=number//10
        # TC is log10(N)
        print(number)
        count += 1
    return count

# Example usage
number = 12345
print(f"The number of digits in {number} is {count_digits(number)}")