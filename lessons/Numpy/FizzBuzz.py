lst = range(1, 101)
new_lst = ["FB" if i % 3 == 0 and i % 5 == 0 else "F" if i % 3 == 0 else "B" if i % 5 == 0 else i for i in lst]

print(new_lst)