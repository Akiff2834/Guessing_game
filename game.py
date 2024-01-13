import random


def guessing_game():
  print("Hello! I've selected a number between 1 and 100. Start guessing!")

  target_number = random.randint(1, 100)
  guess_count = 0
  max_attempts = 10

  while guess_count < max_attempts:
    user_guess = int(input("Enter your guess: "))
    guess_count += 1

    if user_guess < target_number:
      print("Guess higher.")
    elif user_guess > target_number:
      print("Guess lower.")
    else:
      print(
          f"Congratulations! You guessed the number {target_number} in {guess_count} attempts."
      )
      break
  else:
    print(
        f"Unfortunately, you couldn't guess the correct number. The correct number was {target_number}."
    )


guessing_game()
