# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_pos = int(input('Введите номер буквы латинского алфавита: '))
ascii_start = 96
ascii_pos = ascii_start + letter_pos

print(f'Буква: {chr(ascii_pos)}')
