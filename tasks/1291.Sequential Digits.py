"""

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

10 <= low <= high <= 10^9

"""


def sequential_digits(input_number):
    if input_number // 10 > 0:
        if ((input_number % 10 - (input_number // 10) % 10) == 1) and sequential_digits(input_number // 10):
            return True
        else:
            return False
    else:
        return True


low = 1000
high = 130000
sec_digits = [i for i in range(low, high + 1) if sequential_digits(i)]
print(sec_digits)
