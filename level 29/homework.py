list1 = [6,7,8,9,10,6,7,8,9,10]
list1[0] = 1
list1[1] = 2
list1[2] = 3
list1[3] = 4
list1[4] = 5
print(list1)
print(sum(list1))
for i in list1:
    print(i * i)
nums = 1
for i in list1:
    nums *= i
print(nums)
weight = int(input())
height = float(input())
x = weight / float(height * height)
print(x)
if x < 18.5:
    print('Underweight')
if x >= 18.5 and x < 25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')

