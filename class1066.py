# count_values.py

def count_values():
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for _ in range(5):
        value = int(input())
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1

    print(f"{even_count} valor(es) par(es)")
    print(f"{odd_count} valor(es) impar(es)")
    print(f"{positive_count} valor(es) positivo(s)")
    print(f"{negative_count} valor(es) negativo(s)")

count_values()
