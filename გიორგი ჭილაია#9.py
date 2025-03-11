#1
string = input("შეიყვანეთ სტრიქონი: ")
count_a = string.count("a")
print("სიმბოლო 'a'-ს რაოდენობა: ", count_a)

#2
string = input("შეიყვანეთ სტრიქონი: ")
upper_string = string.upper()
print("მაღალ რეგისტრში: ", upper_string)

#3
text = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
first_20 = text[:20]
count_s = text.count("ს")
print("პირველი 20 სიმბოლო: ", first_20)
print("'ს'-ს რაოდენობა: ", count_s)

#4
string = input("შეიყვანეთ სტრიქონი: ")
swapped_string = string.swapcase()
print("რეგისტრის შეცვლილი სტრიქონი: ", swapped_string)

#5
text = "Hello, this is example of string. Please, write this text and do some exercises."
word_count = len(text)
print("სიტყვების რაოდენობა: ", word_count)


#bonus

#6
text = "Hello, this is example of string. Please, write this text and do some exercises."
replaced_text = text.replace("is", "were")
print("შეცვლილი ტექსტი: ", replaced_text)

