import random

#  Generate the grid dimensions /length width
l = random.randint(15, 25)  # Grid length rows
w = random.randint(10, 15)  # Grid width columns

print("Length of the grid:", l)
print("Width of the grid:", w)

#   Generates treasure location
s1 = random.randint(1, l)
s2 = random.randint(1, w)

# print(f"DEbUG: Treasure is at row {s1}, column {s2}")

# 3. Initialize the number of attempts and start the game
attempts = 0

print("Now let's BEGIN the treasure hunt!")
print("You have to guess the row and column position of the treasure.")

print("The row position is between 1 and", l)
print("The column position is between 1 and", w)
print("Guess the row position of the treasure.")

# 4.    guesses row position
while True:
    try:
        guess_row = int(input("Guess the row position: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1

    if guess_row < s1:
        print(f"You guessed too low for the row position, try again. {attempts} attempt(s) used!")
    elif guess_row > s1:
        print(f"You guessed too high for the row position, try again. {attempts} attempt(s) used!")
    else:
        print(f"You guessed correctly for the row position in {attempts} attempt(s)! Now try to guess the column position!")
        break

# 5.Guesses  column position
while True:
    try:
        guess_col = int(input("Guess the column position: "))

    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1

    if guess_col < s2:
        print(f"You guessed too low for the column position, try again. {attempts} attempt(s) used!")

    elif guess_col > s2:
        print(f"You guessed too high for the column position, try again. {attempts} attempt(s) used!")
    else:
        print(f"You guessed the position of the treasure correctly in {attempts} attempt(s)!")
        break


print("\nCongrats! You have found the treasure (a pot of gold)!")
print(f"Total number of attempts: {attempts}")
