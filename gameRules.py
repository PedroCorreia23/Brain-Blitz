def rules():
    
    #This function explains the rules of the Brain Blitz quiz game, based on the game's format.
    
    rules_text = """
    Welcome to Brain Blitz! In this quiz game, a single contestant answers 12 general knowledge questions 
    to win up to €50,000. Here's how the game works:

    1. **Questions**: The contestant faces 12 questions, and for each question, they must select the correct answer 
       from multiple choices within a time limit. The first few questions have a 30-second limit, and as the contestant 
       progresses, the time increases.

    2. **Hints**: The contestant has 7 Hints. Each Hint can eliminate one incorrect answer from the available options.
        The contestant can use multiple Hints on a single question if needed.

    3. **Losing Hints**: If the contestant answers incorrectly, they lose three Hints. If they have fewer than three, 
       they will lose all remaining Hints and drop levels on the prize ladder. If no Hints are left, the contestant 
       falls by three levels on the money tree.

    4. **Bonus Round**: After every four questions, the contestant accesses a bonus round. In this round, the contestant 
       has 60 seconds to answer as many quick-fire questions as possible. Each question has only two possible answers, 
       and the contestant must select one of the options. The more correct answers they provide, the more additional 
       Hints they can earn:
       - If the contestant answers 5 questions correctly, they earn 1 additional Hint.
       - If they answer 10 questions correctly, they earn 2 additional Hints.

       The bonus round is designed to help the contestant gather more Hints to use in the main game.

    5. **Money Ladder**: Each correct answer raises the contestant up a money ladder:
       - €0
       - €200
       - €500
       - €1,000
       - €3,000
       - €10,000
       - €50,000 (grand prize)

    6. **Final Question**: On the final 12th question, the contestant can choose not to answer and drop one level on 
       the money ladder, or they can risk it all for a chance to win the grand prize.
    """
    return rules_text



