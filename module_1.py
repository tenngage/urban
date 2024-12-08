grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_dict = {}

students = sorted(tuple(students))

for i in range(len(students)):
    avg = sum(grades[i]) / len(grades[i])
    my_dict[students[i]] = avg

print(my_dict)
