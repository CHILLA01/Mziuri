#1
numbers_tuple = tuple(x**3 for x in range(1, 101) if x % 5 == 0)
length = len(numbers_tuple)

print("Tuple:", numbers_tuple)
print("Tuple-ის სიგრძე:", length)

#2
iterator = iter(numbers_tuple)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Iteration დასრულდა!")

#3
numbers_set = {x**3 for x in range(1, 101) if x % 5 == 0}
average = sum(numbers_set) / len(numbers_set)

print("Set:", numbers_set)
print("Set-ის საშუალო:", average)

#4

iterator_set = iter(numbers_set)

try:
    while True:
        print(next(iterator_set))
except StopIteration:
    print("Iteration დასრულდა!")

#5
def number_generator():
    for num in range(1, 6):
        yield num

gen_iter = number_generator()

try:
    while True:
        print(next(gen_iter))
except StopIteration:
    print("Iteration დასრულდა!")

#bonus
bonus_iterator = iter(numbers_tuple)

try:
    while True:
        print(next(bonus_iterator))
except StopIteration:
    print("Iteration დასრულდა!")
