#1
file_name = "example.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write("ეს არის საცდელი ტექსტი")
print(f"ფაილი '{file_name}' შეიქმნა")

#2
file_name = "example.txt"
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()
print("ფაილის კონტენტი:")
print(content)
char_count = len(content)
print(f"\nფაილში არსებული სიმბოლოების რაოდენობა: {char_count}")

#3
file_name = "example.txt"
append_text = "\nეს არის დამატებული ტექსტი!"
with open(file_name, "a", encoding="utf-8") as  file:
     file.write(append_text)
print(f"ფაილში '{file_name}' წარმატებით დაემატა ტექსტი")

#4
destination_file = "copy.txt"
file_name = "source.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("ეს არის საცდელი ფაილი")
print(f"ფაილი '{file_name}' წარმატებით შეიქმნა")

with open(destination_file, "w", encoding="utf-8") as file:
    file.write(content)
print(f"ფაილი '{file_name}' წარმატებით დაკოპირდა '{destination_file}'-ში")

#5
file1 = "file1.txt"
with open(file1, "w", encoding="utf-8") as file:
    file.write("ეს არის ახალი ფაილი\n")
print(f"ფაილი '{file1}' შეიქმნა")

file2 = "file2.txt"
with open(file2, "w", encoding="utf-8") as file:
    file.write("ეს არის ახალი ფაილი\n")
print(f"ფაილი '{file2}' შეიქმნა")


merged_file = "merged.txt"
with open(file1, "r", encoding="utf-8") as f1:
    content1 = f1.read()

with open(file2, "r", encoding="utf-8") as f2:
    content2 = f2.read()

with open(merged_file, "w", encoding="utf-8") as merged:
    merged.write(content1 + "\n" + content2)
print(f"ფაილები '{file1}' და '{file2}' წარმატებით გაერთიანდა '{merged_file}'-ში!")

#6
file_name = "example.txt"

with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
print("ფაილის კონტენტი დიდი ასოებით:")
print(content.upper())

#7

file_name = "example.txt"
with open(file_name, "w", encoding="utf-8") as file:
    while True:
        user_input = input("შეიყვანეთ ინფორმაცია: ")
        if user_input == "0":
            break
        file.write(user_input + "\n")

print(f"შეყვანილი მონაცემები ჩაიწერა '{file_name}' ფაილში")

#8



