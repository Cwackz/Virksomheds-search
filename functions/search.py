from utils.imports import *
from utils.misc import *
class Search:
    def __init__(self, main_instance):
        self.main_instance = main_instance
    def run(self):
        os.system("cls")
        
        os.system("cls")

        user_input = input("""
    Du har disse valgmuligheder for søgning:
    1) CVR/Virksomhedens navn 
    2) Hvilken virksomhed har dette tlf nr?
                        
    Indtast dit valg:""")
        if user_input == "1":

            user_input = input("Indtast CVR eller virksomhedens navn: ")

            virksomhed = user_input.replace(" ", "%20")
            
            with open('history.txt', 'a') as f:

                f.write(f'{virksomhed}\n')

            virk = f"https://cvrapi.dk/api?country=dk&search={virksomhed}"

            response = requests.post(virk)

            data = response.json()
        
            name = data.get("name")
            os.system("cls")
            typewrite(f"Data hentet fra {name}")
        while True:
            sleep(0.5)
            os.system("cls")
            dataprint()
            
            user_input = input("Indtast dit valg: ")

            if user_input == "1":
                print(data.get("vat"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "2":
                print(data.get("address"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "3":
                print(data.get("startdate"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "4":
                print(data.get("phone"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "5":
                print(data.get("email"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "6":
                print(data.get("employees"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "7":
                print(data.get("industrydesc"))
                input("Tryk enter for at komme videre...")
            
            elif user_input == "8":
                print(data.get("companydesc"))
                input("Tryk enter for at komme videre...")
                
            elif user_input == "9":
                print(data.get("creditbankrupt"))
                input("Tryk enter for at komme videre...")
                
            elif user_input == "10":
                print(data.get("owners", [{}])[0].get("name") if data.get("owners") else None)
                input("Tryk enter for at komme videre...")
                
            elif user_input == "11":
                self.main_instance.run()
                break

            elif user_input == "2":
                user_input = input("Indtast telefon nr: ")
                virksomhed = user_input.replace(" ", "").replace("+45", "")

                virk = f"https://cvrapi.dk/api?country=dk&phone={virksomhed}"

                response = requests.post(virk)

                data = response.json()

                name = data.get("name")

                typewrite(f"Virksomheden bag telefon nummeret er: {name}")
                input("Tryk enter for at komme videre...")
                
            else:
                print("Ugyldigt valg!")
                self.main_instance.run()
