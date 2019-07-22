# Классическое решение
# def give_length(names):
#     lengths = []
#     for name in names:
#         lengths.append(len(name))
#     return lengths


def give_length(names):
      return list(map(len, names))


female_names = ['Аня', 'Маша', 'Света']
male_names = ['Денис', 'Рома', 'Петя']



# give_length(female_names) вернёт [3, 4, 5]
# give_length(male_names) вернёт [5, 4, 4]
# give_length(male_names + female_names) вернёт [3, 4, 5, 5, 4, 4]

print(give_length(female_names))
print(give_length(male_names))
print(give_length(male_names + female_names))