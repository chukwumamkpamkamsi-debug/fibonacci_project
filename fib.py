a, b = 0, 1
for i in range(1, 101):
    print(f"{i}: {a}")
    a, b = b, a + b