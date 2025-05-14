# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."

# def modulus(x, y):
#     return x % y

# def exponentiate(x, y):
#     return x ** y

# def floor_divide(x, y):
#     try:
#         return x // y
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."

# def calculator():
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         operator = input("Enter an operator (+, -, *, /, %, **, //): ")

#         if operator == '+':
#             result = add(num1, num2)
#         elif operator == '-':
#             result = subtract(num1, num2)
#         elif operator == '*':
#             result = multiply(num1, num2)
#         elif operator == '/':
#             result = divide(num1, num2)
#         elif operator == '%':
#             result = modulus(num1, num2)
#         elif operator == '**':
#             result = exponentiate(num1, num2)
#         elif operator == '//':
#             result = floor_divide(num1, num2)
#         else:
#             result = "Error: Invalid operator."

#         print("Result:", result)
    
#     except ValueError:
#         print("Error: Invalid input. Please enter numeric values.")

# calculator()

# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def determine_grade(average):
#     if average >= 90:
#         return 'A'
#     elif average >= 80:
#         return 'B'
#     elif average >= 70:
#         return 'C'
#     elif average >= 60:
#         return 'D'
#     else:
#         return 'F'

# def main():
#     marks = []
#     for i in range(1, 6):
#         while True:
#             try:
#                 mark = float(input(f"Enter marks for subject {i}: "))
#                 if 0 <= mark <= 100:
#                     marks.append(mark)
#                     break
#                 else:
#                     print("Please enter a valid mark between 0 and 100.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#     average = calculate_average(marks)
#     grade = determine_grade(average)

#     print(f"\nAverage Marks: {average:.2f}")
#     print(f"Grade: {grade}")

# main()

# import re

# def check_password_strength(password):
#     # Check password length
#     length_check = len(password) >= 8

#     # Check for uppercase and lowercase characters
#     uppercase_check = any(char.isupper() for char in password)
#     lowercase_check = any(char.islower() for char in password)

#     # Check for digits
#     digit_check = any(char.isdigit() for char in password)

#     # Check for special characters
#     special_char_check = bool(re.search(r"[!@#$%^&*]", password))

#     # Determine password strength
#     if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
#         return "Strong"
#     elif length_check and (uppercase_check or lowercase_check) and (digit_check or special_char_check):
#         return "Moderate"
#     else:
#         return "Weak"

# def main():
#     password = input("Enter your password: ")
#     strength = check_password_strength(password)
#     print(f"Password strength: {strength}")

# main()
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def generate_primes(limit):
#     primes = []
#     for num in range(2, limit + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# def main():
#     try:
#         limit = int(input("Enter the upper limit to generate prime numbers: "))
#         if limit < 2:
#             print("Please enter a number greater than or equal to 2.")
#         else:
#             prime_numbers = generate_primes(limit)
#             print(f"Prime numbers up to {limit}: {prime_numbers}")
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

# main()
# Predefined store items with their prices
# store_items = {
#     "apple": 0.5,
#     "banana": 0.3,
#     "milk": 1.2,
#     "bread": 1.5,
#     "chocolate": 2.0
# }

# # Initialize the shopping cart as an empty dictionary
# cart = {}

# def add_item_to_cart(item, quantity):
#     if item in store_items:
#         cart[item] = cart.get(item, 0) + quantity
#         print(f"{quantity} {item}(s) added to the cart.")
#     else:
#         print("Item not found in store.")

# def remove_item_from_cart(item, quantity):
#     if item in cart:
#         if quantity >= cart[item]:
#             cart.pop(item)
#             print(f"{item} removed from the cart.")
#         else:
#             cart[item] -= quantity
#             print(f"{quantity} {item}(s) removed from the cart.")
#     else:
#         print("Item not in cart.")

# def calculate_total_cost():
#     total = 0
#     for item, quantity in cart.items():
#         total += store_items[item] * quantity
#     return total

