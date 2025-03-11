#1
import math
decimal_number = float(input("Enter a decimal number: "))

rounded_number = round(decimal_number, 1)
print(f"Rounded (round): {rounded_number}")

ceil_number = math.ceil(decimal_number * 10) / 10
print(f"Rounded up (ceil): {ceil_number}")

floor_number = math.floor(decimal_number * 10) / 10
print(f"Rounded down (floor): {floor_number}")

truncated_number = math.trunc(decimal_number * 10) / 10
print(f"Truncated (trunc): {truncated_number}")

#2
result_3_8 = pow(3, 8)
print(f"3⁸ = {result_3_8}")

result_2_9 = pow(2, 9)
print(f"2⁹ = {result_2_9}")

result_4_6 = pow(4, 6)
print(f"4⁶ = {result_4_6}")

#3
import math

result_a = math.sqrt(225625)
print(f"√225625 = {result_a}")

result_b = math.sqrt(4225)
print(f"√4225 = {result_b}")

#4
import random

random_decimal = random.uniform(0, 1)
rounded_decimal = round(random_decimal, 3)
print(f"Random decimal number: {random_decimal}")
print(f"Rounded to 3 decimal places: {rounded_decimal}")

#5
import random

random_decimal = random.uniform(100, 120)
rounded_decimal = round(random_decimal, 1)
print(f"Random decimal number: {random_decimal}")
print(f"Rounded to 1 decimal place: {rounded_decimal}")

#6
import random

for i in range(10):
    random_integer = random.randint(1, 100)
    print(f"Random integer {i + 1}: {random_integer}")
