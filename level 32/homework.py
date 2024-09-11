def even_numbers(list1):
    for num in list1:
        if num % 2 == 0:
            print("even")
        if num % 2 != 0:
            print("odd")
even_numbers([1,2,3,4,5,6,7,8,9])
def module(num):
    print(num - num - num)
module(int(input()))