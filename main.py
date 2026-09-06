import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

def main():
    logging.info("Starting the program.")
    initial_info()
    while True:
        try:
            menu()
            selected_option: int = int(input("Your choice: "))
            if not selected_option:
                raise ValueError("Choice must be digit only between 1 to 5!") 
            elif selected_option>5 or selected_option<1:
                raise ValueError("Choice must be only between 1 to 5!")
            else:
                break

        except Exception as error:
            print(error)
            logging.error(error)
            continue

    match selected_option:
        case 1:
            pass

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
4- show tottal sum
5- exit
""")

if __name__ == "__main__":
    main()