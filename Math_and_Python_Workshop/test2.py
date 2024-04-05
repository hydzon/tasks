import sys

def sum_big_numb(n1: str, n2: str):
    res_substring = ''
    perenos = 0
    for i in range(1, len(n2) + 1):
        sum = int(n1[-i]) + int(n2[-i]) + perenos
        perenos = sum // 10
        if perenos:
            res_substring += str(sum % 10)
        else:
            res_substring += str(sum)

    if perenos and len(n1) == len(n2):
        res_substring += str(perenos)
    else:
        if perenos:
            res_substring += str(int(n1[len(n1) - len(n2) - 1]) + perenos)
        else:
            res_substring += n1[len(n1) - len(n2) - 1]

    return res_substring[::-1]


n1, n2 = '123789999999999999999999999999999999999999999999999999', '1'
res_substring = ''
if len(n1) > len(n2):
    i = 1
    perenos = 0
    while i:
        if i < len(n2):
            sum = int(n1[-i]) + int(n2[-i]) + perenos
            perenos = sum // 10
        else:

        if i < len(n1):
            i += 1
        else:
            break

if len(n1) > len(n2):
    res = n1[:len(n1) - len(n2) - 1]
    res = res + sum_big_numb(n1[len(n1) - len(n2) - 1:], n2)
    print(res)
else:
    print(sum_big_numb(n1, n2))

