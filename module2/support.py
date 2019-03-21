from datetime import datetime as dt, timedelta

def check_10days_after(x,y):
    m.month = x
    d.day = y
    d.day = d.day + 10
    d2 = ftd.day
    m2 =ftd.month
    print("Сегодняшнее число ", d1)
    print("Сегодняший месяц",m1)
    print("Через 10 дней будет день ", d2 )
    print("Месяц через 10 дней", m2)

    if m2 < m1:
        z = True
    else:
        z = False
    return z

print(check_10days_after(1, 22))     # 31
print(check_10days_after(2, 19))     # 28
print(check_10days_after(3, 21))     # 31
print(check_10days_after(4, 20))     # 30
print(check_10days_after(5, 21))     # 31
print(check_10days_after(6, 20))     # 30
print(check_10days_after(7, 21))     # 31
print(check_10days_after(8, 21))     # 31
print(check_10days_after(9, 20))     # 30
print(check_10days_after(10, 21))    # 31
print(check_10days_after(11, 20))    # 30
print(check_10days_after(12, 21))    # 31