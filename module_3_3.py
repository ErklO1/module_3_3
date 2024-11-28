def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, "Ряд", 88]
values_dict = {"a": 100, "b": True, "c": 'Диагональ'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [67, "Буква"]

print_params(*values_list_2, 42)