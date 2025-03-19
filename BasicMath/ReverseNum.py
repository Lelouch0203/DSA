def reverse(x: int) -> int:
    revNum = 0
    is_negative = x < 0  # Check if the number is negative
    x = abs(x)  # Work with the absolute value

    while x != 0:
        digit = x % 10  # Extract the last digit
        revNum = revNum * 10 + digit  # Append digit to revNum
        x //= 10  # Remove last digit

    # Restore negativity if needed
    if is_negative:
        revNum = -revNum

    # Handle 32-bit integer overflow
    if revNum < -2**31 or revNum > 2**31 - 1:
        return 0

    return revNum


x=-1234
print(reverse(x))