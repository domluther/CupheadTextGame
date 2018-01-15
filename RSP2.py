import random

def play_RSP(max, player_name, computer_name):
	player_options = ["Rock", "Scissors", "Paper"]
	print(player_options)

	prompt = "What would you like to play? (R)ock, (S)cissors or (P)aper \n> "

	score1 = 0
	score2 = 0

	# Allows creation of characters with special sets.
	# For example, Rocky who never plays paper.
	if computer_name == "Rocky":
		cpu_options = ["Rock", "Scissors"]
	else:
		cpu_options = ["Rock", "Scissors", "Paper"]

	# To loop the game until a winner has been found
	while score1 < max and score2 < max:

		choice1, choice2 = make_choice(player_options, cpu_options, prompt)

		"""Uses dict key:value to store item and what beats it
		Logic works by comparing the choice to one that would have 
		beaten their opponent"""
		play_dict = {"Rock" : "Paper", "Scissors" : "Rock", "Paper" : "Scissors"}
		choice1_beater = play_dict[choice1]
		choice2_beater = play_dict[choice2]

		if choice1 == choice2:
			print(f"You both picked {choice1}. Try again.")
			continue
		elif choice1 == choice2_beater:
			print(f"{choice1} beats {choice2}")
			print(f"{player_name} wins")
			score1 += 1
		elif choice2 == choice1_beater:
			print(f"{choice2} beats {choice1}")
			print(f"{computer_name} wins")
			score2 += 1
		else:
			print("Something went wrong.")

		print(f"{score1} : {score2}")

	if(score1 > score2):
		return(player_name)
	else:
		return(computer_name)


def make_choice(player_options, cpu_options, prompt):

		choice1 = ""
		choice2 = ""
		# Ensuring a valid input
		while choice1 not in player_options:

			choice1 = full_name(input(prompt)[:1].upper())

		# Used random.choice because it's prettier than randint()
		choice2 = random.choice(cpu_options)

		return choice1, choice2

# Allows user to type in just a letter because typing in full names is tedious
def full_name(input):
		if input == "R":
			return "Rock"
		elif input == "P":
			return "Paper"
		elif input == "S":
			return "Scissors"
		else:
			pass

play_RSP(5, "Dom", "Computer")
