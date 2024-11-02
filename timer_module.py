import time
import sys

import sys
import time

def timer(stop_event, resume_event, bonus_round):

    # Set timer duration based on bonus round status
    time_limit = 60 if bonus_round else 30
    i = time_limit

    while i > 0 and not stop_event.is_set():
        # Check if resume_event is set, allowing countdown to continue
        if resume_event.is_set():  
            sys.stdout.write(f"\rTime left: {i} seconds  {'Write your answer: ' if bonus_round else 'Lock in your answer: '}")
            sys.stdout.flush()
            time.sleep(1)
            i -= 1
        else:
            # Pause the countdown by sleeping in short intervals while waiting to resume
            time.sleep(0.1)

    # When timer expires naturally, or stop_event is set
    if not stop_event.is_set():  
        if bonus_round:
            sys.stdout.write("\nTimes up!! Bonus Round Finished\n")
        else:
            sys.stdout.write("\nTimes up! Unfortunately, that counts as a wrong answer.\n")
        sys.stdout.flush()
        stop_event.set()  # Signal that time has expired
