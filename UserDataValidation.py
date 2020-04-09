import random
import string


def collect_details():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email = input("Also, what is your email address: ")
    return first_name, last_name, email


def generate_password(first_name, last_name):
    create_pword = first_name[:2] + last_name[-2:]
    n = 5
    gen_pword = ''.join(random.choices(string.ascii_lowercase + string.digits, k=n)) #random generator for 5 characters
    password = create_pword + gen_pword
    print(f"This password was automatically generated for you - {password}")
    return password


print("Hello there! Welcome to HNG Tech.")
HNG_interns = []
admin_check = True

while admin_check:
    first_name, last_name, email = collect_details()
    user_name = [first_name, last_name, email] # create container for user
    password = generate_password(first_name, last_name)

    admin_choice = True

    while admin_choice: #checks if input is not YES or NO
        user_input1 = input('''
        Are you okay with the password? 
        Type YES to proceed, or NO to create a password yourself: ''')
        response1 = user_input1.upper()
        if response1 == "YES" or response1 == "NO":
            break
        else:
            print('''
            You have typed in a wrong request!
            Let us give this another try''')


    if admin_choice == "NO":
            password = str(input("\nKindly input your desired password: "))
            while len(password) < 7:
                password = str(input('''
                Your custom password must be equal to or greater than 7 alphanumeric characters.
                Kindly retype a compliant password: '''))
            else:
                print(f'''
                Thank you, {first_name}. 
                Your provided details have been logged into our system.''')
                user_name.append(password) # add password to user_name container
                HNG_interns.append(user_name) # add user_name list to overall container

    else:
        print(f'''
        Thank you, {first_name}. 
        Your provided details have been logged into our system.''')
        user_name.append(password) # add password to user_name container
        HNG_interns.append(user_name) # add user_name list to overall container

    user_input = input('''\nIs there anybody else to be added?
    Type YES to add new entrant, or NO to end the program: ''')

    if user_input == "YES":
        response2 = user_input.upper()
        if response2 == "YES" or response2 == "NO":
            break
        else:
            print("Kindly enter a valid response")

    admin_check = True

    if user_input == "No":
        admin_check = False
        for item in HNG_interns:
            print("Thank you. Below are the details of all the added interns: " + item)
            break

    else:
        admin_check = True