# lists
my_dict = {"banana": "fruit", "cucumber": "vegetable"}
print(my_dict)

print(my_dict["banana"])
print(my_dict.get("coconut", "Not found"))

my_dict.update({"strawberry": "berry", "orange": "fruit"})
print(my_dict)

print(my_dict.pop("strawberry"))
print(my_dict)

#sets
my_set = {1, True, 0, 15, "urban"}
print(my_set)

my_set.add(6)
my_set.add("student")
my_set.remove(1)
print(my_set)
