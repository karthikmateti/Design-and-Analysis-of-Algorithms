def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    # Calculate size of the numbers
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    # Split the digit sequences middle
    high_x = x // 10**half
    low_x = x % 10**half
    high_y = y // 10**half
    low_y = y % 10**half
    
    # 3 recursive calls made to numbers half the size
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)
    
    # Combine results using the Karatsuba formula
    return (z2 * 10**(2*half)) + ((z1 - z2 - z0) * 10**half) + z0

num1 = 123456789
num2 = 987654321
result = karatsuba(num1, num2)
print(f"Product of {num1} and {num2} is {result}")
