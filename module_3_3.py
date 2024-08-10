def print_params(a=1, b='string', c=True):
    print(a, b, c)

print("Вызов без аргументов")
print_params()

print("Вызов с одним аргументом")
print_params(b=25)

print("Вызов с другим аргументом")
print_params(c=[1, 2, 3])

# Создаём список из трех элементов разных типов.
values_list = [42, 'hello', False]

# Создаём словарь с тремя ключами, соответствующими параметрам функции print_params.
values_dict = {'a': 99, 'b': 'world', 'c': True}

print("Передаём Values_list и Values_dict в функцию print_params, используя распаковку параметров.")
print_params(*values_list)
print_params(**values_dict)

# Создаём список с двумя элементами разных типов
values_list_2 = [54.32, 'String']

print("Проверяем, работает ли print_params(*values_list_2, 42)")
print_params(*values_list_2, 42)

def print_params(a=1, b='string', c=True):
    print(a, b, c)

print("Часть 1: Функция с параметрами по умолчанию")
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print("Часть 2: Распаковка параметров")
values_list = [42, 'hello', False]
values_dict = {'a': 99, 'b': 'world', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print("Часть 3. Распаковка отдельных параметров")
values_list_2 = [54.32, 'String']
print_params(*values_list_2, 42)

