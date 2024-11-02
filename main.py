from gameRules import rules
from test_questions import *
from timer_module import *

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
            ready()
            game()  # Skip the rules and start the game
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def ready():
    user_input = input("Press ENTER when you are ready to play\n")

    while user_input != "":  
        user_input = input() 

def game():
    hints = 7
    level = 0
    money_levels = ["0€", "200€", "500€", "1000€", "3000€", "10000€", "50000€"]
    n_question = 0
    questions = load_questions()  
    difficulty = ["easy", "medium", "hard", "super hard"]
    incorrect_choices = []
    print("Starting the game...\n")

    while n_question < 12:

        if n_question == 1:
            hints_gained= bonus_round(1)
            hints += hints_gained
            print(f"You have now {hints} hints.\n")
        elif n_question == 3:
            hints_gained= bonus_round(2)  
            hints += hints_gained
            print(f"You have now {hints} hints.\n")

        question_num(n_question)

        # Choose difficulty based on question number
        if level <= 2:
            question = get_random_question(questions, difficulty[0])
        elif level == 3 or level == 4:
            question = get_random_question(questions, difficulty[1])
        elif level == 5 or level == 6:
            question = get_random_question(questions, difficulty[2])
        else:
            question = get_random_question(questions, difficulty[3])

        if question:
            print(question['question'])
            print("Choices:")
            for idx, choice in enumerate(question['choices'], 1):
                print(f"{idx}. {choice}")

            # Events for managing the timer and its pausing
            stop_event = threading.Event()
            resume_event = threading.Event()
            resume_event.set()  # Start with the timer running
            
            # Start the timer in a separate thread
            timer_thread = threading.Thread(target=timer, args=(stop_event, resume_event, False))
            timer_thread.start()
            
            answer = None
            while not stop_event.is_set():
                try:
                    # Check if the user inputs a valid answer before time expires
                    answer = input().upper()
                    if answer in ['A', 'B', 'C', 'D']:
                        stop_event.set()  # Stop the timer if a valid answer is provided
                        break
                    elif answer == "H":
                        print("Hint used!")
                        hints, incorrect_choices = eliminate_incorrect_options(question, hints, incorrect_choices, resume_event)
                    elif not stop_event.is_set():
                        print("Invalid input! Enter A, B, C, or D, or press H to use a Hint.")
                except EOFError:
                    # Handle unexpected end-of-input
                    break

            # Wait for the timer thread to finish
            timer_thread.join()
            
            # Evaluate answer after timer ends or input is given
            if stop_event.is_set() and answer in ['A', 'B', 'C', 'D']:
                if answer == question['correct_answer']:
                    level = min(level + 1, len(money_levels) - 1)
                    print(f"Congratulations! You got it right! The correct answer is {question['correct_answer']}.\n")
                else:
                    # Handle penalties based on hints
                    hints, level = apply_penalty(hints, level)
                    print(f"That's incorrect!\nThe correct answer was {question['correct_answer']}. Better luck next time!\n")
            else:
                print("Moving on to the next question\n")
                hints, level = apply_penalty(hints, level)

            print(f"Numero de Hints: {hints}\nMoney Level: {money_levels[level]}\n")
            n_question += 1

def bonus_round(n_bonus_round):

    if n_bonus_round == 1:
        print("*" * 25, "\n****FIRST BONUS ROUND****", "\n" + "*" * 25)
        print("!!!ATTENTION!!!\nWriting the answer with orthographic errors will count as a wrong answer!!!")

        ready()
        hints_gained, correct_answers = print_bonus_questions(bonus_questions, n_bonus_round)
        
        if hints_gained > 0:
            print(f"Congratulations you got {correct_answers} correct answers, so you won {hints_gained} more hints.")
        else:
            print(f"Sorry, you got {correct_answers} correct answers, so you won {hints_gained} hints. Better luck in the next bonus round.")
    else:
        print("*" * 26, "\n****SECOND BONUS ROUND****", "\n" + "*" * 26)
        print("!!!ATTENTION!!!\nWriting the answer with orthographic errors will count as a wrong answer!!!")
        
        ready()
        hints_gained, correct_answers = print_bonus_questions(bonus_questions, n_bonus_round)

        if hints_gained > 0:
            print(f"\nCongratulations you got {correct_answers} correct answers, so you won {hints_gained} more hints.")
        else:
            print(f"\nSorry, you got {correct_answers} correct answers, so you won {hints_gained} hints this round.\n Now let's get ready for the last questions of the game.")

    # Return hints gained and correct answers to be used in the game function
    return hints_gained

def apply_penalty(hints, level):
    if hints >= 3:
        hints -= 3
    elif hints == 2:
        hints -= 2
        level -= 1
    elif hints == 1:
        hints -= 1
        level -= 2
    elif hints == 0:
        level -= 3

    if level < 0:
        level = 0
                    
    
    return hints, level

def eliminate_incorrect_options(question, hints, incorrect_choices, resume_event):
    if hints <= 0:
        print("No hints available.")
        return hints, incorrect_choices

    # Pause timer by clearing resume_event
    resume_event.clear()

    # Request user input for two options they want to use the hint on
    while True:
        input_line = input("Enter the two options you're considering (e.g., A B): ").upper()
        options = input_line.split()
        
        # Validate user input
        if len(options) == 2 and all(opt in ['A', 'B', 'C', 'D'] for opt in options):
            option1, option2 = options
            break
        else:
            print("Invalid input! Please enter exactly two options (e.g., A B).")

    hints -= 1  # Deduct a hint

    # Check which option is incorrect and give feedback
    if option1 != question['correct_answer']:
        incorrect_choices.append(option1)
        print(f"Hint used: Option {option1} is incorrect.")
    elif option2 != question['correct_answer']:
        incorrect_choices.append(option2)
        print(f"Hint used: Option {option2} is incorrect.")
        
    # Resume timer by setting resume_event
    resume_event.set()

    return hints, incorrect_choices

main()