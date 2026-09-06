import logging

from expense import Expense, OperationsUnderExpense

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

operation_under_expense = OperationsUnderExpense()

def main():
    logging.info("Starting the program.")
    initial_info()
    while True:
        while True:
            try:
                menu()
                selected_option: int = int(input("Your choice: "))
                if selected_option>5 or selected_option<1:
                    raise ValueError("Choice must be only between 1 to 5!")
                break

            except Exception as error:
                print(f"Error: {error}")
                logging.error(f"Input error in menu: {error}")
                continue

        match selected_option:
            case 1:
                logging.info("User is adding a new expense.")
                try:
                    print("You must enter the title, the amount, the category of expense.")
                    title: str = input("Title: ")
                    amount: float = float(input("Amount: "))
                    category: str = input("Category(food, transport): ")
                    category_split = category.split(",")
                    id_new_expense = operation_under_expense.id_number()

                    new_expense: Expense = Expense(title, amount, category_split, id_new_expense )

                    operation_under_expense.add_expense(new_expense)
                    print("The new expense was added successfully!")
                    logging.info(
                        f"Expense '{title}' for amount {amount} successfully added."
                    )
                except Exception as error:
                    print(f"Error: {error}")

            case 2:
                logging.info("User selected: Show all expenses.")
                print("All expenses:")
                print(operation_under_expense)
                

            case 3:
                logging.info(
                    "User selected: Show expenses for a certain category."
                )
                try:
                    name_category: str = input("Your category for searching: ")
                    result_search: list[Expense] = operation_under_expense.search_certain_category(name_category)
                    print(f"Here all expenses which have {name_category} category:")
                    for item in result_search:
                        print(item)
                    
                except Exception as error:
                    print(f"Error: {error}")

            case 4:
                logging.info("User selected: Show total sum.")
                total_amount: float = operation_under_expense.show_total_amount()
                if not total_amount:
                    print("Expense list is empty!")
                else:
                    print(f"Total amount = {total_amount}")

            case 5:
                logging.info("Program finished by user.")
                print("Goodbye!")
                break
                




def initial_info():
    print("""
Hello!
Here you can commit some operations with expense:
""")

def menu():
    print("""
--- MENU ---
1- add expense
2- show all expenses
3- show expense for a certain category
4- show total sum
5- exit
""")

if __name__ == "__main__":
    main()