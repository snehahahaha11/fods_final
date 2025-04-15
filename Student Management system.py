# Define a class named Project
class Project:
    # Constructor method for the Project class
    def __init__(self):
        # Initialize necessary files if they don't exist
        self.check_files()
   
    def check_files(self):
        """Create necessary files if they don't exist"""
        required_files = ['password.txt', 'adminpassword.txt', 'grades.txt', 'eca.txt']
        for file_name in required_files:
            try:
                # Try to open the file in append mode (creates if doesn't exist)
                with open(file_name, 'a'):
                    pass
            except Exception as e:
                print(f"Error ensuring {file_name} exists: {str(e)}")

    # Static method to validate user credentials
    @staticmethod
    def check_valid(file_path, username, password):
        try:
            # Open the specified file to read credentials
            with open(file_path, 'r') as file:
                # Iterate through each line in the file
                for line in file:
                    if not line.strip():  # Skip empty lines
                        continue
                    # Extract stored username and password from the line
                    try:
                        stored_username, stored_password = line.strip().split(',', 1)
                        # Check if provided username and password match stored credentials
                        if username == stored_username and password == stored_password:
                            return True  # Return True if credentials are valid
                    except ValueError:
                        # Skip malformed lines
                        continue
            return False  # Return False if credentials are invalid
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return False
        except Exception as e:
            print(f"Error validating credentials: {str(e)}")
            return False

    # Method to handle user login
    def login(self):
        # Prompt user to specify whether they are a student or an admin
        user_type = input("Are you a student or an admin? ").lower()
        if user_type not in ['student', 'admin']:
            print("Invalid user type. Please enter 'student' or 'admin'.")
            return None, None
            
        # Determine the file path based on user type
        file_path = 'password.txt' if user_type == 'student' else 'adminpassword.txt'
        # Prompt user for username and password
        user_login = input("Enter your username: ")
        password_login = input("Enter your password: ")
        # Validate credentials
        if self.check_valid(file_path, user_login, password_login):
            # Print a success message if login is successful
            print("Login successful. Welcome, {}!".format(user_type))
            return user_type, user_login  # Return user type and username if successful
        else:
            # Print an error message if login fails
            print("Invalid username or password. Please try again.")
            return None, None  # Return None values if login fails

    # Method to register a new user
    def register_student(self):
        try:
            # Open 'password.txt' file to append new user credentials
            with open('password.txt', 'a') as credentials_file:
                # Prompt user to enter username and password
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                password_confirm = input('Confirm password: ')
                # Check if passwords match and meet minimum length requirement
                if password != password_confirm:
                    print("Passwords don't match, please retype.")
                elif len(password) <= 7:
                    print('Password is too short. It must be at least 8 characters long.')
                else:
                    # Write username and password to the file if all conditions are met
                    credentials_file.write(f"{username},{password}\n")
                    print("User registered successfully!")  # Print success message
        except Exception as e:
            print(f"Error registering user: {str(e)}")

    # Method to register a new admin
    def register_admin(self):
        try:
            # Open 'adminpassword.txt' file to append new admin credentials
            with open("adminpassword.txt", 'a') as credentials_file:
                # Prompt admin to enter username and password
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                password_confirm = input('Confirm password: ')
                # Check if passwords match and meet minimum length requirement
                if password != password_confirm:
                    print("Passwords don't match, please retype.")
                elif len(password) <= 7:
                    print('Password is too short. It must be at least 8 characters long.')
                else:
                    # Write admin username and password to the file if all conditions are met
                    credentials_file.write(f"{username},{password}\n")
                    print("Admin registered successfully!")  # Print success message
        except Exception as e:
            print(f"Error registering admin: {str(e)}")

    # Method to add marks for a student
    def add_grades(self):
        try:
            # Prompt user to enter student's information and marks
            student_name = input("Enter student's name: ")
            
            try:
                data_science = float(input("Enter the marks of DataScience: "))
                it = float(input('Enter the marks of IT: '))
                fom = float(input("Enter the marks of FOM: "))
                academic_english = float(input("Enter the marks of Academic English: "))
                itf = float(input('Enter the marks of ITF: '))
            except ValueError:
                print("Error: Marks must be numeric values.")
                return
                
            # Open 'grades.txt' file to append student's marks
            with open('grades.txt', 'a') as grade_file:
                # Write student's marks to the file
                grade_file.write(f"{student_name}: Datascience: {data_science}, IT: {it}, FOM: {fom}, Academic English: {academic_english}, ITF: {itf}\n")
            print('Marks added successfully!')  # Print success message
        except Exception as e:
            print(f"Error adding marks: {str(e)}")

    # Method to add extra-curricular activities for a student
    def add_eca(self):
        try:
            # Open 'eca.txt' file to append extra-curricular activity details
            with open('eca.txt', 'a') as eca_file:
                # Prompt user to enter student's username and ECA details
                std = input("Enter student's username: ")
                sports = input("Interested sport: ")
                club = input("Joined clubs: ")
                services = input('Engaged in any services: ')
                more = input('Any other activities done: ')
                # Write student's ECA details to the file
                eca_file.write(f'Username: {std}\nSports joined: {sports}\nClubs joined: {club}\nServices: {services}\nMore: {more}\n\n')
                print('ECA details added successfully!')  # Print success message
        except Exception as e:
            print(f"Error adding ECA details: {str(e)}")

    # Method to view extra-curricular activities of a student
    def view_eca(self):
        try:
            # Prompt user to enter student's username
            username = input("Enter student's username: ")
            
            # Check if the eca.txt file exists and has content
            try:
                with open('eca.txt', 'r') as eca_file:
                    # Read all lines from the file
                    eca_data = eca_file.readlines()
                    
                    if not eca_data:
                        print("No ECA details found. The file is empty.")
                        return
                        
                    found = False  # Flag to track if student's ECA details are found
                    # Iterate through each line in ECA data
                    for i, line in enumerate(eca_data):
                        # Check if the line starts with 'Username:'
                        if line.strip().startswith('Username:'):
                            # Extract the username from the line
                            line_username = line.strip().split(': ', 1)[1] if ': ' in line else ""
                            # If the username matches, print the student's ECA details
                            if line_username == username:
                                found = True  # Set flag to True
                                print("\nStudent's ECA details:")
                                # Determine how many lines to print
                                end_index = i + 5
                                if i + 5 < len(eca_data):
                                    # Check for a blank line indicating the end of this student's entry
                                    for j in range(i, len(eca_data)):
                                        if j < len(eca_data) and eca_data[j].strip() == '':
                                            end_index = j
                                            break
                                
                                # Print the lines from the username to the determined end
                                for j in range(i, min(end_index, len(eca_data))):
                                    print(eca_data[j].strip())
                                break  # Exit loop once details are printed
                    
                    # If student's ECA details are not found, print a message
                    if not found:
                        print("No ECA details found for the given username.")
            except FileNotFoundError:
                print("No ECA details found. The file does not exist.")
                
        except Exception as e:
            print(f"Error viewing ECA details: {str(e)}")

    # Method to delete a user
    def delete_student(self):
        try:
            # Prompt user to enter the username of the user to be deleted
            username = input("Enter the username of the user you want to delete: ")
            
            try:
                # Open 'password.txt' file to read user credentials
                with open('password.txt', 'r') as file:
                    lines = file.readlines()  # Read all lines from the file
                
                # Check if any user with the given username exists
                found = False
                for line in lines:
                    if line.strip() and line.split(',')[0] == username:
                        found = True
                        break
                
                if not found:
                    print(f"No user found with username '{username}'.")
                    return
                
                # Open 'password.txt' file again to write updated user credentials
                with open('password.txt', 'w') as file:
                    # Iterate through each line in the file
                    for line in lines:
                        # Skip empty lines
                        if not line.strip():
                            continue
                        # Write the line to the file if the username does not match
                        if not line.startswith(username + ','):
                            file.write(line)
                
                print(f"User '{username}' deleted successfully.")  # Print success message
            except FileNotFoundError:
                print("Error: password.txt file not found.")
                
        except Exception as e:
            print(f"Error deleting user: {str(e)}")

    # Method to display marks of all students
    def view_marks(self):
        try:
            # Check if the grades.txt file exists
            try:
                with open('grades.txt', 'r') as grade_file:
                    content = grade_file.read().strip()
                    if not content:
                        print("No grades available. The file is empty.")
                        return
                        
                    print("\nStudent's marks:")
                    # Iterate through each line in the file and print the marks
                    for line in content.split('\n'):
                        print(line.strip())
            except FileNotFoundError:
                print("No grades available. The file does not exist.")
                
        except Exception as e:
            print(f"Error displaying marks: {str(e)}")

