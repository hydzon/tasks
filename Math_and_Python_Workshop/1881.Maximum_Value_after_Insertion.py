def maxValue(n, x):
    """
    :type n: str
    :type x: int
    :rtype: str
    """
    if int(n) > 0:
        for i in range(len(n)):
            if int(n[i]) < x:
                n = str(x) + n if i == 0 else n[:i] + str(x) + n[i:]
                return n
    else:
        for i in range(1, len(n)):
            if int(n[i]) > x:
                n = n[:i] + str(x) + n[i:]
                return n
    return n + str(x)


print(maxValue('343367251721', 1))
