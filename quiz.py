def register_user():
    print("Welcome to the Registration System!")
    
    # Get user details
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
    college_name = input("Enter your College Name: ")

    # Validate DOB format
    try:
        day, month, year = map(int, dob.split('/'))
        if day < 1 or day > 31 or month < 1 or month > 12 or len(str(year)) != 4:
            raise ValueError
    except ValueError:
        print("Invalid DOB format! Please use DD/MM/YYYY.")
        return

    # Store user details in a dictionary
    user_data = {
        'Username': username,
        'Email': email,
        'Password': password,
        'Date of Birth': dob,
        'College Name': college_name
    }

    # Save this data to a file (or database)
    with open("user_data_with_college.txt", "a") as file:
        file.write(f"{username},{email},{password},{dob},{college_name}\n")

    print("\nRegistration successful!")
    print("Your registration details:")
    print(user_data)

# Call the function to start the registration process
register_user()
def login_user():
    print("Welcome to the Login System!")

    # Read the stored user data from the file
    try:
        with open("user_data_with_college.txt", "r") as file:
            stored_data = file.read().splitlines()
    except FileNotFoundError:
        print("No registered users found. Please register first.")
        return

    if not stored_data:
        print("No registered users found. Please register first.")
        return

    # Ask for email and password
    login_email = input("Enter your email: ")
    login_password = input("Enter your password: ")

    # Validate the credentials
    for user in stored_data:
        username, email, password, dob, college_name = user.split(',')
        if login_email == email and login_password == password:
            print("\nLogin successful!")
            print(f"Welcome back, {username}!")
            print(f"Your details:")
            print(f"Date of Birth: {dob}")
            print(f"College: {college_name}")
            return

    print("\nInvalid email or password. Please try again.")

# Call the function to start the login process
login_user()
def main():
    action = input("Do you want to (r)egister or (l)ogin? ").lower()
    if action == 'r':
        register_user()
    elif action == 'l':
        login_user()
    else:
        print("Invalid option. Please choose 'r' to register or 'l' to login.")

# Run the main program
main()
# Question Bank
quiz_questions = {
    "DBMS": [
        {
            "question": "What is a primary key in a database?",
            "options": [
                "A key that uniquely identifies a record in a table.",
                "A key that is used to encrypt the database.",
                "A duplicate key in a table.",
                "None of the above."
            ],
            "answer": "A key that uniquely identifies a record in a table."
        },
        {
            "question": "Which of the following is a DML (Data Manipulation Language) command?",
            "options": ["CREATE", "DELETE", "ALTER", "DROP"],
            "answer": "DELETE"
        },
        {
            "question": "Which of these is not a type of database normalization?",
            "options": ["1NF", "2NF", "3NF", "5FF"],
            "answer": "5FF"
        },
        {
            "question": "What is the purpose of the ACID properties in a database?",
            "options": [
                "To ensure database recovery and consistency.",
                "To provide faster data retrieval.",
                "To optimize queries.",
                "To create indexes."
            ],
            "answer": "To ensure database recovery and consistency."
        },
        {
            "question": "Which SQL clause is used to sort the result set?",
            "options": ["GROUP BY", "SORT BY", "ORDER BY", "FILTER BY"],
            "answer": "ORDER BY"
        }
    ],
    "DSA": [
        {
            "question": "Which data structure is used for implementing recursion?",
            "options": ["Queue", "Stack", "Array", "Linked List"],
            "answer": "Stack"
        },
        {
            "question": "What is the time complexity of searching in a binary search tree (BST)?",
            "options": ["O(log n)", "O(n)", "O(n log n)", "O(1)"],
            "answer": "O(log n)"
        },
        {
            "question": "Which sorting algorithm is the fastest in the average case?",
            "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"],
            "answer": "Quick Sort"
        },
        {
            "question": "Which of these is a divide-and-conquer algorithm?",
            "options": ["Merge Sort", "Heap Sort", "Bubble Sort", "Insertion Sort"],
            "answer": "Merge Sort"
        },
        {
            "question": "What is the maximum number of nodes at level k of a binary tree?",
            "options": ["2^k", "2^(k+1)", "k^2", "k"],
            "answer": "2^k"
        }
    ],
    "Python": [
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".py", ".python", ".pyt", ".pt"],
            "answer": ".py"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": "def"
        },
        {
            "question": "What is the output of print(2**3)?",
            "options": ["6", "8", "9", "16"],
            "answer": "8"
        },
        {
            "question": "Which of these data types is immutable in Python?",
            "options": ["List", "Dictionary", "Set", "Tuple"],
            "answer": "Tuple"
        },
        {
            "question": "What does len() function do in Python?",
            "options": [
                "Returns the number of elements in an object",
                "Returns the length of a string",
                "Counts the number of characters",
                "All of the above"
            ],
            "answer": "All of the above"
        }
    ]
}

# Quiz Function
def run_quiz(subject):
    print(f"\nStarting Quiz on {subject}!\n")
    questions = quiz_questions[subject]
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        answer = input("Your answer: ")
        
        # Check answer and increment score
        if answer.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")

    # Display final score
    print("\n================== QUIZ RESULT ==================")
    print(f"Your final score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")
    # Grade calculation
    if percentage == 100:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"
    print(f"Grade: {grade}")
    print("=================================================\n")

# Main Program
def main():
    print("Welcome to the Quiz Application!")
    print("Choose a subject:")
    print("1. DBMS")
    print("2. DSA")
    print("3. Python")
    
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        run_quiz("DBMS")
    elif choice == "2":
        run_quiz("DSA")
    elif choice == "3":
        run_quiz("Python")
    else:
        print("Invalid choice. Exiting the application.")

# Run the program
main()
all code data store file
