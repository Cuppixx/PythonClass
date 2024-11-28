# pylint: skip-file

my_list = []

def my_func(num):
    my_list.append(num)
    if num == 1: return
    if num % 2 == 0: my_func(num // 2)
    else: my_func(3 * num + 1)

# my_func(int(input("Num: ")))
# print(my_list)

def ergebnisliste(func): return [func(i) for i in range(0,10)]
print(ergebnisliste(lambda i: i * i))