mas = [111, 23232, 12,12, 34, 345, 607, 7,345,345,345,345,4358]
n = len(mas)
for i in range(n - 1):
    for j in range(n - i - 1):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1],mas[j]
print(mas)
