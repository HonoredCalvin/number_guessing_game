# number_guessing_game using python

# Display message to the player
print("Am thinking of a number which is 1 to 100")
print("Think you can guess give it a shot")

# Taking the player's guess and accounting for any wrong input from the user
while True:
    while True:
        try:
            my_guessed_number = float(input("Enter your number: "))
            break
        except ValueError:
            print("Wrong input this is not a number!")

    if my_guessed_number == 55:
        print("Gracious! you guessed it!")
        break
    elif 50 <= my_guessed_number < 55:
        print("Slightly less than the number keep on trying!")
    elif my_guessed_number < 50:
        print("Too small try hyping it up!")
    elif 55 < my_guessed_number <= 60:
        print("Slightly higher than the number keep on trying!")
    else:
        print("Too big try trimming it!")

    print(f"The number you guessed is {my_guessed_number} and is wrong!")

    again = input("Do you wish to try again (y/n): ")

    if again.lower() != "y":
        break