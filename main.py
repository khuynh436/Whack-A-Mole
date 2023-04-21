import random
import time

# Constants
MOLE_SYMBOL = "M"
EMPTY_SYMBOL = "-"
GRID_SIZE = 5
NUM_MOLES = 3
MAX_ATTEMPTS = 10

# Create the game grid
grid = [[EMPTY_SYMBOL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place moles randomly on the grid
moles = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_MOLES)
for mole in moles:
    row = mole // GRID_SIZE
    col = mole % GRID_SIZE
    grid[row][col] = MOLE_SYMBOL

# Initialize the number of attempts and score
attempts = 0
score = 0

# Game loop
while attempts < MAX_ATTEMPTS:
    print("Attempts left:", MAX_ATTEMPTS - attempts)
    print("Score:", score)
    print("-" * 20)
    # Display the game grid
    for row in grid:
        print(" ".join(row))
    print("-" * 20)

    # Get user's guess
    guess = input("Enter row and column (e.g., 1 3) to whack a mole: ")
    guess = guess.split()
    if len(guess) != 2 or not guess[0].isdigit() or not guess[1].isdigit():
        print("Invalid input! Please enter row and column as numbers separated by space.")
        continue

    row = int(guess[0]) - 1
    col = int(guess[1]) - 1

    if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
        print("Invalid input! Row and column must be within the grid size.")
        continue

    if grid[row][col] == MOLE_SYMBOL:
        print("You whacked a mole!")
        score += 1
        grid[row][col] = EMPTY_SYMBOL
    else:
        print("Missed!")
    attempts += 1

# Game over
print("Game over!")
print("Your score:", score)
