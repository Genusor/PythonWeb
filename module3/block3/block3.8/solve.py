def solve():
    solution = ""
    for n in range(2000, 3200):
        if n%7==0 and n%5!=0:
            solution = solution + "{0},".format(n)
    solution = solution[:-1]
    return solution

print(solve())