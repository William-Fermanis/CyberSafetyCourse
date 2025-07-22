import time
import random

# List of fake accounts with hints, passwords, and extra hints
accounts = [
    {"username": "Wiremu", "hint": "My favorite Maori food", "password": "hangi", "extra_hint": "ha___"},
    {"username": "Darren", "hint": "My Marae", "password": "takapuwahia", "extra_hint": "ta__pu__h__"},
    {"username": "Ngati_Kura_school_admin", "hint": "Name of school + 123", "password": "NgatiKura123", "extra_hint": "Nga__Ku__1__"},
    {"username": "Emily", "hint": "My favorite KPOP Band", "password": "HUNTRIX", "extra_hint": "H__T__X"},
    {"username": "Aroha", "hint": "The word for love in Māori", "password": "aroha", "extra_hint": "a___a"},
    {"username": "Jake", "hint": "Common pet name + 123", "password": "Fluffy123", "extra_hint": "F____123"},
    {"username": "AdminNZ", "hint": "Default admin password", "password": "admin", "extra_hint": "a____"},
    {"username": "Reuben", "hint": "A city in NZ starting with W", "password": "Wellington", "extra_hint": "W_________"},
    {"username": "Tina", "hint": "A fruit and a color", "password": "Orange", "extra_hint": "O_____"},
    {"username": "GamingGuy", "hint": "Most common keyboard combo", "password": "wasd", "extra_hint": "w___"},
    {"username": "Marie", "hint": "Birth year + name", "password": "Marie2009", "extra_hint": "M____20__"},
    {"username": "Library1", "hint": "Read + number", "password": "Read123", "extra_hint": "R___123"},
    {"username": "NatureGirl", "hint": "Tall native tree in NZ", "password": "Kauri", "extra_hint": "K___i"},
    {"username": "TeReoFan", "hint": "Maori for family", "password": "whānau", "extra_hint": "w_____"},
    {"username": "SportsKing", "hint": "National sport of NZ", "password": "rugby", "extra_hint": "r___y"},
    {"username": "CookieLover", "hint": "Classic sweet + number", "password": "Cookie7", "extra_hint": "C____7"},
    {"username": "Maddy", "hint": "A season of the year", "password": "summer", "extra_hint": "s_____"},
    {"username": "NZHistory", "hint": "Year Treaty of Waitangi signed", "password": "1840", "extra_hint": "1__0"},
    {"username": "Teacher", "hint": "My profession", "password": "teacher", "extra_hint": "t______"},
    {"username": "Techie", "hint": "Popular search engine", "password": "Google", "extra_hint": "G____e"},
]

# Game start
print("🔐 Welcome to the Cyber Safe Terminal!")
print("Your mission: Access all accounts by guessing their passwords.")
print("You will receive a hint for each account. You have 3 tries per account.\n")

score = 0
i = 0

for acc in accounts:
    print(f"Score {score}/{i}")
    print(f"🔍 Attempting to access account {i + 1}/{len(accounts)}")
    print(f"\nAccessing account: {acc['username']}")
    print(f"Password hint: {acc['hint']}")
    i += 1
    attempts = 3

    while attempts > 0:
        
        guess = input("Enter password: ")
        if guess == acc["password"]:
            print("✅ Access granted!")
            score += 1
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect. Attempts left: {attempts}")
            if attempts == 1:
                print(f"❌ Incorrect. Here's an extra hint: {acc['extra_hint']}")
            
    
    if attempts == 0:
        print(f"🚫 Access denied. The correct password was: {acc['password']}")

    time.sleep(1)
    if(i!=len(accounts)-1):
        print("🔄 Moving to the next account...\n")

# Game end summary
print("\n🔚 Session complete.")
print(f"You successfully accessed {score} out of {len(accounts)} accounts.")
