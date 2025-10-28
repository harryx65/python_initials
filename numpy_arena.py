import numpy as np
import random
import string

# STORE THE 1D ARRAY FROM USER
# user_input = input("add number with spaces: ")
# numbers = user_input.split()
# numbers = list(map(int, numbers))
# user_array = np.array(numbers)
# print(user_array)


def calculator():
    print("Welcome to HARRYMAC Calculator")

    rows = int(input("Input number of rows: "))
    column = input("Input number of columns: ")
    result = ""

    print("FIRST MATRIX")
    first_matrix = np.array([list(map(int, input(
        f"Enter the Element of 1st matrix of {x+1} row with space: ").split())) for x in range(rows)])

    print("\nSECOND MATRIX")
    second_matrix = np.array([list(map(int, input(
        f"Enter the Elements of 2nd matrix of {x+1} row with space: ").split())) for x in range(rows)])

    print("\nYour First Matrix: ")
    print(first_matrix)
    print("Your Second Matrix: ")
    print(second_matrix)

    while True:
        print("\nCHOOSE OPERTATION")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply(element wise)")
        print("4. Divide")
        print("5. dot product")
        print("6. Find minimum value(for 1D array)")
        print("7. Find maximum value(for 1D array)")
        print("8. Find average(for 1D array)")
        print("9. find Standard Deviation")

        choice = int(input("\nEnter Your Choice (1-9): "))

        if choice == 1:
            result = np.add(first_matrix, second_matrix)
            print(f"The Addition of your both matrix are {result}")

        elif choice == 2:
            result = np.subtract(first_matrix, second_matrix)
            print(f"The Subtraction of your both matrix are {result}")

        elif choice == 3:
            result = np.multiply(first_matrix, second_matrix)
            print(f"The Multiplication of your both matrix are {result}")

        elif choice == 4:
            num = int(input("number of floating point: "))
            d = np.divide(first_matrix, second_matrix)
            result = np.round(d, num)
            print(f"The Division of your both matrix are {result}")

        elif choice == 5:
            result = np.dot(first_matrix, second_matrix)
            print(f"The Dot product of your both matrix are {result}")

        elif choice == 6:
            concatenate_array = np.concatenate((first_matrix, second_matrix))
            result = concatenate_array.min()
            print(f"The Minimum element of your both matrix are {result}")

        elif choice == 7:
            concatenate_array = np.concatenate((first_matrix, second_matrix))
            result = concatenate_array.max()
            print(f"The Maximum element of your both :.5f matrix are {result}")

        elif choice == 8:
            concatenate_array = np.concatenate((first_matrix, second_matrix))
            result = concatenate_array.mean()
            print(f"The Mean of your both matrix are {result}")

        elif choice == 9:
            concatenate_array = np.concatenate(first_matrix, second_matrix)
            result = concatenate_array.std()
            print(
                f"The Standard Daviation element of your both matrix are {result}")

        replay_choice = input("wanted to calculate again? (y/n): ").lower()
        if replay_choice == "n":
            break


def guessing_game():

    while True:
        print("WELCOME TO HARRYGUESS GAME")
        guess_game_choice_for_simple = int(
            input("\nWanted to play simple or hard? (1 simple 2. hard):  "))

        if guess_game_choice_for_simple == 1:

            random_number = random.randint(1, 15)
            chances = 3
            for x in range(chances):
                print(
                    f"You have {chances} chances to guess a number between 1-15")
                user_choice = int(input("Enter Your Choice: "))
                if user_choice == random_number:
                    print("Huraaay! You Won")
                    break
                if user_choice > random_number:
                    print("too high")
                    chances = chances - 1
                elif user_choice < random_number:
                    print("too low")
                    chances = chances - 1
            else:
                print(f"You loose, the correct number was {random_number}")

            play_choice_guess = input("Wanter to Play again? (y/n): ").lower()
            if play_choice_guess == "n":
                break

        # Hard-level
        if guess_game_choice_for_simple == 2:
            random_number = random.randint(1, 15)

            print("You have only one chance to guess a number between 1-15 ")
            user_choice = int(input("Enter Your Choice: "))

            if user_choice == random_number:
                print("Huraaay! You Won")
            else:
                print(f"You loose, the correct number was{random_number}")

            play_choice_guess = input("Wanter to Play again? (y/n): ").lower()
            if play_choice_guess == "n":
                break


def choice_maker():
    while True:
        print("Welcome to HarryChoice Game")
        options = np.array(input("\nAdd the choices with space: ").split())
        selected_choice = random.choice(options)
        print(f"You can go with {selected_choice}")

        make_choice = input("Wanted to play again? (y/n): ").lower()
        if make_choice == "n":
            break


def play_game():
    while True:
        print("HI, Welcome to Harriena!")
        print('\n What would you like to do?')
        print('1. Matrix Calculation')
        print('2. Guessing Game')
        print('3. Making Choice')

        usr_choice = int(input("\n Enter Your Choice: "))
        if usr_choice == 1:
            calculator()
        elif usr_choice == 2:
            guessing_game()
        elif usr_choice == 3:
            choice_maker()
        else:
            print("invalid Input")
        user_choice = input("Menu or Quit?(m/q) :").lower()
        if user_choice == "q":
            break


play_game()
