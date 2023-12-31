from utils.misc import *
from utils.imports import *
def main():
    while True:
        os.system("cls")
        menu()
        user_input = input("Indtast dit valg: ")
        if user_input == "1":
            from functions.search import search
            search()
            break
        elif user_input == "2":
            from functions.load import load
            load()
            break
        else:
            print("Ugyldigt valg!")

if __name__ == "__main__":
    main()  