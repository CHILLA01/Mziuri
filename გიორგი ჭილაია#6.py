#1
def is_prime(number):
    if number in [2, 3, 5, 7]:
        print(number)
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        pass
    else:
        print(number)
for num in range(2, 1001):
    is_prime(num)

#2
a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a + b

#3
number = input("შეიყვანეთ მთელი რიცხვი: ")
count = 0
while number:
    count += 1
    number = number[1:]
print("ციფრების რაოდენობა:", count)

#4
number = input("შეიყვანეთ მთელი რიცხვი: ")
sum_of_digits = 0
while number:
    sum_of_digits += int(number[0])
    number = number[1:]
print("ციფრების ჯამი:", sum_of_digits)

#5
number = input("შეიყვანეთ მთელი რიცხვი: ")
if number:
    for digit in number:
        if digit.isdigit():
            print("პირველი ციფრი:", digit)
            break
else:
    print("რიცხვი არ არის შეყვანილი.")
