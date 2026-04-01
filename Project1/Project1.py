import random
import string
import hashlib

# Takes a string and returns a hex digest sha256 
def hash_pw(password):
    # takes password
    hashed = hashlib.sha256(password.encode()).hexdigest() 
    # hashlib.sha256() to create hash
    return hashed # returns hex digest

# Generate and return a random password 
def generate_pw(length):
    pw_chars = []
    all_chars = string.ascii_letters + string.digits + "!" + "@" + "#"+"$" + "*"
    for i in range(length):
        pw_chars.append(random.choice(all_chars))
    return ''.join(pw_chars)

# Takes a hashed password, asks user for a password, hases it and checks it against the given password
def verify_login(stored_password):
    given_password = input("Enter your password: ") 
    given_password = hash_pw(given_password)
    if given_password == stored_password: 
        print("Access Granted")
    else: 
        print("Access Denied")
        select = input("Forgot/Reset password? Y or N: ")
        if select == "Y": 
            secure_password = store_password(create_password())
        else:
            exit()

# Function to prompt user to create or generate a password at a given length.
def create_password():
    print("Would you like to:")
    print("1. Create your own password")
    print("2. Generate one for you")
    option = int(input("Make a selection: ")) 
    if option == 1: 
        password = input("Type your password: ")
        return password 
    elif option == 2: 
        try: length = int(input("How many characters would you like your password to be? Dont enter anything for defult: "))
        except: length = 8
        password = generate_pw(length)
        print(f"Here is the one time to show the password: {password}")
        return password
    else:
        print("Invalid Entry")
    
  

def store_password(password):
    secure_password = hash_pw(password)
    return secure_password




def access_page():
    print("*"*50)
    print("User Log In Screen")
    print("*"*50)
    print("Lets gather some information for the program...")
    Name = input("What is your name?: ")
    print(f"Hello {Name}")
    secure_password = store_password(create_password())
    verify_login(secure_password)
    print("\n")
    return Name 

def tip_calculator():
    print(" ")
    print("Tip Calculator")
    try:
        meal_price = float(input("What is the price of the meal? "))
    except:
        print("Invalid")
        meal_price = float(input("What is the price of the meal? "))

    try:
        tax_rate = float(input("What is the tax rate? "))
        if tax_rate > 1:
            tax_rate = tax_rate / 100
    except:
        print("Invalid")
        tax_rate = float(input("What is the tax rate? "))

    try:
        discount_percent = float(input("What is the discount percentage? "))
        if discount_percent >1:
            discount_percent = discount_percent / 100
    except:
        print("Invalid")
        discount_percent = float(input("What is the discount percentage? "))

    try:
        tip_percent = float(input("What is the tip percentage? "))
        if tip_percent > 1:
            tip_percent = tip_percent /100
    except:
        print("Invalid")
        tip_percent = float(input("What is the tip percentage? "))



    def calculate_tip (meal , tax, tip, dis):
        tax = meal * tax
        tip = meal * tip
        dis = (meal + tax) * dis
        total = meal + tax - dis + tip 
        print(
            f"Subtotal: ${meal:.2f}",
            f"Tax: ${tax:.2f}",
            f"Discount: ${dis:.2f}",
            f"Tip: ${tip:.2f}",
            f"Total: ${total:.2f}",
            sep="   "
            )

    calculate_tip(meal_price, tax_rate, tip_percent, discount_percent)

def word_repeat():
    print(" ")
    print("Word Repeater")
    word = input("What word would you like to repeat? ")
    times = int(input("How many times would you like to repeat it? "))

    banner = " | ".join([word] * times) + "🎉"
    print(banner)

def number_sort():
    return 0


def calc ():
    print(" ")
    print("Calculator")
    first = float(input("What is the first number? "))
    sym = input("what is the math operation? +, -, *, /, // (largest posible division), or % (Modulo (remainder after division))")
    second = float(input("What is the second number? "))

    def calculate(a, b, c):
        if b == "+":
            return a + c
        if b == "-":
            return a- c
        if b == "*":
            return a * c
        if b == "/":
            return a / c
        if b == "//":
            return a // c
        if b == "%":
            return a % c

    result = calculate(first, sym, second)

    print(f"{first}{sym}{second} = {result}")
def task_list():
    print("\nWelcome to TASK LIST!\n")
    tasks = []

    def create_task(task_list):
        title = input("What is the task title?")
        task = {
        'title': title,
        'done' : False
           }
        task_list.append(task)

    def show_list(task_list):
        if not task_list:
            print("No Tasks!")
        else:
            print("\nTask List:")
            for idx, task in enumerate(task_list, 1):
                status = "✓" if task['done'] else "✗"
                print(f"{idx}, {task['title']} [{status}]")


    def complete_task(task_list):
        show_list(task_list)
        index = int(input("What item would you like to mark completed? "))
        if 1 <= index <= len(task_list):
            task_list[index -1]['done']= True
        else :
            print("That is not a valid task number")


    def menuL():
        while True:
            print("\nList Menu:\n1: Add Task\n2: Complete Task\n3: List Tasks\n4: Exit")
            selection = input("Make a selection: ")
            if selection == "1": # Add Task
                create_task(tasks)
                continue
            elif selection == "2": # Complete Task
                complete_task(tasks)
                continue
            elif selection == "3": # List Task
                show_list(tasks)
                continue
            elif selection == "4": # Exit
                break
            else:
                print("Invalid selection.")
    menuL()

def year_check():
    try:
        age = int(input("What is your age? "))
        print(f"Your age next year will be: {age + 1}")
    except:
        print("Invalid")

def backwords():
    word = input("What word would you like to reverse?: ")
    flip = word[::-1]
    print("Flipped:",flip)

def scramble():
    word = input("In sert a word to scramble: ")
    
def number_sort():
    numbers = input("Enter numbers separated by spaces: ")
    lnumbers = numbers.split()
    nums = []
    for lnumber in lnumbers:
        nums.append(lnumber)
        int(lnumber)
    num_sort = sorted(nums)
    print(num_sort)

    scores = [10, 40, 25, 40]

  
def closing():
        print("~"*44)
        print("Thank you for trying this out! ")
        print("Xavier Harris 2026 Python Portfolio")
        print("~"*44)
        


def header(Name):
    print("~"*44)
    print(" "*10 + f"Welcome {Name} to my portfolio!")
    print("~"*44)
    print(f"These are the basic programs I have created. Make a selection and let's have some fun!")
    print("~"*44)
    print("1. Tip calculator (Use to figure out your tip and totals)")
    print("2. Word repeater (Repeats given word given times fallowed by a little celebration!)")
    print("3. Calculation (A calculator showing some basic computer math)")
    print("4. Task List (Crate and manage a list of tasks)")
    print("0. to Exit")


def menu(Name):
    while True:  
        header(Name)
        selection = int(input("What program would you like to try out?: "))
        if selection == 1:
            tip_calculator()
            print("Returning to Menu"+"."*6)
        elif selection == 2:
            word_repeat()
            print("Returning to Menu"+"."*6)
        elif selection == 3:
            calc()
            print("Returning to Menu"+"."*6)
        elif selection == 4:
            task_list()
            print("Returning to Menu"+"."*6)
        elif selection == 0:
            break
        else:
            print("Invalid entry")
        print(" ")
    closing()

 
menu(access_page())