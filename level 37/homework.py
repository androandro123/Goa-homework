numbers = [1,2,3,4,5,6,7,8,9,10]
first_half = numbers[0:5]
second_half = numbers[5:10]
squares = 0
for i in numbers:
    squares = i ** 2
print(first_half)
print(second_half)
print(squares)

temperatures = [72, 68, 75, 70, 78, 74, 71]
print(max(temperatures))
print(min(temperatures))
print(sum(temperatures) // len(temperatures))
above_70 = [x for x in range(10) if x > 70]
print(above_70)
