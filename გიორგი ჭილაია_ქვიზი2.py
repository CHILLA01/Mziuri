#1
for number in range(400, 100, -1):
    if number % 9 == 0:
        print(number)

#2
list = (1, 2, 3, 4, 5)
last_element = list[-1]
print(last_element)

#3
def cube_list(numbers):
    return [number ** 3 for number in numbers]
numbers = [1, 2, 3, 4, 5]
cubed_numbers = cube_list(numbers)
print("რიცხვების კუბები:", cubed_numbers)

#4
def reverse_list(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list

original_list = [1, 2, 3, 4, 5]
reversed_result = reverse_list(original_list)
print("reversed list:", reversed_result)

#5
def favourite_fruit(fruit_list, user_fruit):
    if user_fruit in fruit_list:
        return f"თქვენი საყვარელი ხილი '{user_fruit}' არის ამ სიაში ინდექსით {fruit_list.index(user_fruit)}"
    else:
        return f"'{user_fruit}' თქვენი ხილი სიაში არ არის."
fruits = ['apple', 'banana', 'orange', 'grapes',]
user_fruit = input ("შეიყვანეთ თქვენი საყვარელი ხილი:")
result = favourite_fruit(fruits,user_fruit)
print(result)

#6
def combine_and_sort(odd_list, even_list):
    combined_list = odd_list + even_list
    combined_list.sort()
    return combined_list

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
sorted_list = combine_and_sort(odd_numbers, even_numbers)

print("გაერთიანებული და დალაგებული სია:", sorted_list)

#bonus

#7
""""
ფუნქციის შესაქმნელად გამოიყენება def 
"""""

#8
#მოდულად ვიყენებთ math და ფუნქცია არის pow. მაგალითდ:
import math
result = math.pow(3, 2)
print(result)






fruit1 = input("Enter the first fruit: ")
fruit2 = input("Enter the second fruit: ")
fruit3 = input("Enter the third fruit: ")

fruits = [fruit1, fruit2, fruit3]
fruits.sort()

print(sorted(fruits))