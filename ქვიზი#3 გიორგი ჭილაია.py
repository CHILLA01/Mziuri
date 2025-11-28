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


-- 1. დაბეჭდე ყველა წიგნი, რომლის ავტორია Rowling და ფასი მეტია 20-ზე.
SELECT * FROM books
WHERE author = 'Rowling' AND price > 20;

-- 2. დაბეჭდე ყველა მომხმარებელი, რომლის ბალანსი ნაკლებია 40 ლარზე.
SELECT * FROM users
WHERE balance < 40;

-- 3. დაბეჭდე ყველა წიგნი, რომლის ფასი არ აღემატება 20 ლარს.
SELECT * FROM books
WHERE price <= 20;

-- 4. დაბეჭდე ყველა მომხმარებელი, რომელმაც რაიმე წიგნი იყიდა.
SELECT DISTINCT u.*
FROM users u
JOIN purchase p ON u.id = p.user_id;

-- 5. დაბეჭდე ყველა მომხმარებელი, რომლებმაც იყიდეს წიგნები 100 ლარზე მეტი თანხით ჯამში.
SELECT u.username, SUM(b.price) AS total_spent
FROM users u
JOIN purchase p ON u.id = p.user_id
JOIN books b ON p.book_id = b.id
GROUP BY u.id
HAVING total_spent > 100;

-- 6. დაბეჭდე ყველა მომხმარებელი, რომელმაც იყიდა წიგნები 2018 წელს.
SELECT DISTINCT u.*
FROM users u
JOIN purchase p ON u.id = p.user_id
WHERE strftime('%Y', p.purchase_date) = '2018';

-- 7. დაბეჭდე ყველა მომხმარებელი და წიგნი, რომელიც მათ იყიდეს 2018 წელს.
SELECT u.username, b.title, p.purchase_date
FROM users u
JOIN purchase p ON u.id = p.user_id
JOIN books b ON p.book_id = b.id
WHERE strftime('%Y', p.purchase_date) = '2018';

-- 8. დაბეჭდე ყველა მომხმარებელი და წიგნი, რომელიც მათ იყიდეს, თუნდაც მხოლოდ ერთხელ.
SELECT DISTINCT u.username, b.title
FROM users u
JOIN purchase p ON u.id = p.user_id
JOIN books b ON p.book_id = b.id;

-- 9. დაბეჭდე ყველა მომხმარებელი და მათი ბალანსი, რომლებიც არ იყენებენ არცერთ წიგნს.
SELECT u.*
FROM users u
LEFT JOIN purchase p ON u.id = p.user_id
WHERE p.id IS NULL;

-- 10. დაბეჭდე იმ წიგნების დასახელება, რომლებიც მხოლოდ ერთი მომხმარებლის მიერ იქნა შეძენილი.
SELECT b.title
FROM books b
JOIN purchase p ON b.id = p.book_id
GROUP BY b.id
HAVING COUNT(DISTINCT p.user_id) = 1;

-- 11. დაბეჭდე ყველა წიგნი, რომლის ავტორია William Shakespeare.
SELECT * FROM books
WHERE author = 'William Shakespeare';

