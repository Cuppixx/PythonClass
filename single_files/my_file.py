# pylint: skip-file


# My own solution:
my_list = []

def my_func(num):
    my_list.append(num)
    if num == 1: return
    if num % 2 == 0: my_func(num // 2)
    else: my_func(3 * num + 1)

my_func(int(input("Num: ")))
print(f"My solution: {my_list}")


# Prof's solution:
def ergebnisliste(func): return [func(i) for i in range(0,10)]
print(f"My solution: {ergebnisliste(lambda i: i * i)}")
