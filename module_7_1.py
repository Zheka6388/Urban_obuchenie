class Product:

    def __init__(self, name, weight, category):
        self.name = name # название продукта (str)
        self.weight = weight #  общий вес товара (float)
        self.category = category # категория товара (str)

    def __str__(self): # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        prod_ = str(f"{self.name}, {self.weight}, {self.category}")
        return prod_

class Shop:
    
    def __init__(self): # Инкапсулированный атрибут
        self.__file_name = 'products.txt'

    def get_products(self): # Метод get_products(self), который считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name
        file = open(self.__file_name, 'r') # открыть 'products.txt' в режиме чтения
        name_prod = file.read() # Функция read() используется для чтения содержимого файла после открытия его в режиме
        # чтения (r).
        file.close() # закрыть файл products.txt
        return name_prod # возвращение работы метода self.get_products()

    def add(self, *products): # метод принимает неограниченное количество объектов класса Product и
        # добавляет отсутствующие в файл products.txt (self.__file_name)

        for product in products: # цикл перебора наименований product в products
            if str(product) not in self.get_products(): # если строки product нет в списке products.txt
                file = open('products.txt', 'a+') # открыть файл products.txt в режиме «a+» (открывает файл на чтение
                # и запись, но в отличие от режима «w+», он добавляет данные в конец файла, не удаляя существующие.
                # Если файл не существует, он будет создан.)
                file.write(f'{str(product)}\n') # добавить отсутствующий product в файл products.txt со спец. символом
                # перехода на следующую строку в конце - '\n'.
                file.close() # закрыть файл products.txt
            else: # иначе (когда запись product есть в файле products.txt)
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

