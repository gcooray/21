import random

 # Set the range for a random number
MIN_NUM = 1
MAX_NUM = 100
random_number = random.randint(MIN_NUM, MAX_NUM) # Python function to generate a randon number
def valid_guess(): # Define a fucntion
    while True: # Start the loop until user inputs a valid number
        guess = input(f"Enter your guess between {MIN_NUM} and {MAX_NUM}: ")  # Take user input for guess
        if guess.isdigit(): # Check if the guess is an integer
            guess = int(guess) # Convert the guess value to integer value
            if MIN_NUM <= guess <= MAX_NUM: # Verify if the guess is within the range
                return guess # If it is within the range it returns the value
            else: # If it is not, it prompts the user to enter a value within the range
                print(f"Please enter a number beetween {MIN_NUM} and {MAX_NUM}")
        else: # If the guess is not an integer, it prompts the user to put a valid integer
            print("Please enter a valid integer:")

while True: # Start the loop
    user_guess = valid_guess() # Make valid_guess fucntion equals to a variable called user_guess
    if user_guess < random_number: # Check if user guess is lower than the random number
        print(f"You answered {user_guess}. The correct answer is higher.") # If it is lower, it displays the message
    elif user_guess > random_number: # Check if user guess is higher than the random number
        print(f"You answered {user_guess}. The correct answer is lower.") # If it is higher, it displays the message
    else: # If none of the above applies
        print(f"You answered {user_guess}. This is the correct answer.") # It displays the message.
    break # The loop beeaks if the correct answer is given