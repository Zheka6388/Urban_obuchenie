class WordsFinder: # Объект этого класса должен принимать при создании неограниченного количество
    # названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self): # подготовительный метод, считывает содержимое файлов self.file_names и
        # возвращает словарь с ключом названия файла и значением списка всех слов в файле
        all_words = {} # пустой словарь all_words
        for file_name in self.file_names:
            list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line_cls = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace(
                        '?', '').replace(';', '').replace(':', '').replace('-', '').split()
                    list.append(line_cls)
                all_words[file_name] = sum(list, [])
                return all_words

    def find(self, word): # метод, где word - искомое слово.Возвращает словарь, где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла.
        find_dict = {}
        for name, words in self.get_all_words().items():
           find_dict[name] = words.index(word.lower()) + 1
        return find_dict

    def count(self, word): # метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        # значение - количество слова word в списке слов этого файла.
        count_dict = {}
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word.lower())
        return count_dict



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder3 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))
