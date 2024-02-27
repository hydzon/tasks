laters = 'abcdefghijklmnopqrstuvwxyz'
laters_dict = dict()
for i in range(len(laters)):
    laters_dict[laters[i]] = str(i)


def sum_laters(s):
    return int(''.join([laters_dict[ch] for ch in s]))


def isSumEqual(firstWord, secondWord, targetWord):
    return sum_laters(firstWord) + sum_laters(secondWord) == sum_laters(targetWord)


print(isSumEqual(firstWord="j", secondWord="j", targetWord="bi"))
