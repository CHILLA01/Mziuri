#1
dictionary = {0: 10, 1: 20}
dictionary[2] = 30
del dictionary[1]
dictionary.update({3: 40})
print("Updated Dictionary:", dictionary)

print("After Deletion:", dictionary)

#2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = dic1 | dic2 | dic3
print("Merged Dictionary:", merged_dict)

#3
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key_to_check = 3
if key_to_check in d:
    print(f"Key {key_to_check} is in the dictionary.")
else:
    print(f"Key {key_to_check} is not in the dictionary.")

#4
d = {'x': 10, 'y': 20, 'z': 30}

for key, value in d.items():
    print(f"{key} {value}")

#5
cube_dict = {x: x**3 for x in range(1, 10)}
print("Cube Dictionary:", cube_dict)

#6
person = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
print("Name:", person["firstName"])
print("Last Name:", person["lastName"])
print("Age:", person["age"])
print("Children Names:", ", ".join(child["firstName"] for child in person["children"]))
