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
#homework 2
def years(humanYears):
    catYears = 0
    dogYears = 0
    if humanYears >= 3:
        catYears = 15 + 9 +(int(humanYears) * 4)
        dogYears = 15 + 9 +(int(humanYears) * 5)
        return catYears,dogYears
    if humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
        return catYears,dogYears
    if humanYears == 1:
        catYears = 15
        dogYears = 15
        return catYears,dogYears
print(years(int(input("humanyears:"))))
#homework 3
def enough_or_not(length,gallon,speed):
    if length / speed < gallon:
        return "not enough"
    if length / speed >= gallon:
        return "enough"
print(enough_or_not(int(input("length:")),int(input("gallon:")),int(input("speed:"))))