# def display_cart():
#     if not cart:
#         print("Your cart is empty.")
#     else:
#         print("\nShopping Cart:")
#         for item, quantity in cart.items():
#             print(f"{item.capitalize()}: {quantity} x ${store_items[item]:.2f} = ${store_items[item] * quantity:.2f}")
#         print(f"\nTotal Cost: ${calculate_total_cost():.2f}")

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Add item to cart")
#         print("2. Remove item from cart")
#         print("3. View cart")
#         print("4. Checkout")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == '1':
#             item = input("Enter the item name: ").lower()
#             try:
#                 quantity = int(input("Enter the quantity: "))
#                 if quantity > 0:
#                     add_item_to_cart(item, quantity)
#                 else:
#                     print("Quantity must be positive.")
#             except ValueError:
#                 print("Invalid quantity. Please enter a number.")
        
#         elif choice == '2':
#             item = input("Enter the item name to remove: ").lower()
#             try:
#                 quantity = int(input("Enter the quantity to remove: "))
#                 if quantity > 0:
#                     remove_item_from_cart(item, quantity)
#                 else:
#                     print("Quantity must be positive.")
#             except ValueError:
#                 print("Invalid quantity. Please enter a number.")
        
#         elif choice == '3':
#             display_cart()
        
#         elif choice == '4':
#             display_cart()
#             print("Thank you for shopping!")
#             break
        
#         else:
#             print("Invalid choice. Please select from the menu options.")

# main()

# Initial fixed balance
# balance = 1000.0

# def check_balance():
#     print(f"Your current balance is: ${balance:.2f}")

# def deposit_money(amount):
#     global balance
#     balance += amount
#     print(f"${amount:.2f} deposited successfully.")

# def withdraw_money(amount):
#     global balance
#     if amount > balance:
#         print("Insufficient balance.")
#     else:
#         balance -= amount
#         print(f"${amount:.2f} withdrawn successfully.")

# def atm_menu():
#     while True:
#         print("\nATM Menu:")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
        
#         choice = input("Choose an option (1-4): ")
        
#         if choice == '1':
#             check_balance()
        
#         elif choice == '2':
#             try:
#                 amount = float(input("Enter amount to deposit: "))
#                 if amount > 0:
#                     deposit_money(amount)
#                 else:
#                     print("Deposit amount must be positive.")
#             except ValueError:
#                 print("Invalid input. Please enter a numeric value.")
        
#         elif choice == '3':
#             try:
#                 amount = float(input("Enter amount to withdraw: "))
#                 if amount > 0:
#                     withdraw_money(amount)
#                 else:
#                     print("Withdrawal amount must be positive.")
#             except ValueError:
#                 print("Invalid input. Please enter a numeric value.")
        
#         elif choice == '4':
#             print("Thank you for using the ATM. Goodbye!")
#             break
        
#         else:
#             print("Invalid choice. Please select a valid option.")

# # Start the ATM menu
# atm_menu()
# List to store student records
# students = []

# def add_student():
#     name = input("Enter student name: ")
#     age = input("Enter student age: ")
#     try:
#         age = int(age)
#         grades = input("Enter student grades (comma-separated): ")
#         grades = [float(grade.strip()) for grade in grades.split(',')]
#         student = {"name": name, "age": age, "grades": grades}
#         students.append(student)
#         print(f"Student '{name}' added successfully.")
#     except ValueError:
#         print("Invalid input. Age should be an integer and grades should be numbers.")

# def view_students():
#     if not students:
#         print("No student records found.")
#     else:
#         print("\nStudent Records:")
#         for i, student in enumerate(students, start=1):
#             print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

# def update_student():
#     view_students()
#     try:
#         index = int(input("Enter the student number to update: ")) - 1
#         if 0 <= index < len(students):
#             student = students[index]
#             name = input(f"Enter new name (leave blank to keep '{student['name']}'): ") or student['name']
#             age = input(f"Enter new age (leave blank to keep '{student['age']}'): ")
#             grades = input(f"Enter new grades (leave blank to keep '{student['grades']}'): ")

