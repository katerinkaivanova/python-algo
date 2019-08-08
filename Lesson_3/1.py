# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [x for x in range(2, 100)]
b = [x for x in range(2, 10)]

print("В диапазоне чисел [2..99]:")
for divider in b:
    counter = 0
    for dividend in a:
        if dividend % divider == 0:
            counter += 1

    print(f"Количество чисел кратных {divider} равно {counter}")
