import random

while True:
    print("Simple Rock-Paper-Scissors Game \n"
    "\n"
    "Instructions \n"
    "------------------- \n"
    '"R" for "Rock" \n'
    '"P" for "Paper" \n'
    '"S" for "Scissors" \n'
    "------------------- \n"
    )
    
    user_input = str(input('Pick an option between "R", "P" or "S" :').capitalize())
    possible_inputs = ["R","P","S"]
    computer_input = random.choice(possible_inputs)
    if user_input not in ("R", "P", "S"):
        print("Error! Please try again with a valid input.")
    else:
        try:
            if user_input == computer_input:
                if user_input == "R":
                    user_input = "Rock"
                elif user_input == "P":
                    user_input = "Paper"
                elif user_input == "S":
                    user_input = "Scissors"
                if computer_input == "R":
                    computer_input = "Rock"
                elif computer_input == "P":
                    computer_input = "Paper"
                elif computer_input == "S":
                    computer_input = "Scissors"
                print("Player "+(user_input)+ ": CPU " + (computer_input))
                print("Both Player and CPU pick the same move. It's a tie")
            elif user_input == "R":
                if computer_input == "S":
                    print("Player (Rock): CPU (Scissors)")
                    print("Rock smashes scissors! You win!")
                else:
                    print("Player (Rock): CPU (Paper)") 
                    print("Paper covers rock! You loose.")
            elif user_input == "P":
                if computer_input == "R":
                    print("Player (Paper): CPU (Rock)")
                    print("Paper covers rock! You win!")
                else: 
                    print("Player (Paper): CPU (Scissors)")
                    print("Scissors cuts paper! You loose.")
            elif user_input == "S":
                if computer_input == "P":
                    print("Player (Scissors): CPU (Paper)")
                    print("Scissors cuts paper! You win!")
                else: 
                    print("Player (Scissors): CPU (Rock)")
                    print("Rock smashes scissors! You loose.")

            play_again = input("Play again? ('y' for yes/'n' for no): ")
            if play_again.lower() != "y":
                print("Thanks for Playing!")
                break
        except ValueError:
            print("AN ERROR OCCURED!")