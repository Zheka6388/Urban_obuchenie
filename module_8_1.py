def add_everything_up(a, b): # будет складывать числа(int, float) и строки(str)
    try: # выполнять стандартные действия.
        return a + b
    except TypeError: # когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление
    # этих двух данных вместе (в том же порядке)
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))