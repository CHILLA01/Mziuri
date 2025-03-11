number = input("შეიყვანეთ მთელი რიცხვი: ")
count = 0
while number:
    count += 1
    number = number[1:]
print("ციფრების რაოდენობა:", count)

if number:
    for digit in number:
        if digit.isdigit():
            print("პირველი ციფრი:", digit)
            break
else:
    print("რიცხვი არ არის შეყვანილი.")





numbers = [5, 12, 3, 19, 45, 23, 9]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("მაქსიმალური რიცხვი არის:", max_number)




def add_numbers(a, b):
    print(a + b)

result = add_numbers(5,3 )
print("შედეგი არის:", result)





def nums_sum(a, b):
    return a + b

result = nums_sum(5, 3)
print("შედეგი არის:", result)







def even_number(number):
    """
    ამოწმებს, არის თუ არა მოცემული რიცხვი ლუწი.
        """
    if number % 2 == 0:
        return True
    else:
        return False

user_input = int(input("Enter a number: "))

if even_number(user_input):
    print("The number is even.")
else:
    print("The number is odd.")











