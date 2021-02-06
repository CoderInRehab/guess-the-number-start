
import random
from art import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, attempts):
    if user_guess > actual_answer:
      print("Too high.")
      return attempts - 1
    elif user_guess < actual_answer:
      print("Too low")
      return attempts - 1
    else:
      print(f"you got it! The answer was {actual_answer}")
    
def set_difficulty():
  diff_level = input("Choose your difficulty level. Type 'easy' or 'hard' \t")

  if diff_level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  print("Welcome to the number guessing game")

  print("I'm thinking of a number between 1 to 100")
  #for actual answer
  original_answer = random.randint(1,100)
  print(f"just for test cases: the original answer is {original_answer}")
  attempts_remaining = set_difficulty() 

  user_guess = 0

  while user_guess != original_answer:

    print(f"You have {attempts_remaining} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    attempts_remaining = check_answer(user_guess, original_answer, attempts_remaining)
    if attempts_remaining == 0:
      print("you have run out of guesses, you lose")
      return;
    elif user_guess != original_answer:
      print("Guess again.")
    
play_game = True
while play_game:
  choice = input("Do you want to play the Game? Type 'yes' or 'no': ")
  if choice == "yes":
    clear()
    game()
  else:
    play_game = False