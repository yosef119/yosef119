# Program to check if the entered username is valid or not
# Get the usernames from the user
username_1 = input("Enter the user name: ")
username_2 = input("Reenter the user name: ")

# Check if both entered usernames are the same
if username_1 == username_2:
    print("User name is Valid")
else:
    print("User name is Invalid")
