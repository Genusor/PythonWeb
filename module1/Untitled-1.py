import random 
course_by = "skillfactory"
i = 0 
while i < 10:
    index = random.randrange(0, len(course_by))
    print(course_by[index])
    i = i + 1