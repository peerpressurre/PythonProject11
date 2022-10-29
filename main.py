def rec(b):
    try:
        factorial = 1

        for i in range(1, b + 1):
            factorial *= i
        print(f'{factorial}')
    except Exception as ex:
        print(f'Error information: {ex}')

rec(10)