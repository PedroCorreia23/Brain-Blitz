import time
import sys
'''
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

'''
def timer(stop_event, resume_event, bonus_round):

    time_limit = 30 if not bonus_round else 60
    i = time_limit

    while i > 0 and not stop_event.is_set():
        if resume_event.is_set():  # Check if we're allowed to run
            sys.stdout.write(f"\rTime left: {i} seconds  Lock in your answer: ")
            sys.stdout.flush()
            time.sleep(1)
            i -= 1
        else:
            time.sleep(0.1)  # Small delay to reduce CPU usage when paused

    if not stop_event.is_set():  # Only display timeout message if time expired naturally
        sys.stdout.write("\nTimes up! Unfortunately, that counts as a wrong answer.\n")
        sys.stdout.flush()
        stop_event.set()  # Signal that time has expired