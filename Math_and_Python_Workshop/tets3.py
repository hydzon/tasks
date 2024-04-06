def compress(inp_str):
    result = []
    current_later = inp_str[0]
    count_later = 1
    for i in range(1, len(inp_str)):
        if inp_str[i] == current_later or inp_str[i] == current_later.upper():
            count_later += 1
        else:
            result.append(f'{current_later}{count_later}')
            current_later = inp_str[i]
            count_later = 1
    result.append(f'{current_later}{count_later}')
    result = ''.join(result)
    return result if len(result) < len(inp_str) else inp_str


def test1():
    assert compress('aaaaAAabbcccccccc') == 'a7b2c8'


def test2():
    assert compress('abcd') == 'abcd'
