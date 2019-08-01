# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трёхзначное число: '))

num_one = number // 100
num_two = number // 10 % 10
num_three = number % 10

sum = num_one + num_two + num_three
prod = num_one * num_two * num_three

print(f'Cумма цифр трехзначного числа = {sum}, произведение = {prod}')
