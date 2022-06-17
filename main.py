correct_number = 10
user_number = 0
guess_count = 0
guess_limit = 5

while user_number != correct_number and guess_count < guess_limit:
    guess_count += 1
    user_number = int(input("Guess: "))
    if user_number == correct_number:
        print("You win!")
        break
    elif user_number < correct_number and guess_count < guess_limit:
        print("Too small!")
    elif user_number > correct_number and guess_count < guess_limit:
        print("Too big")
else:
    print("Sorry, you failed!")
