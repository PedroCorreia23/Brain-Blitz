from gameRules import rules
import questions

def main():
    print("****WELCOME TO BRAIN BLITZ****")
    while True:
        user_input = input("Is this your first time playing? (y/n): ").lower()
        if user_input == "y":
            print(rules())
            ready()
            game()  # Automatically start the game after displaying the rules
            break
        elif user_input == "n":
            game()  # Skip the rules and start the game
            ready()
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def ready():
    user_input = input("Press ENTER when you are ready to play\n")

    while user_input != "":  
        user_input = input() 

def game():

    n_question = 0
    print("Starting the game...")

    while n_question < 12:
         
        if question:
                    print(question['question'])
                    print("Choices:")
                    for idx, choice in enumerate(question['choices'], 1):
                            print(f"{idx}. {choice}")


main()