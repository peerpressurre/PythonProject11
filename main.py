
def max_number(a, b):
    try:
        return max(a, b)
    except Exception as ex:
        print(f'Error information: {ex}')

max_number(3, 6)
res = max_number()
print(res)

