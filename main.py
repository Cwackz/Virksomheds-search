# main.py
from utils.misc import *
from utils.imports import *
from functions.search import Search
from functions.load import Load

class Main:
    def __init__(self):
        self.search = Search(self)
        self.load = Load()

    def run(self):
        while True:
            os.system("cls")
            menu()
            user_input = input("Indtast dit valg: ")
            if user_input == "1":
                self.search.run()
            elif user_input == "2":
                self.load.run()
            elif user_input == "11":
                continue
            else:
                print("Ugyldigt valg!")

if __name__ == "__main__":
    Main().run()