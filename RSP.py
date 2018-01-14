from random import randint

def play_RSP(max, player_name, computer_name):
	options = ["Rock", "Scissors", "Paper"]
	print(options)

	prompt = "What would you like to play? Rock, Scissors or Paper \n> "

	choice1 = ""
	choice2 = ""
	score1 = 0
	score2 = 0

	# Because Rocky will never play paper.
	if computer_name == "Rocky":
		max_int = 1
	else:
		max_int = 2


	while score1 < max and score2 < max:
#		print(f">>> 1st while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
		# Used to ensure a valid input
		choice1 = ""
		while choice1 not in options:
#			print(f">>> 2nd while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
			choice1 = input(prompt).title()
#			print(f"<<< exit 2nd while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
		choice2 = (options[randint(0,max_int)])
#		print(f">>> before 3rd while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
		while choice1 == choice2:
#			print(f">>> 3rd while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
			print(f"You both picked {choice1}. Try again.")
			# Resets string so same method works to check for a valid input
			choice1 = ""
#			print(f">>> before 4th while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
			while choice1 not in options:
#				print(f">>> 4th while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
				choice1 = input(prompt).title()
#				print(f"<<< end of 4th while loop. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")
			choice2 = (options[randint(0,max_int)])
#		print(f" Game play. score 1: {score1}, score2: {score2}, choice1: {choice1}, choice2: {choice2}")

		print(f"{player_name} played {choice1}")
		print(f"{computer_name} played {choice2}")


		if choice1 == "Rock" or choice2 == "Rock":

			if choice1 == "Scissors" or choice2 == "Scissors":
				print("Rock beats Scissors")
				if choice1 == "Rock":
					print(f"{player_name} wins.")
					score1 += 1
				else:
					print(f"{computer_name} wins.")
					score2 += 1
			else:
				print("Paper beats Rock")
				if choice1 == "Paper":
					print(f"{player_name} wins.")
					score1 += 1
				else:
					print(f"{computer_name} wins.")
					score2 += 1
		else:
			print("Scissors beats Paper")
			if choice1 == "Scissors":
				print(f"{player_name} wins.")
				score1 += 1
			else:
				print(f"{computer_name} wins.")
				score2 += 1
		print(score1, score2)

	if(score1 > score2):
		return(player_name)
	else:
		return(computer_name)
