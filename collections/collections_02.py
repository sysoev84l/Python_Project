"""Создать список произвольного содержания. После каждой операции выводить список на экран
Добавить к нему строку “Hello”.
Удалить первый элемент.
Поменять второй элемент на строку “World”.
Удалить элемент “World”
Вывести на экран перевернутый список"""

my_list = ['boris', 'turecki', 'jonny', 'kirpich', 1, 2, 3, [4, 5, 6]]

print(my_list)
my_list.append('Hello')
print(my_list)

a = my_list.pop(0)
print(a,'\n-------------------------------------\n',my_list)
my_list[1] = 'World'
print(my_list)


new_list = my_list[::-1]
print(my_list)
print(new_list)