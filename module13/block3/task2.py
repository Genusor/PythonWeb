#Классическое решение
# def filter_rare_female_names(names):
#     rare = []
#     for name in names:
#         ya_end = name.endswith("я")
#         a_end = name.endswith("а")
        
#         if not(ya_end) and not(a_end):
#             rare.append(name)
#     return rare


# тоже самое, но почему-то не засчитывает
# def filter_rare_female_names(names):
#     def func2(name):
#         if name[-1] != 'а' and name[-1] != 'я':
#             return True
#     return list(filter(func2, names))


def filter_rare_female_names(names):
    def func2(name):
        ya_end = name.endswith("я")
        a_end = name.endswith("а")
        if not(ya_end) and not(a_end):
            return True
    return list(filter(func2, names))

female_names = ['Аня', 'Маша', 'Света', 'Любовь']
# filter_rare_female_names(female_names) вернёт ['Любовь']
# filter_rare_female_names(["Анна", "Мария"]) вернёт []
# filter_rare_female_names(["Адель"]) вернёт ["Адель"]

print(filter_rare_female_names(female_names))
print(filter_rare_female_names(["Анна", "Мария"]))
print(filter_rare_female_names(["Адель"]))
