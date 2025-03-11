#1
while True:
    try:
        num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
        result = num1 / num2
        print(f"შედეგი: {result}")
        break
    except ValueError:
        print("შეცდომა შეიყვანეთ რიცხვი.")
    except ZeroDivisionError:
        print("შეცდომა ნულზე გაყოფა შეუძლებელია.")

#2
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "შეცდომა! ნულზე გაყოფა შეუძლებელია."
    except TypeError:
        return "შეცდომა! შეიყვანეთ მხოლოდ რიცხვები."

print(divide_numbers(10, 2))
print(divide_numbers(5, 0))

#3
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("შეცდომა! მასივის ინდექსი არასწორია.")

#4
try:
    with open("myresult.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("შეცდომა! ფაილი ვერ მოიძებნა.")

#5
import math

def solve_quadratic(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("კვადრატულ განტოლებას არ აქვს რეალური ფესვები.")
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    except ZeroDivisionError:
        return "შეცდომა! a ვერ იქნება ნული."
    except ValueError as e:
        return str(e)

print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 5))

#6
def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return (a + b + c) / 3
    else:
        raise ValueError("სამკუთხედის გვერდების სიგრძეები არასწორია.")

try:
    print(check_triangle(3, 4, 5))
    print(check_triangle(1, 2, 3))
except ValueError as e:
    print(e)
