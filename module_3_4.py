def single_root_words(root_word, *other_words): # функция single_root_words, которая принимает
    # одно обязательное слово в параметр root_word, а далее неограниченную последовательность
    # в параметр *other_words.
    same_words = [] #  пустой список same_words, который пополнится нужными словами.
    values = list(other_words) # значения из списка other_words

    for i in range(len(values)): # присвоение i послндовательно значений из списка other_words.

        #if (values[i].lower() in root_word.lower()): # выводится в консоль пустой список
        # первого результата????? ВЫДАЁТ РЕЗУЛЬТАТ ЕСЛИ ТОЛЬКО ЗНАЧЕНИЯ ИЗ *other_words БУДУТ
        # НАХОДИТСЯ ВНУТРИ КОРЕННОГО СЛОВА, ФАКТИЧЕСКИ 'rich' ЯВЛЯЕТСЯ КОРНЕМ ВНУТРИ НЕКОТОРЫХ
        # СЛОВ ИЗ СПИСКА.

        #if (root_word.lower() in values[i].lower()): # выводятся в консоль пустые списки второго и
            # третьего результатов????? И НАОБОРОТ ДЕЙСТВУЕТ К ПРЕДЫДУЩЕМУ ЗАПРОСУ ЦИКЛА.

        if (values[i].lower() in root_word.lower() # если значение из списка other_words (в нижнем
        # регистре) в корневом слове (в нижнем регистре)
        or root_word.lower() in values[i].lower()): # или если корневое слово (в нижнем регистре)
        # в значении из списка other_words (в нижнем регистре)
            same_words.append(values[i]) # тогда это присвоенное к i значение добавить в список same_words

    return (same_words) # возврат значения в список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('Cпутник', "пуТник", "паР", "Спуск")
print(result1)
print(result2)
print(result3)