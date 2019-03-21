def check_10days_after(a , b): # сначала месяц потом день
    day=b+10
    def days_in_month(month):
        need_change_to_30 = (month > 6 and not (month % 2)) or (month <= 6 and (month % 2))
        if month == 1:
            return 28
        elif need_change_to_30:
            return 30
        else:
            return 31
    if day<=days_in_month(a-1):
        return True
    else:
        return False
    
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
