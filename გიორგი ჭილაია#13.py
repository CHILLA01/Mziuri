#1
students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 75, "History": 80},
    "Charlie": {"Math": 95, "Science": 88}
}

def add_student(students, name, grades):
    students[name] = grades

def update_grade(students, name, subject, grade):
    students.setdefault(name, {})[subject] = grade

def calculate_average(students, name):
    return sum(students.get(name, {}).values()) / len(students[name])

def display_student(students, name):
    return students.get(name, "Student not found")

while True:
    print("Options:")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Display Student Info")
    print("4. Calculate Average Grade")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
            student_name = input('Enter student name: ')
            grades_input = input("Enter grades as 'Subject1:Grade1,Subject2:Grade2': ")
            subject_grades = {}
            for item in grades_input.split(","):
                subject, grade = item.split(":")
                subject_grades[subject] = int(grade)

            add_student(students, student_name, subject_grades)

    elif choice == '2':
        name = input('Enter student name: ')
        subject = input('Enter subject: ')
        grade = int(input('Enter new grade: '))
        update_grade(students, name, subject, grade)
    elif choice == '3':
        name = input('Enter student name: ')
        print(display_student(students, name))
    elif choice == '4':
        name = input('Enter student name: ')
        avg = calculate_average(students, name)
        print('fAverage grade: {avg}' if avg else 'No grades available.')
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Try again.')

#2
person = {"name": "Giorgi", "age":28, "city":"Tbilisi", "occupation":"programmer"}
print(person)

#3
person = {"name": "Giorgi", "age":28, "city":"Tbilisi", "occupation":"programmer"}
person['hobby'] = 'ჭამა და ძილი'
del person['age']
print(person)

#4
def merge_dictionaries(dict1, dict2):
        return {dict1 | dict2}

#5
def filter_dictionary(dictionary):
    filtered_dict = {}
    for key, value in dictionary.items():
        if value > 10:
            filtered_dict[key] = value
    return filtered_dict

#6
numbers = [1, 3, 5, 7, 9]
cubed_dict = {num: num**3 for num in numbers}
print(cubed_dict)

#7
def frequency_counter(list):
    return {item: list.count(item) for item in set(list)}
sample_list = [1, 2, 2, 3, 3, 3, 4]
print(frequency_counter(sample_list))

#8

#9
def create_dictionary(keys, values):
    if len(keys) != len(values):
        return "Lists must have the same length."
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict

#10