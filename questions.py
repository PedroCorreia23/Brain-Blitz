import random
import threading

from timer_module import *

def load_bonus_questions():
    with open('bonus_questions.txt', 'r', encoding='utf-8') as file:
            
        bonus_questions = []
        for line in file: 
            line = line.strip()

            if line.startswith("[") and line.endswith("]"):
                    round = line  # Save the category
                    continue
            
            parts = line.split('|') 
            if len(parts) == 4:
                question = parts[0]
                choices = parts[1:3]
                correct_answer = parts[3]

                bonus_questions.append({
                    'round': round,
                    'question': question,
                    'choices': choices,
                    'correct_answer': correct_answer
                })

    return bonus_questions

def load_questions():
    with open('questions.txt', 'r', encoding='utf-8') as file:
            
        questions = []

        for line in file: 
            line = line.strip()

            if line.startswith("[") and line.endswith("]"):
                    category = line  # Save the category
                    continue
            
            parts = line.split('|') 
            if len(parts) == 6:
                question = parts[0]
                choices = parts[1:5]
                correct_answer = parts[5]

                questions.append({
                    'category': category,
                    'question': question,
                    'choices': choices,
                    'correct_answer': correct_answer
                })

    return questions

def get_easy_q(questions):
    return [q for q in questions if q['category'] == "[Easy]"]

def get_med_q(questions):
    return [q for q in questions if q['category'] == "[Medium]"]

def get_hard_q(questions):
    return [q for q in questions if q['category'] == "[Hard]"]

def get_super_hard_q(questions):
    return [q for q in questions if q['category'] == "[Super Hard]"]

def get_random_question(questions, difficulty):
    if difficulty == "easy":
        return random.choice(get_easy_q(questions))
    elif difficulty == "medium":
        return random.choice(get_med_q(questions))
    elif difficulty == "hard":
        return random.choice(get_hard_q(questions))
    elif difficulty == "super hard":
        return random.choice(get_super_hard_q(questions))
    return None

def question_num(n_question):
    positions = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th and Last"]

    if n_question < len(positions):
        print(positions[n_question] + " question")

bonus_questions = load_bonus_questions()
def print_bonus_questions(bonus_questions, round_number):
    count = 0
    hints_gained = 0
    correct_answers = 0

    # Filter questions for the specified bonus round
    filtered_questions = [item for item in bonus_questions if item['round'] == f"[{round_number}]"]

    # Events to control the timer
    stop_event = threading.Event()
    resume_event = threading.Event()
    resume_event.set()  # Start with the timer active

    # Start the timer thread for the entire duration of the bonus round
    timer_thread = threading.Thread(target=timer, args=(stop_event, resume_event, True))
    timer_thread.start()

    for item in filtered_questions:
        if count >= 10 or stop_event.is_set():  # Stop if timer runs out or if 10 questions are answered
            break
         
        print(f"\nRound: {item['round']}")
        print(f"Question: {item['question']}")
        for choice in item['choices']:
            print(choice)

        # Wait for user input or until timer expires
        answer = input("").upper() if not stop_event.is_set() else None

        if answer == item['correct_answer']:
            print("Correct Answer!")
            correct_answers += 1
        else:
            print("Wrong Answer!")
        
        count += 1

    # Ensure the timer thread stops
    stop_event.set()  # Signal timer to stop if the bonus round is complete
    timer_thread.join()

    # Set hints_gained based on correct answers
    if correct_answers >= 5 and correct_answers < 10:
        hints_gained = 1
    elif correct_answers == 10:
        hints_gained = 2

    return hints_gained, correct_answers