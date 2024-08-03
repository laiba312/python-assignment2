def get_list_from_user():
    # Initialize an empty list to store user inputs
    user_list = []

    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # Check if the input is an empty string (user pressed Enter without typing anything)
        if value == "":
            break
        
        # Add the entered value to the list
        user_list.append(value)
    
    # Print the final list
    print("Here's the list:", user_list)

# Call the function to execute
get_list_from_user()
