value = float(input())
value_in_cents = int(round(value * 100))  # Convert to cents to avoid floating-point errors

notes = [10000, 5000, 2000, 1000, 500, 200]  # Represented in cents
coins = [100, 50, 25, 10, 5, 1]  # Represented in cents

print("NOTAS:")
for note in notes:
    count = value_in_cents // note
    value_in_cents -= count * note
    print(f"{count} nota(s) de R$ {note / 100:.2f}")

print("MOEDAS:")
for coin in coins:
    count = value_in_cents // coin
    value_in_cents -= count * coin
    print(f"{count} moeda(s) de R$ {coin / 100:.2f}")
