#1.Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(a = 1, b = 'строка', c = True) #Вывод функции
#print_params() #Также выводит функцию
#print_params(d = 11) #В функции нету d, поэтому выдает ошибку
#print_params(b = 25) # Изменяет параметр b
#print_params(c = [1,2,3]) # Изменяет параметр c


#2.Распаковка параметров
values_list = [3, 'строка', True]
values_dict = {'a' : 10, 'b' : False, 'c': 15.8}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42) # несмотря на то, что пишет а:42, на самом деле он ставится в параметр с
