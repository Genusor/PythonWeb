class SeventenIsOutlawed(Exception):
    pass

def approved_divide(top, bottom):
    if abs(bottom - 17)  < 0.0002:
        raise SeventenIsOutlawed("нельзя делить на 17")
    return top/bottom

print(approved_divide(2, 17))