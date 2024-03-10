import random


# # Выведите на печать вероятность в процентах выпадения ровно m решек при броске n монет,
# # округлив до 1 знака после запятой. C помощью метода Монте-Карло.
# n = 5
# m = 5
# c = 1000000
# s = 0
# for _ in range(c):
#     if sum([randint(0, 1) for _ in range(n)]) == m:
#         s += 1
# print(f'{round(s/c * 100, 2)} %')


# # Брошено N игральных костей с M гранями (см. разминочную задачу). Какова вероятность выпадения ровно K очков в сумме?
# n, m, k = 3, 4, 8
# c = 500000
# s = 0
# for _ in range(c):
#     if sum([randint(1, m) for _ in range(n)]) == k:
#         s += 1
# print(f'{round(s/c * 100, 1)} %')


# # Лента длиной L сантиметров разрезается на N кусков в случайных местах (т.е. делают N-1 разрез).
# # Найдите вероятность того, что один из кусков имеет длину не менее M сантиметров.
#
# l, n, m = 100, 2, 80
# c = 1000000
# s = 0
# for _ in range(c):
#     razrez = [0, l]
#     razrez.extend([random.uniform(0, l) for _ in range(n - 1)])
#     razrez.sort()
#     for i in range(len(razrez) - 1):
#         if razrez[i + 1] - razrez[i] >= m:
#             s += 1
#             break
# print(f'{round(s/c * 100, 1)} %')