#             student['name'] = name
#             student['age'] = int(age) if age else student['age']
#             student['grades'] = [float(grade.strip()) for grade in grades.split(',')] if grades else student['grades']

#             print(f"Student '{name}' updated successfully.")
#         else:
#             print("Invalid student number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid student number and numeric values.")

# def delete_student():
#     view_students()
#     try:
#         index = int(input("Enter the student number to delete: ")) - 1
#         if 0 <= index < len(students):
#             removed_student = students.pop(index)
#             print(f"Student '{removed_student['name']}' deleted successfully.")
#         else:
#             print("Invalid student number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid student number.")

# def main():
#     while True:
#         print("\nStudent Records Menu:")
#         print("1. Add a new student")
#         print("2. View all students")
#         print("3. Update a student's information")
#         print("4. Delete a student")
#         print("5. Exit")
        
#         choice = input("Choose an option (1-5): ")
        
#         if choice == '1':
#             add_student()
        
#         elif choice == '2':
#             view_students()
        
#         elif choice == '3':
#             update_student()
        
#         elif choice == '4':
#             delete_student()
        
#         elif choice == '5':
#             print("Exiting the program. Goodbye!")
#             break
        
#         else:
#             print("Invalid choice. Please choose a valid option.")

# # Start the program
# main()

# import random

# def number_guessing_game():
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
    
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
    
#     while True:
#         try:
#             guess = int(input("Enter your guess: "))
#             attempts += 1
            
#             if guess < 1 or guess > 100:
#                 print("Please guess a number between 1 and 100.")
#             elif guess < number_to_guess:
#                 print("Too low! Try again.")
#             elif guess > number_to_guess:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
#                 print(f"It took you {attempts} guesses.")
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# # Start the game
# # number_guessing_game()
# class BankAccount:
#     def __init__(self, account_holder, account_number, balance=0.0):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"${amount:.2f} deposited successfully.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds for withdrawal.")
#         elif amount > 0:
#             self.balance -= amount
#             print(f"${amount:.2f} withdrawn successfully.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def display_account_details(self):
#         print("\nAccount Details:")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Balance: ${self.balance:.2f}")

# # Simulate transactions
# account = BankAccount("John Doe", "123456789")

# # Display initial account details
# account.display_account_details()

# # Deposit money
# account.deposit(500.0)

# # Withdraw money
# account.withdraw(150.0)

# # Attempt to withdraw more than the balance
# account.withdraw(400.0)

# # Display final account details
# account.display_account_details()

# Dictionary to store available books with titles as keys and authors as values
available_books = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen",
    "The Catcher in the Rye": "J.D. Salinger"
}

# Dictionary to keep track of borrowed books
borrowed_books = {}

def view_books():
    if available_books:
        print("\nAvailable Books:")
        for title, author in available_books.items():
            print(f"Title: {title}, Author: {author}")
    else:
        print("\nNo books are currently available.")

def borrow_book(title):
    if title in available_books:
        author = available_books.pop(title)
        borrowed_books[title] = author
        print(f"You have borrowed '{title}' by {author}.")
    elif title in borrowed_books:
        print(f"'{title}' is already borrowed by someone else.")
    else:
        print(f"'{title}' is not available in the library.")

def return_book(title):
    if title in borrowed_books:
        author = borrowed_books.pop(title)
        available_books[title] = author
        print(f"Thank you for returning '{title}'.")
    else:
        print(f"'{title}' was not borrowed from this library.")

def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_books()
        
        elif choice == '2':
            title = input("Enter the title of the book you want to borrow: ")
            borrow_book(title)
        
        elif choice == '3':
            title = input("Enter the title of the book you want to return: ")
            return_book(title)
        
        elif choice == '4':
            print("Exiting the library system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Start the library system
library_menu()



