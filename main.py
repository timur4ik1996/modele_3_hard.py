def calculate_structure_sum(data_structure):
    сумма = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            сумма += calculate_structure_sum(len(key))
            сумма += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            сумма += calculate_structure_sum(i)
    elif isinstance(data_structure, int):
        сумма += data_structure
    elif isinstance(data_structure, str):
        сумма += len(data_structure)
    return сумма


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
