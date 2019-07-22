# Классическое решение
# def get_intersection(lhs, rhs):
#     intersect = []
#     for element in rhs:
#         if element in lhs:
#             intersect.append(element)
#     return intersect


def get_intersection(lhs, rhs):
   return list(filter(lambda x: x in lhs,rhs))

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]
female_names = ['Аня', 'Маша', 'Света', 'Любовь', 'Женя', 'Саша']
male_names = ['Миша', 'Саша', 'Валентин', 'Женя', 'Егор']


# get_intersection(a, b) вернёт [2, 3, 5, 7]
# get_intersection(female_names, male_names) вернёт ['Женя', 'Саша']
# get_intersection(female_names, b) вернёт []

print(get_intersection(a, b))
print(get_intersection(female_names, male_names))
print(get_intersection(female_names, b))