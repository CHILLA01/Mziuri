class BankAccount:
    def __init__(self, account_name):
        self.__account_name = account_name
        self.__balance = 0

    def get_account_name(self):
        return self.__account_name

    def set_account_name(self, new_name):
        self.__account_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} ლარი წარმატებით დაემატა ანაბარზე.")
        else:
            print("თანხა უნდა იყოს 0-ზე მეტი.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"ანგარიშიდან წარმატებით გაიტანე {amount} ლარი.")
            else:
                print("ბალანსზე არასაკმარისი თანხაა.")
        else:
            print("თანხა უნდა იყოს 0-ზე მეტი.")


    def get_balance(self):
        return self.__balance

def main():
    name = input("შეიყვანეთ თქვენი სახელი: ")
    account = BankAccount(name)

    while True:
        print("\nაირჩიეთ მოქმედება:")
        print("1 - ანგარიშის სახელის შეცვლა")
        print("2 - ანაბრის დამატება")
        print("3 - თანხის გატანა")
        print("4 - ბალანსის შემოწმება")
        print("5 - გასვლა")

        choice = input("შეიყვანეთ არჩევანი (1-5): ")

        if choice == "1":
            new_name = input("ახალი სახელი: ")
            account.set_account_name(new_name)
            print(f"სახელი განახლდა: {account.get_account_name()}")

        elif choice == "2":
            amount = float(input("რა ოდენობის თანხა გსურთ რომ შეიტანოთ? "))
            account.deposit(amount)
            print(f"ბალანსი: {account.get_balance()} ლარი")

        elif choice == "3":
            amount = float(input("რა ოდენობის თანხა გსურთ რომ შეიტანოთ "))
            account.withdraw(amount)
            print(f"ბალანსი: {account.get_balance()} ლარი")

        elif choice == "4":
            print(f"ბალანსი: {account.get_balance()} ლარი")

        elif choice == "5":
            print("ნახვამდის!")
            break

        else:
            print("არასწორი არჩევანი! სცადეთ თავიდან.")
main()
