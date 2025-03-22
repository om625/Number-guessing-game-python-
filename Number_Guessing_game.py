import random
from emoji import emojize

def play_game():
    print("Welcome to number guessing game!",emojize(":grinning_face:\n"))
    print("Enter two numbers and guess the number between them")
    num1 = input("Enter the first number: \n")
    num2 = input("Enter the second number: \n")

    if num1 >= num2:
        print("Error! please enter valid details..\n")
        return
    elif num1.isdigit() and num2.isdigit():
        num1,num2 = int(num1), int(num2)

        random_number = random.randint(num1, num2)
        print("You have 10 chances to guess the correct number!!\n")
        number_of_guesses = 10


        while number_of_guesses > 0:
            try:
                guess_number = int(input(f"Guess the number, You have {number_of_guesses} guess left\n"))
            except ValueError:
                print("ERROR!! please enter valid details\n")
                continue

            if guess_number > random_number:
                print("Your guess is larger",emojize(":thumbs_down:\n"))
            elif guess_number < random_number:
                print("Your guess is smaller",emojize(":thumbs_down:\n"))
            else:
                print("YOU WON!!!",emojize(":partying_face:\n"))
                break

            number_of_guesses -= 1

            if number_of_guesses == 0:
                print("GAME OVER!! ", f"correct number was {random_number}", emojize(":crying_face:\n"))
                break

    else:
        print("ERROR!! please enter valid details\n")

while True:
   play_game()
   play_again = input("Do you want to play again? (yes/no)\n").lower()
   if play_again != "yes":
       print("Thanks for playing!", "Good bye")
       break

