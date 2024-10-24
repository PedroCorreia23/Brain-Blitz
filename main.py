from gameRules import rules

def main():

    print("****WELCOME TO BRAIN BLITZ****")
    user_input = input("Is this your first time playing?(y/n): ")
    if user_input == "y":
        print(rules())
    else:
        game()

def game():

    hints = 7
    prize = 0
    

main()