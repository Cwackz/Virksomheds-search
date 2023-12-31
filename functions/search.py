from utils.imports import *
from utils.misc import *
def search():
    from main import main
    
    os.system("cls")

    user_input = input("""
Du har disse valgmuligheder for søgning:
1) CVR/Virksomhedens navn 
2) Hvilken virksomhed har dette tlf nr?
3) tilbage til menuen
                       
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

        dataprint()
        
        user_input = input("Indtast dit valg: ")

        if user_input == "1":
            print(data.get("vat"))
        
        elif user_input == "2":
            print(data.get("address"))
        
        elif user_input == "3":
            print(data.get("startdate"))
        
        elif user_input == "4":
            print(data.get("phone"))
        
        elif user_input == "5":
            print(data.get("email"))
        
        elif user_input == "6":
            print(data.get("employees"))
        
        elif user_input == "7":
            print(data.get("industrydesc"))
        
        elif user_input == "8":
            print(data.get("companydesc"))
        
        elif user_input == "9":
            print(data.get("creditbankrupt"))
        
        elif user_input == "10":
            print(data.get("owners", [{}])[0].get("name") if data.get("owners") else None)
        
        elif user_input == "11":
            main()

        else:
            print("Ugyldigt valg!")
            search()
    
    elif user_input == "2":
        user_input = input("Indtast telefon nr: ")
        virksomhed = user_input.replace(" ", "").replace("+45", "")
        
        virk = f"https://cvrapi.dk/api?country=dk&phone={virksomhed}"
        
        response = requests.post(virk)
        
        data = response.json()
        
        name = data.get("name")
        
        typewrite(f"Virksomheden bag telefon nummeret er: {name}")

    elif user_input == "3":
        main()
    else:
        print("Ugyldigt valg!")
        search()