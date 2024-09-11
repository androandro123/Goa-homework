def even_numbers(list1):
    for num in list1:
        if num % 2 == 0:
            print(num, end=" ")
even_numbers([1,2,3,4,5,6,7,8,9])
list1 = ["roblox","brawl stars","subway surfers"]
list1[0] = "python"
list1[1] ="c++"
list1[2] = "c#"
def greet(name):
    print("hello," + name + ",how are you?")
greet(input("your name:"))