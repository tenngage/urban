def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# print_params(3, 2, 1)
# print_params(2)
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = [151, "string", False]
values_dict = {"a": 14, "b": "urban", "c": True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [131, "строка"]
print_params(*values_list_2)
