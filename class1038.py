# Define the menu with prices
menu = {
    1: 4.00,  # Cachorro Quente
    2: 4.50,  # X-Salada
    3: 5.00,  # X-Bacon
    4: 2.00,  # Torrada simples
    5: 1.50   # Refrigerante
}

# Input: product code and quantity
x, y = map(int, input("").split())

# Calculate total
if x in menu:
    total = menu[x] * y
    print(f"Total: R$ {total:.2f}")
else:
    print("Invalid product code.")