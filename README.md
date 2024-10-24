# Brain-Blitz

**Brain Blitz** is a fast-paced trivia quiz game built in Python where players answer multiple-choice questions to climb the prize ladder. The game incorporates lifelines, called "Hints," that help players eliminate incorrect answers. Test your knowledge and strategy while racing against time to reach the top!

## Table of Contents
- [Game Features](#game-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Game Features

- **Multiple-choice questions**: Answer a set of questions, each with four options.
- **Hint System**: Use "Hints" to eliminate wrong answers and improve your chances of winning.
- **Bonus Rounds**: Earn additional Hints with bonus rounds.
- **Super Hint**: Get help from a companion in tough situations.
- **Dynamic Prize Ladder**: Progress through prize levels by answering correctly, with a maximum prize of €75,000.
- **Fast-Paced Gameplay**: Timed rounds create urgency and excitement.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/brain-blitz.git
    ```

2. Navigate to the project directory:

    ```bash
    cd brain-blitz
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the game:

    ```bash
    python brain_blitz.py
    ```

## How to Play

1. Upon starting the game, you will be presented with a series of trivia questions.
2. Each question will have four possible answers. Select the correct one to progress.
3. You have **Hints** to use, which eliminate incorrect answers:
    - Use a Hint when you're uncertain to improve your odds.
4. The goal is to answer all questions correctly and reach the final prize level.
5. Bonus rounds provide opportunities to win more Hints.

### Controls
- Type the letter corresponding to your answer (A, B, C, or D) to submit your response.
- Press 'H' to use a Hint.

## Game Rules

- You begin the game with 7 Hints.
- For each correct answer, you progress up the prize ladder.
- For each wrong answer, you lose 3 Hints. If you're out of Hints, you fall down the prize ladder.
- Use your Hints wisely to eliminate incorrect answers and get closer to the prize.
- Answer all 15 questions to win the maximum prize of €75,000.

## Future Improvements

- **Leaderboard**: Add a system to track high scores.
- **Question Categories**: Allow players to choose categories of questions (e.g., Science, History).
- **Multiplayer Mode**: Implement a feature where players can compete against each other.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

**Brain Blitz** is inspired by the Portuguese game show *Joker*, aired on RTP1. While Brain Blitz is an original creation, it borrows key elements from *Joker*, such as the use of lifelines (here referred to as "Hints") and the structure of a progressive prize ladder. Special thanks to the creators of *Joker* for the inspiration!
