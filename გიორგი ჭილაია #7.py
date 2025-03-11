#1
numbs = [3, 15, 2, 20, 19]
sum_numbs = sum(numbs)
min_numbs = min(numbs)
max_numbs = max(numbs)
average_numbs = sum_numbs / len(numbs)

print("ჯამი:", sum_numbs)
print("მინიმალური:", min_numbs)
print("მაქსიმალური:", max_numbs)
print("საშუალო არითმეტიკული:", average_numbs)

#2
numbs = [3, 15, 2, 20, 19]
numbs.append(102)
numbs.insert(2, 205)
del numbs[3]
numbs.sort()

print("განახლებული სია ზრდადობის მიხედვით:", numbs)

#3
data = []
for i in range(10):
    value = input(f"შეიყვანეთ {i+1}-ე მონაცემი: ")
    data.append(value)

print("შეყვანილი მონაცემები სიის სახით:", data)

#4
data = []
if data:
    print("სია არ არის ცარიელი.")
else:
    print("სია ცარიელია.")

#5
numbers = [5, 12, 7, 20, 33, 8, 19, 2, 13]
even_numbers = [num for num in numbers if num % 2 == 0]
print("მიღებული სია (მხოლოდ ტოლი რიცხვები):", even_numbers)

#6
input_list = [5, 8, 2, 8, 6, 5, 9, 3, 2]
output_list = [item for item in input_list if input_list.count(item) == 1]
print("მიღებული სია, სადაც არ არის დუბლიკატები:", output_list)

#bonus
