#1
base = float(input("შეიყვანეთ ფუძე:"))
power = float(input("შეიყვანეთ ხარისხი:"))
result = base ** power
print("პასუხი", result)

#2
a= float(input("შეიყვანეთ პირველი რიცხვი:"))
b= float(input("შეიყვანეთ მეორე რიცხვი:"))
difference = abs(a - b)
print("ამ რიცხვებს შორის აბსოლუტური სხვაობაა:", difference)

#3
number = int(input("შეიყვანეთ რიცხვი:"))
result = ["ლუწია", "კენტია"][number % 2]
print("რიცხვი", result)

#4
num1 = float(input("შეიყვანეთ პირველი რიცხვი:"))
num2 = float(input("შეიყვანეთ მეორე რიცხვი:"))
both_positive = (num1 > 0) and (num2 > 0)
one_negative = (num1 < 0) or (num2 < 0)
print("ორივე რიცხვი დადებითია:", both_positive)
print("ერთი მაინც უარყოფითია:", one_negative)

#bonus

#1
a = float(input("რიცხვი 1:"))
b = float(input("რიცხვი 2:"))
print("ჯამი:", a +  b)
print("სხვაობა:", a - b)
print("ნამრავლი:", a * b)
print("განაყოფი:", a / b if b != 0 else "ნულზე გაყოფა არ შეიძლება")

#2
num = float(input("შეიყვანეთ რიცხვი: "))

დადებითია = num > 0
უარყოფითია = num < 0
ნულია = num == 0

print("დადებითი:", დადებითია)
print("უარყოფითი:", უარყოფითია)
print("ნულია:", ნულია)




