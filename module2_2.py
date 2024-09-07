first = int(input('Введите первое число '))#123 ; 42
second= int(input('Введите второе число '))#456 ; 69
third = int(input('Введите третье число '))#789 ; 42
if first == third == second:
    print(3)
elif first == second or second== third or first == third:
    print(2)
else:
    print(0)
