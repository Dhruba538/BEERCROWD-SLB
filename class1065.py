even_count = 0

for _ in range(5):
    value = int(input())
    if value % 2 == 0:
        even_count += 1

print(f"{even_count} valores pares")
