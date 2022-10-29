import math
def cube(b):
    try:
        return math.pow(b, 3)

    except Exception as ex:
        print(f'Error information: {ex}')
res = cube(2)
print(int(res))
