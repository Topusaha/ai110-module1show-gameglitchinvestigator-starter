# Number Guessing Game - Expected Logic

## Game Overview
A player tries to guess a secret number within a given range and attempt limit.

## Core Game Rules

### 1. Secret Number Generation
- **WHEN**: At the start of a new game
- **BEHAVIOR**: Generate ONE random number within the difficulty range
- **CRITICAL**: The secret number must STAY THE SAME throughout the entire game
- **STATE**: Should be stored in session state and NOT regenerated on button clicks

### 2. Difficulty Settings
The game offers three difficulty levels:

| Difficulty | Range    | Max Attempts |
|-----------|----------|--------------|
| Easy      | 1-20     | 6            |
| Normal    | 1-100    | 8            |
| Hard      | 1-50     | 5            |

### 3. Guess Validation
When a player submits a guess:
- Accept numeric input (integers or floats converted to int)
- Reject non-numeric input with an error message
- Empty input should show "Enter a guess."

### 4. Guess Comparison Logic
After validating the guess, compare it to the secret:

```
IF guess == secret:
    → Player WINS

IF guess > secret:
    → Hint: "Go LOWER!" (player guessed too high)

IF guess < secret:
    → Hint: "Go HIGHER!" (player guessed too low)
```

**Important**: Hints should help the player converge on the answer!

### 5. Score System
- **Win**: Award points based on how quickly they won
  - Formula: 100 - 10 × (attempts + 1)
  - Minimum 10 points
- **Too High**: Add 5 points on even attempts, subtract 5 on odd attempts
- **Too Low**: Subtract 5 points

### 6. Game End Conditions
- **WIN**: Player guesses correctly
- **LOSE**: Player runs out of attempts
- Both states should prevent further guessing until "New Game" is clicked

### 7. New Game Behavior
Clicking "New Game" should:
- Reset attempts to 0
- Generate a NEW secret number
- Reset score
- Clear history
- Set status back to "playing"

## Key Functions

### `get_range_for_difficulty(difficulty: str) -> (int, int)`
Returns the (low, high) range for the difficulty level

### `parse_guess(raw: str) -> (bool, int|None, str|None)`
Validates user input and returns (success, value, error_message)

### `check_guess(guess: int, secret: int) -> (str, str)`
Compares guess to secret, returns (outcome, message)

### `update_score(current_score: int, outcome: str, attempt_number: int) -> int`
Calculates new score based on outcome

---

## Known Issues (From README)
- The secret number changes between guesses (state bug)
- The hints are wrong (logic bug)
- Functions need to be refactored to `logic_utils.py`
