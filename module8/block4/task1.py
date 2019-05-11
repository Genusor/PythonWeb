def call_twice(f):
    f()
    f()

def print_thing_up():
    print("thing".upper())

call_twice(print_thing_up)