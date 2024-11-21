salary = float(input())

if salary <= 400.00:
    adjustment_rate = 0.15
elif salary <= 800.00:
    adjustment_rate = 0.12
elif salary <= 1200.00:
    adjustment_rate = 0.10
elif salary <= 2000.00:
    adjustment_rate = 0.07
else:
    adjustment_rate = 0.04

increase = salary * adjustment_rate
new_salary = salary + increase

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {increase:.2f}")
print(f"Em percentual: {adjustment_rate * 100:.0f} %")
