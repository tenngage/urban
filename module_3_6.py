data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    res = 0
    if isinstance(structure, int):
        res += structure
    if isinstance(structure, str):
        res += len(structure)
    if isinstance(structure, (list, tuple, set)):
        for item in structure:
            res += calculate_structure_sum(item)
    if isinstance(structure, dict):
        for key, value in structure.items():
            res += calculate_structure_sum(key)
            res += calculate_structure_sum(value)
    return res

print(calculate_structure_sum(data_structure))
