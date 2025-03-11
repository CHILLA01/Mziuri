#1
def get_lengths(strings):
    return [len(s) for s in strings]

string_list = ["hello", "world", "python", "123"]
lengths = get_lengths(string_list)
print(lengths)

#2
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 and set2  # and ვიცი რომ არასწორია მაგრამ არ ვიცოდი როგორ გამეკეთებინა
    return list(common)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(common_elements(list1, list2))

#3
def create_dict_and_print(people):
    people_dict = {person[0]: person[1] for person in people}

    for person in people_dict.items():
        print(f"{person[0]}: {person[1]}")

people = [("ჯასურ", 90), ("ბეკი", 25)]
create_dict_and_print(people)

#4
def check_inventory(products):
    result = []

    for product, amount in products.items():
        if amount > 5:
            result.append((product, "საკმარისია"))
        else:
            result.append((product, "არაა საკმარისი"))
    return result
products = {'ბადრიჯანი': 3, 'ხახვი': 6, 'კომბოსტო': 2}
result = check_inventory(products)
print(result)

#5
def filter_words_starting_with_a(words):
    result = {}
    for word in words:
        if word.lower().startswith('a'):
            result[word] = len(word)
    return result
words = ["apple", "banana", "avocado", "grape", "ananas"]

result = filter_words_starting_with_a(words)
print(result)

#6
# ეს მეთოდებია discard (); pop(); remove ()

#7
# თაფლში როდესაც ელემენტებს შეიყვან შემდეგ მათი შეცვლა არ შეგეძლობა ანუ ვერ დაამატებ სხვა ელემენტებს.
# ლისტში კი შჰეგიძლია შეცვალო დაამატო ან თუნდაც ამოაგდო ელემენტები

#8
#union; min;max;average

#9
# my_dict[key] = value

#10
#მეთოდი .items() გვიბრუნებს ლექსიკონში გასაღებსაც და მნიშვნელობასაც

#11
# თუ არ ვიცით რამდენი არგუმენტის გადაცემა გვსურს მაშინ ვიყენებთ args


