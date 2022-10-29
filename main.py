def rec(a, b):
    try:
        for i in range(a):
            for j in range(b):
                print('*', end=' ')
            print()
        print()
    except Exception as ex:
        print(f'Error: {ex}')

rec(3,4