def rec(b):
    try:
        counter = 0
        for i in range(1, b+1):
            if b % i == 0:
                counter += 1

        if counter == 2:
            print(f'{b} є простим числом')
        else:
            print(f'{b} не є простим числом')

    except Exception as ex:
        print(f'Error information: {ex}')


number = int(input("number->"))
rec(number)