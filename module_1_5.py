immutable_var = (15, True, "Urban", ["banana", "coconut"])
print(immutable_var)

# immutable_var[1] = False выдаст ошибку, так как кортежи относятся к неизменяемым типам данных

mutable_list = ["a", 2, "b", "c", 99]
print(mutable_list)
mutable_list[3] = "d"
mutable_list[0] = "e"
print(mutable_list)