"""
Напишите программу на Python для подсчета количества символов (частоты символов) в строке.
Пример строки: google.com '
Ожидаемый результат: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

from collections import defaultdict

s = input('Введите выражение: ')
symbol_count = defaultdict(int)

for char in s:
    symbol_count[char] += 1

print(symbol_count)
print(sorted(symbol_count.items()))
