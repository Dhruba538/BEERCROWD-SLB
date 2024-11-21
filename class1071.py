X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

sum_odd = sum(i for i in range(X + 1, Y) if i % 2 != 0)
print(sum_odd)
