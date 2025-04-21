numbers = list(range(10))
squares = [x**2 for x in numbers if x % 2 == 0]
odd_squares = [x**2 for x in numbers if x % 2 != 0]
combined = squares + odd_squares
print(combined)
