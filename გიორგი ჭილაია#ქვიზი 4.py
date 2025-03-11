
file_path = "titanic.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

headers = lines[0].strip().split(",")
data = [line.strip().split(",") for line in lines[1:]]


sex_index = headers.index("Sex")
survived_index = headers.index("Survived")
pclass_index = headers.index("Pclass")
fare_index = headers.index("Fare")
age_index = headers.index("Age")



total_passengers = len(data)
female_count = male_count = 0
survived_females = not_survived_females = 0
survived_males = not_survived_males = 0
class_counts = {1: 0, 2: 0, 3: 0}
fare_sums = {1: 0, 2: 0, 3: 0}
fare_counts = {1: 0, 2: 0, 3: 0}
age_sum = age_count = 0




for row in data:
    sex = row[sex_index]
    survived = int(row[survived_index])
    pclass = int(row[pclass_index])
    fare = float(row[fare_index]) if row[fare_index] else 0
    age = float(row[age_index]) if row[age_index] else 0


    if sex == "female":
        female_count += 1
        if survived:
            survived_females += 1
        else:
            not_survived_females += 1
    elif sex == "male":
        male_count += 1
        if survived:
            survived_males += 1
        else:
            not_survived_males += 1

    class_counts[pclass] += 1
    fare_sums[pclass] += fare
    fare_counts[pclass] += 1



    # ასაკის ჯამი
    if age > 0:
        age_sum += age
        age_count += 1

female_percentage = (female_count / total_passengers) * 100
male_percentage = (male_count / total_passengers) * 100

avg_fare_per_class = {cls: round(fare_sums[cls] / fare_counts[cls], 2) if fare_counts[cls] > 0 else 0 for cls in class_counts}

# საშუალო ასაკი
avg_age = round(age_sum / age_count, 2) if age_count > 0 else 0

titanic_stats = {
    "Total Passengers": total_passengers,
    "Female Count": female_count,
    "Male Count": male_count,
    "Female Percentage": round(female_percentage, 2),
    "Male Percentage": round(male_percentage, 2),
    "Survived Females": survived_females,
    "Not Survived Females": not_survived_females,
    "Survived Males": survived_males,
    "Not Survived Males": not_survived_males,
    "Class Counts": class_counts,
    "Average Fare Per Class": avg_fare_per_class,
    "Average Age": avg_age  # ბონუსი
}

print(titanic_stats)









#2
class Ticket:
    def __init__(self, movie_name, price, quantity, language="Geo"):
        self.movie_name = movie_name
        self.price = price
        self.quantity = quantity
        self.language = language

    def __str__(self):
        return f"ფილმი: {self.movie_name} | ფასი: {self.price} | დარჩენილი ბილეთები: {self.quantity} | ენა: {self.language}"


class User:
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance

        def __str__(self):
            return f"მომხმარებელი: {self.name} | ბალანსი: {self.balance}"

        def deposit(self, amount):
            """ ბალანსზე თანხის დამატება """
            if amount > 0:
                self.balance += amount
                print(f" {amount} დაემატა ბალანსზე. ახალი ბალანსი: {self.balance}")
            else:
                print("თანხა უნდა იყოს დადებითი რიცხვი.")

        def buy_ticket(self, ticket, quantity):
            """ ბილეთის შეძენა """
            total_cost = ticket.price * quantity
            if ticket.quantity < quantity:
                print(f"მხოლოდ {ticket.quantity} ბილეთია დარჩენილი ფილმზე '{ticket.movie_name}'.")
            elif self.balance < total_cost:
                print(f"ბალანსი არასაკმარისია. საჭიროა {total_cost}, თქვენ გაქვთ {self.balance}.")
            else:
                self.balance -= total_cost
                ticket.quantity -= quantity
                print(f"{self.name}-მ შეიძინა {quantity} ბილეთი ფილმის '{ticket.movie_name}'თვის. თქვენი ახალი ბალანსია: {self.balance}.")


ticket1 = Ticket("Oppenheimer", 15, 10)
ticket2 = Ticket("Snowfall", 25, 5)
ticket3 = Ticket("Dexter", 30, 12)

name = input("შეიყვანეთ თქვენი სახელი: ")
balance = float(input(f"{name}, შეიყვანეთ თქენი ბალანსი: "))
user = User(name, balance)

print(user)


print("\nდამატებული ფილმები:")
print("1.Oppenheimer")
print("2.Snowfall")
print("3.Dexter")

movie_choice = int(input("მოიტანეთ თქვენი არჩევანი: "))
if movie_choice == 1:
    selected_ticket = ticket1
elif movie_choice == 2:
    selected_ticket = ticket2
elif movie_choice ==3:
    selected_ticket = ticket3
else:
    print("არასწორი არჩევანი.")
    exit()

quantity = int(input(f"რამდენი ბილეთი გსურთ'{selected_ticket.movie_name}'-ისთვის? "))
user.buy_ticket(selected_ticket, quantity)