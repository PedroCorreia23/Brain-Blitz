import time
import sys

def timer(stop_event, bonus_round):
    
    if bonus_round == False:
        i = 30
        while i > 0 and not stop_event.is_set():
            sys.stdout.write(f"\rTime left: {i} seconds  Lock in your answer: ")
            sys.stdout.flush()
            time.sleep(1)
            i -= 1

        if not stop_event.is_set():  # If the stop event was not set before time runs out
            sys.stdout.write("\nTimes up! Unfortunately, that counts as a wrong answer.\n")
            sys.stdout.flush()
            stop_event.set()    # Signal that time has expired
    else:
        i = 60
        while i > 0 and not stop_event.is_set():
            sys.stdout.write(f"\rTime left: {i} seconds  Write your answer: ")
            sys.stdout.flush()
            time.sleep(1)
            i -= 1

        if not stop_event.is_set():  # If the stop event was not set before time runs out
            sys.stdout.write("\nTimes up!! Bonus Round Finished\n")
            sys.stdout.flush()
            stop_event.set()    # Signal that time has expired