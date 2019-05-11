def h1_result(f):
    def wrapper():
        res = f()
        return "<h1>" + res + ":</h1>"
    return wrapper

@h1_result
def my_function():
    return "Следите за руками"

print(my_function())