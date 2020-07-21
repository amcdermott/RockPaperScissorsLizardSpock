import random

# Declare constants used
ROCK     = "Rock"
PAPER    = "Paper"
SCISSORS = "Scissors"
LIZARD   = "Lizard"
SPOCK    = "Spock"
PLAYER   = "Player"
COMPUTER = "Computer"
TIE      = "Tie"


def determine_winner(player_choice, computer_choice, return_list):
    if player_choice == computer_choice:
        return_list[0]  = TIE
        return;

    result_winner = ""
    result_message = ""

    if player_choice == ROCK:
        if computer_choice == SCISSORS or computer_choice == LIZARD:
            result_winner = PLAYER
            result_message = "Rock crushes " + computer_choice + "."
        elif computer_choice == PAPER:
            result_winner = COMPUTER
            result_message = "Paper covers rock."
        elif computer_choice == SPOCK:
            result_winner = COMPUTER
            result_message = "Spock vapourises rock."

    elif player_choice == PAPER:
        if computer_choice == SPOCK:
            result_winner = PLAYER
            result_message = "Paper disproves Spock."
        elif computer_choice == ROCK:
            result_winner = PLAYER
            result_message = "Paper covers rock."
        elif computer_choice == SCISSORS:
            result_winner = COMPUTER
            result_message = "Scissors cuts paper."
        elif computer_choice == LIZARD:
            result_winner = COMPUTER
            result_message = "Lizard eats paper."

    elif player_choice == SCISSORS:
        if computer_choice == PAPER:
            result_winner = PLAYER
            result_message = "Scissors cuts paper."
        elif computer_choice == LIZARD:
            result_winner = PLAYER
            result_message = "Scissors decapitates lizard."
        elif computer_choice == SPOCK or computer_choice == ROCK:
            result_winner = COMPUTER
            result_message = computer_choice + " smashes scissors."

    elif player_choice == LIZARD:
        if computer_choice == SPOCK:
            result_winner = PLAYER
            result_message = "Lizard poisons Spock."
        elif computer_choice == PAPER:
            result_winner = PLAYER
            result_message = "Lizard eats paper"
        elif computer_choice == SCISSORS:
            result_winner = COMPUTER
            result_message = "Scissors decapitates lizard"
        elif computer_choice == ROCK:
            result_winner = COMPUTER
            result_message = "Rock crushes lizard."

    elif player_choice == SPOCK:
        if computer_choice == SCISSORS:
            result_winner = PLAYER
            result_message = "Spock smashes scissors."
        elif computer_choice == ROCK:
            result_winner = PLAYER
            result_message = "Spock vapourises rock."
        elif computer_choice == PAPER:
            result_winner = COMPUTER
            result_message = "Paper disproves Spock."
        elif computer_choice == LIZARD:
            result_winner = COMPUTER
            result_message = "Lizard poisons Spock."

    return_list[0] = result_winner
    return_list[1] = result_message


print("Let's play Rock, Scissors, Paper, Lizard, Spock...\n\n")

# Declare variables used here...
# int() forces the value to be an integer, allows us to use in comparrison in while loop
firstTo = int(input("  First to: "))
playerScore = 0
computerScore = 0
roundNo = 1

options = [ROCK, PAPER, SCISSORS, LIZARD, SPOCK]

# Keep playing until somebody has enough wins....
while(playerScore < firstTo and computerScore < firstTo):
    print("\n  Round " + str(roundNo))

    # Get player choice
    playerChoice = input("  Player picks: ")

    # Get computer choice...
    computerChoice = options[random.randrange(0, 5)]
    print("  Computer picks: " + computerChoice)

    # Determine who won...
    winner = ""
    message = ""
    list = [winner,message]
    determine_winner(playerChoice, computerChoice, list)

    winner = list[0]
    message = list[1]

    if winner == TIE:
        print("    Draw!")
    else:
        if winner == PLAYER:
            playerScore += 1
        elif winner == COMPUTER:
            computerScore += 1

        print("    " + message)
        print("    " + winner + " wins.")

    print("    Player: " + str(playerScore) + "    Computer: " + str(computerScore))
    roundNo += 1



if (playerScore == firstTo):
    print ("\n  Player wins")
else:
    print("\n  Computer wins")




