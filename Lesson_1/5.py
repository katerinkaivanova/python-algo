#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letter_one, letter_two = input('Введитe две строчные латинские буквы через пробел: ').split()

ascii_start = 96
abc_pos_one = ord(letter_one) - ascii_start
abc_pos_two = ord(letter_two) - ascii_start
diff = abs(abc_pos_one - abc_pos_two) - 1

print(f'Буква: {letter_one}, позиция в алфавите: {abc_pos_one}')
print(f'Буква: {letter_two}, позиция в алфавите: {abc_pos_two}')
print(f'Количество букв между ними: {diff}')
