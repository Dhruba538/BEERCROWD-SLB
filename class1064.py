# Read 6 values
values = [float(input()) for _ in range(6)]

# Calculate positive values
positive_values = [value for value in values if value > 0]
count_positive = len(positive_values)
average_positive = sum(positive_values) / count_positive

# Print results
print(f"{count_positive} valores positivos")
print(f"{average_positive:.1f}")