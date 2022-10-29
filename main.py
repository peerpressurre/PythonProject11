def rec(b):
    try:
        counter = 0
        for i in range(1, 10):
            if b / i == 0 or b / b == 0:
                counter += 1
                print(counter)
        if counter == 2:
            print(f'{b} є простим числом')
        else:
            print(f'{b} не є простим числом')
        print(counter)
    except Exception as ex:
        print(f'Error information: {ex}')

rec(3