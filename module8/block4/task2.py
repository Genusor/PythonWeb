# def my_decorator(my_f):
#     def wrapper():
#         print("Я внутри wrapper")
#         my_f()
#         print("Я уже вызвал твою функцию, но ещё внутри wrapper")

#     return wrapper

# def some_function():
#     print("Притворимся, что я тут что-то полезное делаю")

# some_function()
# print("-----")
# decorated = my_decorator(some_function)
# print("*****")
# decorated()

#тоже самое только через декоратор
def my_decorator(my_f):
    def wrapper():
        print("Я внутри wrapper")
        my_f()
        print("Я уже вызвал твою функцию, но еще внутри wrapper")

    return wrapper

@my_decorator
def some_function():
    print("Притворимся, что я тут что-то полезное делаю")

some_function()