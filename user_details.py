import pandas as pd
import user_details_func

df = pd.read_csv("credentials.csv")

with open("credentials.csv", "w") as credentials:
    credentials.write("Name,Last name,Year of birth,Contacts,Password")

def new_user():
    print("\t\t" + ":" * 21)
    print("\t\t| Create an account |")
    print("\t\t" + ":" * 21)
    
    while True:
        name = input("Enter first name:\n>>> ")
        characters = "abcdefghijklmnopqrstuvwxyz"
        incorrect = False
        for j in name:
            if j.lower() not in characters:
                incorrect = True

        if incorrect:
            print("Invalid first name")
            continue
        else:
            break

    while True:
        last_name = input("\nEnter last name:\n>>> ")
        characters = "abcdefghijklmnopqrstuvwxyz"
        incorrect = False
        for j in last_name:
            if j.lower() not in characters:
                incorrect = True

        if incorrect:
            print("Invalid last name entered")
            continue
        else:
            break

    while True:
        year = input("\nYear of birth:\n>>> ")
        
        try:
            y = int(year)
            if y < 1922:
                print("People this age cannot use smartphones")
                quit()
            elif y > 2006:
                print("Under age for this app")
                quit()
            break
        except:
            print("Year entered is invalid")
            continue

    account = False
    while True:
        contact = input("\nEmail/cellphone numbers:\n>>> ")
        contact_1 = input("Confirm contact details\n>>> ")
        if contact.isdigit():
            contact = int(contact)
            contact_1 = int(contact_1)

        if contact_1 != contact:
            print("Contacts do not match")
            continue
        elif contact in list(df["Contacts"]):
            account = True
            print("Account already exist for this contact, sign in")
            break
        break
    
    if account:
        return None

    gen_pass = input("Auto generate password(yes/no)\n>>>")

    if gen_pass.lower() == "no":
        print("\nPassword has to contain:\n::Minimum length of 8\n::Lower and upper case letters\n::Atleast one special character\n::Atleast one number\n")
        while True:
            password = input("Password:\n>>>")
            if user_details_func.pw_validator(password):
                break
            print("Your password does not meet the requirements, try again....\n")
    else:
        password = user_details_func.password_gerator()
        print(f"\nYour unique password is >> {password}\n")


    with open("credentials.csv", "a") as credentials:
        credentials.write(f"\n{name.capitalize()},{last_name.capitalize()},{year},{contact},{password}")
    
    print("\t\t" + "~" * 22)
    print("\t\t| WELCOME TO THE APP |")
    print("\t\t" + "~" * 22)
    print(f"\n{'_'*50}\n\n")

def sign_in():
    print("\t\t" + ":" * 16)
    print("\t\t| Sign in page |")
    print("\t\t" + ":" * 16)

    while True:
        contacts = input("\nEmail or cell number registered\n::> ")
        password = input("\nPASSWORD\n::> ")
        if contacts.isdigit():
            contacts = int(contacts)

        if contacts not in list(df["Contacts"]):
            new = input("Username does not exist, create account?(yes/no)\n>>> ")
            if new.lower() == "yes":
                new_user()
                return None
            else:
                continue
        
        user = df[df["Contacts"] == contacts]
        if password != list(user["Password"])[0]:
            print("Incorrect password entered, re-confirm details...")
            continue
        break

    print(f"\n\n Welcome back to the app {list(user['Name'])[0]} your friends are waiting on you\n{':' * 75}\n{'~' * 75}")
    user_details_func.triangle(-38)


print(f"\n\t\t\tWelcome to my app\n{'_-'*40}")
status = input("\nAre you a new user?(yes/no)\n::> ")

if status.lower() == "yes":
    new_user()
elif status.lower() == "no":
    sign_in()

