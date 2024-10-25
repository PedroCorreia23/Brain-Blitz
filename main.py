import threading
import time
import sys

from gameRules import rules
from questions import *

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

def timer(stop_event):
    i = 30
    while i > 0 and not stop_event.is_set():
        sys.stdout.write(f"\rTime left: {i} seconds  Lock in your answer: ")
        sys.stdout.flush()
        time.sleep(1)
        i -= 1

    if not stop_event.is_set():  # If the stop event was not set before time runs out
        sys.stdout.write("\nTimes up! Unfortunately, that counts as a wrong answer.\n")
        sys.stdout.flush()

def game():
    n_question = 0
    questions = load_questions()
    difficulty = ["easy", "medium", "hard", "super hard"]
    print("Starting the game...\n")

    while n_question < 12:
        question_num(n_question)
        # Choose difficulty based on question number
        if n_question < 3:
            question = get_random_question(questions, difficulty[0]) 
        elif n_question >= 3 and n_question < 6:
            question = get_random_question(questions, difficulty[1])  
        elif n_question >= 6 and n_question < 9:
            question = get_random_question(questions, difficulty[2])  
        else:
            question = get_random_question(questions, difficulty[3])

        if question:
            print(question['question'])
            print("Choices:")
            for idx, choice in enumerate(question['choices'], 1):
                print(f"{idx}. {choice}")

            # Event to signal the timer to stop
            stop_event = threading.Event()

            # Start the timer in a separate thread
            timer_thread = threading.Thread(target=timer, args=(stop_event,))
            timer_thread.start()
            
            answer = None
            while True:
                if stop_event.is_set():
                    # Timer has expired, break out of input loop
                    break

                answer = input().upper()
                
                if answer in ['A', 'B', 'C', 'D']:
                    stop_event.set()  # Stop the timer if a valid answer is provided
                    break
                else:
                    print("Invalid input! Please enter A, B, C, or D.")

            # Wait for the timer thread to finish
            timer_thread.join()

            if answer != question['correct_answer']:
                print(f"That's incorrect!\nThe correct answer was {question['correct_answer']}. Better luck next time!\n")
            else:
                print(f"Congratulations! You got it right! The correct answer is {question['correct_answer']}.\n")
            n_question += 1       
                 

main()