# Create an instance of the Project class
project = Project()

# Main program loop
while True:
    try:
        print("\n===== Student Management System =====\n")
        print("1. Login")
        print("2. Register as a user")
        print("3. Register as an admin")
        print("4. Exit\n")
        
        # Prompt user to enter their choice
        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        # Perform actions based on user's choice
        if choice == 1:
            user_type, username = project.login()
            if user_type:
                if user_type == 'student':
                    while True:
                        print("\n===== Student Panel =====\n")
                        print("Welcome to the Student Profile Management System\n")
                        print("1. Display ECA activities")
                        print("2. Show grades")
                        print("3. Logout and Return to main menu\n")
                        
                        try:
                            input_choice = int(input("Enter your choice: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                            
                        if input_choice == 1:
                            project.view_eca()
                        elif input_choice == 2:
                            project.view_marks()
                        elif input_choice == 3:
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            
                elif user_type == 'admin':
                    while True:
                        print("\n===== Admin Panel =====")
                        print("Welcome to the Student Profile Management System\n")
                        print("1. Add New Student")
                        print("2. Delete Student")
                        print("3. Add grades to a student")
                        print("4. Add ECA activities details to a student")
                        print("5. Logout and Return to main menu")
                        
                        try:
                            input_choice = int(input("Enter your choice: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                            
                        if input_choice == 1:
                            project.register_student()
                        elif input_choice == 2:
                            project.delete_student()
                        elif input_choice == 3:
                            project.add_grades()
                        elif input_choice == 4:
                            project.add_eca()
                        elif input_choice == 5:
                            break
                        else:
                            print("Invalid choice. Please try again.")
        elif choice == 2:
            project.register_student()
        elif choice == 3:
            project.register_admin()
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  # Print an error message if choice is invalid
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")