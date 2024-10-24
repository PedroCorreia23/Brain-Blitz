from gameRules import rules

def main():
    print("****WELCOME TO BRAIN BLITZ****")
    while True:
        user_input = input("Is this your first time playing? (y/n): ").lower()
        if user_input == "y":
            print(rules())
            game()  # Automatically start the game after displaying the rules
            break
        elif user_input == "n":
            game()  # Skip the rules and start the game
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def game():
    print("Starting the game...")

main()