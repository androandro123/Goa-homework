def quarter_of_the_year(a):
    a = int(a)
    if a > 0:
        if a <= 3:
            return "first quarter"
    if a > 3:
        if a <= 6:
            return "second quarter"
    if a > 6:
        if a <= 9:
            return "third quarter"
    if a > 9:
        if a <= 12:
            return "fourth quarter"
    else:
        return "not correct"
print(quarter_of_the_year(int(input("the number of month:"))))
#classwork 2
def paperwork(n,m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
print(paperwork(int(input("numbers of paperwork:")),int(input("numbers of pages:"))))
#classwork 3
def grade_book(mark):
    if 90 <= mark <= 100:
        return "A"
    if 80 <= mark < 90:
        return "B"
    if 70 <= mark < 80:
        return "C"
    if 60 <= mark < 70:
        return "D"
    if mark < 60:
        return "F"
    if mark > 100:
        return "error"
    if mark < 0:
        return "error"
print(grade_book(int(input("your grade:"))))
