from utils.imports import *

def dataprint():
        print("""Hvilken data vil du se?
1) vat
2) adresse
3) start dato
4) telefon nr
5) email
6) medarbejdere
7) industri
8) hvilken type virksomhed
9) konkurs
10) ejere
11) tilbage til menuen
              """)
        
def menu():
    print("""
    ┌───────────────────────────┐
    │            Menu           │
    │1. Søg Virksomhed          │
    │2. historik                │
    └───────────────────────────┘     
    """)

def typewrite(text:str):
    for char in text:
        sleep(0.05)
        print(char, end="", flush=True)
    print("\n")
