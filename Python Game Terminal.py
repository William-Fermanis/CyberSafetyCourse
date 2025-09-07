import time

# Fake file system
file_system = {
    "/": {
        "home": {
            "notes.txt": "Always use strong passwords.",
            "documents": {
                "password_hint.txt": "Try looking in /home/secrets",
            },
            "secrets": {
                "clue1.txt": "The password is hidden in parts: first part is 'hack'",
                "clue2.txt": "Second part is 'the'",
                "clue3.txt": "Third part is 'planet'",
            }
        },
        "secure_account": {
            "locked.txt": "🔒 This folder is locked. Enter password to unlock."
        }
    }
}

# Helper variables
current_path = ["/"]
correct_password = "hacktheplanet"
unlocked_secure_account = False

def get_current_dir():
    ref = file_system
    for p in current_path[1:]:
        ref = ref.get(p, {})
    return ref

def print_prompt():
    print(f"\nuser@cyber-safe:{'/'.join(current_path)}$ ", end='')

def list_dir():
    items = get_current_dir()
    for key in items:
        print(key)

def change_dir(folder):
    global current_path
    if folder == "..":
        if len(current_path) > 1:
            current_path.pop()
    else:
        dir_ref = get_current_dir()
        if folder in dir_ref and isinstance(dir_ref[folder], dict):
            current_path.append(folder)
        else:
            print("No such directory.")

def cat_file(filename):
    dir_ref = get_current_dir()
    if filename in dir_ref and isinstance(dir_ref[filename], str):
        print(f"\n📄 {filename}:\n{dir_ref[filename]}")
    else:
        print("No such file.")

def unlock_secure_folder():
    global unlocked_secure_account
    attempt = input("Enter password to unlock secure_account: ")
    if attempt == correct_password:
        print("✅ Access granted! You've unlocked the secure folder.")
        unlocked_secure_account = True
    else:
        print("❌ Incorrect password.")

# Game loop
print("Welcome to the Cyber Terminal Challenge!")
print("Use commands: ls, cd [folder], cd .., cat [filename], unlock\nFind the hidden password and access the secure account.\n")

while True:
    print_prompt()
    command = input().strip()

    if command == "exit":
        print("Goodbye.")
        break
    elif command == "ls":
        list_dir()
    elif command.startswith("cd "):
        _, folder = command.split(" ", 1)
        change_dir(folder)
    elif command.startswith("cat "):
        _, filename = command.split(" ", 1)
        cat_file(filename)
    elif command == "unlock":
        if "/secure_account" in "/".join(current_path):
            if unlocked_secure_account:
                print("🔓 Folder already unlocked.")
            else:
                unlock_secure_folder()
        else:
            print("You must be in the /secure_account directory to unlock it.")
    elif command == "help":
        print("Commands: ls, cd [folder], cd .., cat [filename], unlock, exit")
    else:
        print("Unknown command. Type 'help' for a list of commands.")

    # Show folder contents if unlocked
    if unlocked_secure_account:
        if "/secure_account" in "/".join(current_path):
            print("\n📁 secure_account contents:\n - top_secret.txt: Mission accomplished!")
