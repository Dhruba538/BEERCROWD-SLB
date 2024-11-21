positive_count = 0

for _ in range(6):
    number = float(input())
    if number > 0:
        positive_count += 1

print(f"{positive_count} valores positivos")
