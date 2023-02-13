#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def randonLen(n):
    array = list()
    from random import randint 
    for _ in range(n):
        array.append(randint(0, 10))
    return array

a = int(input('Введите число: '))

b = int(input('Введите число: '))


ar1 = randonLen(a)
print(ar1)
ar2 = randonLen(b)
print(ar2)


result = sorted((set(ar1)).intersection(set(ar2)))


print(result)
