my_list = [1, 3, 6, 10]

list_ = [x**2 for x in my_list]

generator = (x**2 for x in my_list)

print(list_)
print(generator)