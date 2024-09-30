
from fake_math import divide as fd # импорт из fake_math функции divide и названием fd (fake divide)
from true_math import divide as td # импорт из true_math функции divide и названием td (true divide)

result1 = fd(69, 3)
result2 = fd(3, 0)
result3 = td(49, 7)
result4 = td(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)