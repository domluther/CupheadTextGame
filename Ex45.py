from random import randint
from RSP import play_RSP
from textwrap import dedent
import time

class Character(object):
# All characters have a name, 2 of the subclasses can have HP and attrib
# so I prefer to define those here even though NAC won't need those stats.
	def __init__(self, name):
		self.name = name

	def set_name(self, name):
		self.name = name

	def get_HP(self):
		return self.currentHP

	def restore_HP(self, value):
		currentHP = self.currentHP
		maxHP = self.maxHP
		restorable_HP = self.maxHP - self.currentHP

		if value == 0:
			self.currentHP = self.maxHP
		else:
			if value > restorable_HP:
				value = restorable_HP
			else:
				restorable_HP = value
			self.currentHP = self.currentHP + restorable_HP

		print (f"Restored {restorable_HP} HP")

	def set_attribs(self, HP, attack, defence):
		self.maxHP = HP
		self.currentHP = HP
		self.attack = attack
		self.defence = defence


class NAC(Character):
# NAC - Non-active Character. People who are interacted with, but don't fight.
	pass


class Monster(Character):
# Monsters - Characters that the player fights.
	pass


class Player(Character):
# The player, our hero, himself
	def __init__(self, name):
		super().__init__(name)
		self.money = 0
		self.travel = {}
		self.update_inv("Souls", 0)

#Debug triggers
#		self.add_money(100)
#		self.update_inv("Coat", True)
#		self.update_inv("Sword", True)
#		self.update_inv("BatBlood", True)
#		self.update_inv("Torch", True)
#		self.update_inv("BatBlood", True)
#		self.update_inv("Souls", 4)

	# To save information about the player
	def update_inv(self, key, value):
#		print(f">>> update_inv {self.travel}")
		self.travel[key] = value
#		print(f"<<< update_inv {self.travel}")


	def print_inv(self):
#		print(f">>> print_inv()")
		list_of_items = ""
#		print(self.travel)
		for item, value in list(self.travel.items()):
#			print(item, value)
			if value == True:
#				print(f"Value true. Item added :{item}")
				list_of_items += item + " "
			else:
				pass
#				print(f"Value not true. Item NOT added :{item}")
		return list_of_items

	def check_inv(self, item):
#		print(f">>> check_inv for {item}, result : {self.travel.get(item)}")
		return self.travel.get(item)


	# Caled to add money.
	def add_money(self, amount):
		print(f"{self.name} gained {amount} coins.")
		self.money += amount
		print(f"{self.name} now has {self.money} coins.")

	# Takes money away, but confirms that there isn't enough money.
	# The return message could be checked for to stop the transaction
	# But that's not implemented, yet.
	def take_money(self, amount):
		if self.money < amount:
			return "Not enough money"
		else:
			print(f"{self.name} lost {amount} coins.")
			self.money -= amount
			return f"{self.name} now has {self.money} coins."

	def new_soul(self):
		souls = Cuphead.check_inv("Souls")
		souls += 1
		Cuphead.update_inv("Souls", souls)
		print(
			f"{Cuphead.name} now has {souls} souls."
			)


#Defines all the games characters and starting attributes.
Cuphead = Player("Cuphead")
Cuphead.set_attribs(6, 3, 3)

TheDevil = Monster("The Devil")
TheDevil.set_attribs(20, 20, 20)

IceGiant = Monster("Ice_Giant")
IceGiant.set_attribs(4, 5, 1)

Troll = Monster("Troll")
Troll.set_attribs(2, 3, 1)

Bat = Monster("Bat")
Bat.set_attribs(3, 1, 4)

Dragon = Monster("Dragon")
Dragon.set_attribs(6, 5, 4)

Father = NAC("Father")
Barkeeper = NAC("Sam the Barkeeper")
RSPlayer = NAC("Rocky")


class Scene(object):
# Dummy parent class
	pass	

class Intro(Scene):

	def __init__(self):
		Cuphead.update_inv("Intro", "First")

	# Called on entry into the game, assuming it's the first time.
	def enter(self):
#		print("\n>>>Intro.enter()")
#		print(Cuphead.check_inv("Intro"))
		if Cuphead.check_inv("Intro") == "First":
			Cuphead.update_inv("Intro", "Visited")
			print("\nWelcome to Cuphead - The Text Adventure")

			
			print("""                      ____
	             /\' . \    _____
	            /: \___\  / .  /\\
	            \\' / . / /____/..\\
	             \\/___/  \\'  '\  /
	                      \\'__'\/
	                                             """)
			print(dedent("""
				You are Cuphead. You are playing in a casino.
				It's your lucky day. Normally you lose, but,
				ever since that man shook your hand, you just can't.
				"""))
			time.sleep(1)
			print("Just. Can't. Lose.")
			time.sleep(1)
			print(dedent("""
				It's the end of the night. That man who shook your hand comes over.
				He congratulates you, and says that he'll be taking his price now.
				"""))
			time.sleep(1)
			print(dedent("""
				Price? You don't know what he's talking about.
				Then he waves his hand over your eyes.
				"""))
			time.sleep(2)
			print("You feel strange.")
			time.sleep(1)
			print("You feel uninhibited.")
			time.sleep(1)
			print(dedent("""
				You almost ask what happened, but you know.
				You've seen enough films. You made a deal with The Devil.
				Now you don't have a soul.
				"""))
			time.sleep(2)
			print("It takes some time to sink in.")

			i=0
			while i < 3:
				i += 1
				time.sleep(1)
				print("...")
			print(dedent("""
				You miss your soul. You're sure, your father will know what to do.
				You stumble out of the casino, and meander home.
				"""))
			time.sleep(1)
			input("Press enter to go home.")

			where = Home()
			where.enter()
		else:
			# Debug purposes. Stops player coming back to the intro.
			Game.player_dies("You enter a timeloop and kill the game.")
			exit()


class Home(Scene):

	def __init__(self):
		Cuphead.update_inv("Home", "First")

	# Called on entry.
	def enter(self):
#		print(f"\n>>>Home.enter() \n{Cuphead.check_inv('Home')}")

		print("""\
                               ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''-         ''-         ''-         '''  '''

                    """)

		# Different dialogue depending on characteristics.
		# Alternate way could be to define a dic on the player
		if Cuphead.check_inv("Home") == "First":
			Cuphead.update_inv("Home", "Bar")
			print(dedent("""
				Your father is home. He moves to hug you.
				You nomrmally love to hug. But now stare blankly.
				He senses immediately that something is up.
				You explain what you remember of the casino.
				"""))
			time.sleep(2)
			print(dedent("""
				Immediately your father knows what happened, and what to do.
				He's that kind of guy.
				Your father tells explains that the man you met was The Devil.
				There's only one solution. Buy back your soul.
				The price for your soul? The guy in the bar will know.
				"""))
		elif Cuphead.check_inv("Home") == "Bar":
			print(dedent("""
				Did you go to the bar?
				It's in Town.
				"""))

		Game.make_a_choice("Home")


class Town(Scene):

	def __init__(self):
		Cuphead.update_inv("Town", "First")


	def enter(self):
#		print("Town.enter()")
#		print(Cuphead.check_inv("Town"))

		print("""

		  ~         ~~          __
		       _T      .,,.    ~--~ ^^
		 ^^   // \                    ~
		      ][O]    ^^      ,-~ ~
		   /''-I_I         _II____
		__/_  /   \ ______/ ''   /'\_,__
		  | II--'''' \,--:--..,_/,.-{ },
		; '/__\,.--';|   |[] .-.| O{ _ }
		:' |  | []  -|   ''--:.;[,.'\,/
		'  |[]|,.--'' '',   ''-,.    |
		  ..    ..-''    ;       ''. '

			""")
		print(dedent("""
			You enter Town.
			It is bustling with people, but you're not intersted in them.
			Your friend Rocky is in the corner, always willing to play RSP.
			Alternatively there's the Bar, or you can leave Town to the Woods.
			"""))
		Game.make_a_choice("Town")


class Bar(Scene):

	def __init__(self):
		Cuphead.update_inv("Bar", "First")


	def enter(self):
#		print(Cuphead.check_inv("Bar"))

		print('''

              ___                 ___
        _____/___\_____        __|___|__
        """"("-_-")""""         ( o_o )      ~
          /\_)=o~/              _\~-~/_   _ _~
         / /\\\///\      ~     / \/|\/ \/\(|_|
         \__|\\//\ \   ~      / |.   .|\_/
  __________|//\\/_/___~______\_\_____|_____
           _______   |_|)      _______
           \_____/             \_____/
			''')

		print("You enter the Bar.")

		if Cuphead.check_inv("Bar") == "First":
			Cuphead.update_inv("Bar", "NeedSword")
			print(f"{Barkeeper.name} looks at you and waves you over.")
			time.sleep(1)
			print(dedent(f"""
				I heard what happened last night. I guessed you'd be coming.
				As you know, {TheDevil.name} has your soul.
				And you need to meet his price to get it back.
				"""))
			time.sleep(1)
			print(dedent(f"""
				Put your wallet away. Your {Cuphead.money} coins isn't close.
				{TheDevil.name} doesn't care about money. He wants souls.
				If you want to keep your own, you need to meet his price.
				"""))
			time.sleep(2)
			print(dedent("""
				That price? 4 souls. Thankfuly he's not picky.
				How do you get 4 souls? Easy. Kill 4 creatures.
				You just need a trusty sword and to go hunting.
				"""))
		else:
			pass
		if Cuphead.check_inv("Bar") == "NeedSword":
			print(dedent("""
				You don't have a sword? Good thing I have one.
				It's yours for 10 coins.
				"""))
			if Cuphead.money < 10:
				print(dedent("""
					You don't have enough. Go earn some.
					How about playing Rocky at Rock Scissors Paper.
					You know how much he loves rock?
					He won't even use paper!
					"""))
			else:
				choice = input(f"{Cuphead.name}, my friend. Yes or No?\n> ")
				if choice.title() == "Yes":
					Cuphead.update_inv("Sword", True)
					Cuphead.update_inv("Bar", "GotSword")
					Cuphead.take_money(10)
					print("Here you are. My sword. Should do you well.")
				else:
					print("Fine. Be like that. Get out of my bar.")
					Game.make_a_choice("Bar")
		if Cuphead.check_inv("Bar") == "GotSword":
			print(f"{Cuphead.name}, that sword looks good on you!")
			print(dedent(f"""
				Now go use it! You need 4 souls.
				You currently have {Cuphead.check_inv('Souls')}.
				"""))

		Game.make_a_choice("Bar")


class Woods(Scene):

	def __init__(self):
		Cuphead.update_inv("Woods", "First")

	# Called on entry.
	def enter(self):
#		print("\n>>>Woods.enter()")
#		print(Cuphead.check_inv("Woods"))

		print("""

	  ^  ^  ^   ^    ^  ^   ^  ^  ^   ^  ^
	 /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|\\n
	 /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|\\n
	 /|\/|\/|\ /|\  /|\/|\ /|\/|\/|\ /|\/|\\n
	 		""")
		if Cuphead.check_inv("Woods") == "First":
			Cuphead.update_inv("Woods", "Visited")
			print(dedent("""
				It's your first time in the woods since you were young.
				Ever since the monsters arrived in the surrounding areas,
				you haven't felt comfortable coming for a walk here.
				It's such a shame, as they're spectacular.
				"""))
		else:
			pass
		if Cuphead.check_inv("Woods") == "Visited":
			print(dedent("""
				You've been here before. But it still feels strange.
				You look around. There's a path heading north, but it's cold.
				"""))
			if(Cuphead.check_inv("Coat") != True):
				print("You need a coat if you're heading that way.")
			else:
				print("Good thing that you have that 'coat'.")

			print("There is a Field to the east where you used to play.")
		else:
			pass

		Game.make_a_choice("Woods")


class Field(Scene):

	def __init__(self):
		Cuphead.update_inv("Field", "First")


	def enter(self):
#		print(Cuphead.check_inv("Field"))

		print("""

	 _.,-*~'^'~*-,._      (                 _.,-*~'^'~*-,._
	|               '*-,._            _.,-*'               '-,._
	|                     '*-,.__.,-*'                          '*-,.__.,-*,
	|                                                                      |
	`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'`'
			""")
#		print("You enter the Field.")
		if Cuphead.check_inv("Field") == "First":
#			print(">> in first if")
			if Cuphead.check_inv("Sword") == True:
				print(dedent("""
					Seeing the troll appear in front of you, you're relieved.
					You have a sword that was a good idea.
					The troll doesn't want to talk. Just kill you.
					"""))
				print(Game.fight(Cuphead, Troll))
				Cuphead.update_inv("Field", "TrollDead")
				print(dedent("""
					There is a flash in the air.
					The soul of the troll flies up and you hear a chuckle.
					You look to the troll's body and you come up with an idea.
					A few minutes later and you're the owner of a new coat.
					That'll be important to head to the north.
					"""))
				Cuphead.update_inv("Coat", True)
				# Adds a soul to the count
				Cuphead.new_soul()

			else:
				Game.player_dies(dedent("""
					As the troll appears in front of you, you freeze scared.
					You realised you should have listened to your father.
					That thing about going to the bar might have helped.
					Oh well. Death it is.
					"""))
		else:
			print("You've been here before.")
		if Cuphead.check_inv("Field") == "TrollDead":
			print(dedent("""
				The troll's guts are everywhere. A reminder of your first kill.
				Hopefully children can play here again, after the guts go.
				"""))

			Game.make_a_choice("Field")


class TheNorth(Scene):

	def __init__(self):
		Cuphead.update_inv("TheNorth", "First")


	def enter(self):
#		print(Cuphead.check_inv("TheNorth"))
#		print("You enter The North.")

		print("""

                     *  .  *							\n
                   . _\/ \/_ .							\n
                    \  \ /  /             .      .		\n
      ..    ..    -==>: X :<==-           _\/  \/_ 		\n
      '\    /'      / _/ \_ \              _\/\/_ 		\n
        \\//       '  /\ /\  '         _\_\_\/\/_/_/_ 	\n
   _.__\\\///__._    *  '  *            / /_/\/\_\ \ 	\n
    '  ///\\\  '                           _/\/\_ 		\n
        //\\                               /\  /\ 		\n
      ./    \.                            '      ' 		\n

			""")
		#Checks if the player has the coat. If they don't, death.
		if Cuphead.check_inv("TheNorth") == "First":
#			print(">> in first if")
			if Cuphead.check_inv("Coat") == True:
				print(dedent("""
					You get breathed on by an Ice Giant.
					Thanks to your 'coat' you don't freeze to death immediately.
					Another fight!
					"""))
				print(Game.fight(Cuphead, IceGiant))
				Cuphead.update_inv("TheNorth", "GiantDead")
				print(dedent("""
					There is a flash in the air.
					The soul of the Ice Giant flies up and you hear that chuckle again.
					You rip the Ice Giant's left eye out.
					It still has it's shine. That'll do for a torch.
					"""))
				Cuphead.update_inv("Torch", True)
				# Adds a soul to the count
				Cuphead.new_soul()

			else:
				Game.player_dies(dedent(f"""
					No coat? Bad idea {Cuphead.name}.
					The Ice Giant breathes on you once.
					You turn into a rather ugly ice sculpture.
					"""))
		else:
			print("You've been here before.")
		if Cuphead.check_inv("TheNorth") == "GiantDead":
			print(dedent("""
				The North is empty again.
				Without the Ice Giants, the frost might go over time.
				"""))

			Game.make_a_choice("TheNorth")

class Cave(Scene):

	def __init__(self):
		Cuphead.update_inv("Cave", "First")


	def enter(self):

		print("""
                    /   \              /'\       _                              
\_..           /'.,/     \_         .,'   \     / \_                            
    \         /            \      _/       \_  /    \     _                     
     \__,.   /              \    /           \/.,   _|  _/ \                    
          \_/                \  /',.,''\      \_ \_/  \/    \                   
                           _  \/   /    ',../',.\    _/      \                  
             /           _/m\  \  /    |         \  /.,/'\   _\                 
           _/           /MMmm\  \_     |          \/      \_/  \                
          /      \     |MMMMmm|   \__   \          \_       \   \_              
                  \   /MMMMMMm|      \   \           \       \    \             
                   \  |MMMMMMmm\      \___            \_      \_   \            
                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          
                    /'.,___________...,,'   \            \   \        \         
                   /       \          |      \    |__     \   \_       \        
                 _/        |           \      \_     \     \    \       \_      
                /                               \     \     \_   \        \     
                                                 \     \      \   \__      \    
                                                  \     \_     \     \      \   
                                                   |      \     \     \      \  
                                                    \ms          |            \ 
			""")
		if Cuphead.check_inv("Cave") == "First":
#			print(">> in first if")
			if Cuphead.check_inv("Torch") == True:
				print(dedent("""
					Thanks to your 'torch' you see the bat swooping down.
					You dodge to the side and get ready, another fight.
					"""))
				print(Game.fight(Cuphead, Bat))
				Cuphead.update_inv("Cave", "BatDead")
				print(dedent("""
					There is a flash in the air.
					The soul of the bat flies up and you hear the customary chuckle.
					You wonder if the vampire bat's regenerative ability can work for you.
					You suck the bat dry. Can't hurt, right?
					"""))
				Cuphead.update_inv("BatBlood", True)
				# Adds a soul to the count
				Cuphead.new_soul()

			else:
				Game.player_dies(dedent("""
					Walking into a cave without any way to see isn't smart.
					You're walking carefully to not fall into a pit when it starts.
					The first thing you feel is a rush of wind.
					The last thing you feel is the bat's teeth ripping you apart.
					You might not have died, if you could have seen it.
					"""))
		else:
			print("You've been here before.")
		if Cuphead.check_inv("Cave") == "BatDead":
			print(dedent("""
				You walk through the cave peacefully.
				With the main bat dead, the rest seem to have left.
				Finding these souls is bringing peace back to your community. 
				"""))

			Game.make_a_choice("Cave")


class Mountains(Scene):

	def __init__(self):
		Cuphead.update_inv("Mountains", "First")


	def enter(self):
		print("""

           ,                  /\.__      _.-\
          /~\,      __       /~    \   ./    \
        ,/  /_\   _/  \    ,/~,_.~'"\ /_\_  /'\
       / \ /## \ / V#\/\  /~8#  # ## V8  #\/8 8\
     /~#'#"#""##V&#&# ##\/88#"#8# #" #\#&"##" ##\
    j# ##### #"#\&&"####/###&  #"#&## #&" #"#&#"#'\
   /#"#"#####"###'\&##"/&#"####"### # #&#&##"#"### \
  J#"###"#"#"#"####'\# #"##"#"##"#"#####&"## "#"&"##|\

			""")

		if Cuphead.check_inv("Mountains") == "First":
#			print(">> in first if")
			print(dedent("""
				You come out of the cave onto the mountain side.
				What's waiting for you but the mythical Black Dragon.
				He swoops down, breathing fire.
				You roll out of the way, ready for another fight.
				"""))
			print(Game.fight(Cuphead, Dragon))
			Cuphead.update_inv("Mountains", "DragonDead")
			print(dedent("""
				There is a flash in the air.
				The dragon's soul is yours.
				"""))
			Cuphead.new_soul()
			if Cuphead.check_inv("Souls") == 4:
				print(dedent("""
					That's 4 souls!
					You're ready. 
					You can now teleport.
					"""))
			else:
				print("Not got 4 souls. Error?")
		else:
			print("You've been here before.")
		if Cuphead.check_inv("Mountains") == "DragonDead":
			print(dedent("""
				The top of the mountain is peaceful.
				You could sit here and rest.
				"""))

			Game.make_a_choice("Mountains")


class Hell(Scene):

	def __init__(self):
		Cuphead.update_inv("Hell", "First")


	def enter(self):
		print(Cuphead.check_inv("Hell"))
		print("""\

	                                      _.---**""**-.       
	                              ._   .-'           /|`.     
	                               \`.'             / |  `.   
	                                V              (  ;    \  
	                                L       _.-  -. `'      \ 
	                               / `-. _.'       \         ;
	                              :            __   ;    _   |
	                              :`-.___.+-*"': `  ;  .' `. |
	                               |`-/     `--*'   /  /  /`.\|
	                              : :              \    :`.| ;
	                              | |   .           ;/ .' ' / 
	                              : :  / `             :__.'  
	                               \`._.-'       /     |      
	                                : )         :      ;      
	                                :----.._    |     /       
	                               : .-.    `.       /        
	                                \     `._       /         
	                                /`-            /          
	                               :             .'           
	                                \ )       .-'             
	                                 `-----*"'  

	                           """)

		if Cuphead.check_inv("Hell") == "First":
#			print(">> in first if")
			print(dedent("""
				The Devil looks at you blinkingly.
				He doesn't know what you're doing or how you appear.
				You show him the 4 souls, and the recognition comes on his face.
				You've come to pay the price.
				With the 4 souls, you want yours back.
				He lets you know that you've got a choice.
				You can either fight him for it, or gamble.
				You know neither will be easy.
				What in life is?
				What will it be?
				"""))
			while Cuphead.check_inv("DevilFight") != True:
#				print(f">> Hell while loop. DevilRPS = {Cuphead.check_inv('DevilRPS')} DevilFight = {Cuphead.check_inv('DevilFight')}")
				Game.make_a_choice("Hell")
#				print(f"<< Hell while loop. DevilRPS = {Cuphead.check_inv('DevilRPS')} DevilFight = {Cuphead.check_inv('DevilFight')}")
			Game.player_wins()			



class Quit(object):

	def enter(self):
		Game.quit()

class Engine(object):

	def play(self):
		where = Intro()
		where.enter()

	def move(self, current_location):
#		print(">>move()")
		locations = {
		"Intro" : IntroInstance,
		"Home" : HomeInstance,
		"Woods" : WoodsInstance,
		"Town" : TownInstance,
		"Bar" : BarInstance,
		"Field" : FieldInstance,
		"The North" : TheNorthInstance,
		"Cave" : CaveInstance,
		"Mountains" : MountainsInstance,
		"Hell" : HellInstance,
		"Quit" : Quit()
		}

		possible_destinations = {
		"Home" : "Town, Quit",
		"Woods" : "Town, The North, Field, Quit",
		"Town" : "Home, Bar, Woods, Quit",
		"Bar" : "Town, Quit",
		"Field" : "Woods, Cave, Quit",
		"TheNorth" : "Woods, Quit",
		"Cave" : "Field, Mountains, Quit",
		"Mountains" : "Cave, Quit",
		"Hell" : "Hell, Quit",
		}
		
		while True:
			try:
#				print("\n>> in try")
#				print(f">>> options : {possible_destinations[current_location]}")
				to_where = input("\nWhere do you want to go?\n> ").title()
#				print(f"\nto_where : {to_where}")
				print(f"Possible Destinations : {possible_destinations[current_location]}")
				if to_where == current_location:
					print("You're already there.")
				elif to_where in possible_destinations.get(current_location):
					return locations[to_where]
				else:
					print(f"{to_where} from here? Unlikely. Not unless you can teleport.")
#				print(f"locations.get(to_where) {locations.get(to_where)}")
			except KeyError:
				print("Invalid location.")


	def teleport(self, current_location):
#		print(">>teleport()")
		locations = {
		"Intro" : IntroInstance,
		"Home" : HomeInstance,
		"Woods" : WoodsInstance,
		"Town" : TownInstance,
		"Bar" : BarInstance,
		"Field" : FieldInstance,
		"The North" : TheNorthInstance,
		"Cave" : CaveInstance,
		"Mountains" : MountainsInstance,
		"Hell" : HellInstance,
		"Quit" : Quit()
		}
		
		while True:
			try:
#				print("\n>> in try")
				to_where = input("\nWhere do you want to go?\n> ").title()
#				print(f"\nto_where : {to_where}")
#				print(f"poss : {possible_destinations[current_location]}")
#				print(f"locations.get(to_where) {locations.get(to_where)}")
				return locations[to_where]
			except KeyError:
				print("Invalid location.")

	def make_a_choice(self, current_location):

		possible_choices = {
		"Home" : "Beg, Go, Inv, Rest, Quit",
		"Woods" : "Go, Inv, Quit",
		"Town" : "Go, Inv, Play, Quit",
		"Bar" : "Go, Inv, Quit",
		"Field" : "Go, Inv, Rest, Quit",
		"TheNorth" : "Go, Inv, Quit",
		"Cave" : "Go, Inv, Quit",
		"Mountains" : "Go, Inv, Rest, Quit",
		"Hell" : "Fight, Play, Quit",
		}

		while True:
			# Capitalises it to provide uniform values
			to_do = input("\nWhat would you like to do?\n> ").title()
			# Removes empty space at the end
			to_do = to_do.strip()
#			print(f">>> to_do : {to_do}")
#			print(f">>> current_location : {current_location}")
#			print(f">>> possible_choices[current_location] : {possible_choices[current_location]}")
			if to_do in possible_choices[current_location]:

				if to_do == "Go":
					# When the player gets to 4 souls, they can teleport.
					if Cuphead.check_inv("Souls") < 4:
						# Switched between move and teleport for debug
						where = Game.move(current_location)
						where.enter()
						break
					else:
						where = Game.teleport(current_location)
						where.enter()

				elif to_do == "Quit":
					Game.quit()

				if to_do == "Inv":
					inv = Cuphead.print_inv()
					if inv == "":
						print("You have nothing.")
					else:
						print(f"You have {inv}")

				elif to_do == "Beg":
					print(f"You ask {Father.name} for money.")
					if Cuphead.money == 0:
						print(f"OK, {Cuphead.name}. Here you are.")
						Cuphead.add_money(5)
					else:
						print(dedent(f"""
							{Cuphead.name}, what are you begging for?
							You already have {Cuphead.money} coins!
							"""))

				elif to_do == "Rest":
					if current_location == "Home":
						print("You jump in to bed and sleep peacefully.")
					elif current_location == "Mountains":
						print("You close your eyes and meditate.")
					else:
						print("What")
					Cuphead.restore_HP(0)

				elif to_do == "Play":
					if current_location == "Town":
						print(dedent("""
							You walk over to Rocky. He's thrilled to play with you,
							for a price.
							"""))
						try:
							games = int(input("How many games do you want to play?\n> "))
						except ValueError:
							print("Enter a number next time.")
							continue
						if games == 0:
							print("Changed your mind? Fine. Be like that.")
						elif games > Cuphead.money:
							print(dedent(f"""
								Come on {Cuphead.name}. You have {Cuphead.money} coin(s).
								You know it's 1 coin per game.
								Go beg from your father.
								"""))
						else:
							print(f"{games}? . OK. Time to play.")
							winner = play_RSP(games, Cuphead.name, RSPlayer.name)
							if winner == Cuphead.name:
								print(f"Well done {Cuphead.name}!")
								Cuphead.add_money(games)
							else:
								print(f"Unlucky {Cuphead.name}!")
								print(Cuphead.take_money(games))
					elif current_location == "Hell":
						if Cuphead.check_inv("DevilRPS") != True:
							print(dedent("""
								RPS with The Devil? Sounds like a plan.
								The Devil is not Rocky.
								He's got some skills, and you'll have to win.
								Also, if you lose, that's it. You die.							
								"""))
							winner = play_RSP(5, Cuphead.name, TheDevil.name)
							if winner == Cuphead.name:
								Cuphead.update_inv("DevilRPS", True)
								print(f"Well done {Cuphead.name}!")
								Cuphead.set_attribs(6, 6, 6)
								TheDevil.set_attribs(6, 6, 6)
								break
							else:
								Game.player_dies("""
									The Devil beats you.
									Your soul is his forever.
									Welcome to Hell.
									It's your new home.
									""")									
						else:
							print(dedent("""
								Are you trying to taunt the devil?
								You already beat him once. Don't try it.
								"""))
				elif to_do =="Fight":
					Cuphead.update_inv("DevilFight", True)
					print(Game.fight(Cuphead, TheDevil))
					break
				elif to_do =="":
					print("Try to enter something instead.")
				else:
					print("I'm confused.")
			else:
				print(f"What? You can {possible_choices[current_location]}")


	def quit(self):
		print("Byebye")
		quit()

	# Called when the player dies. Prints the reason, dedented.
	def player_dies(self, reason):
#		print(">>> player_dies")
		print(dedent(reason))
		Game.quit()

	# Called when the player wins. Just a simple message.
	def player_wins(self):
#		print(">>> player_wins")
		print(dedent(f"""
			You did it!
			You got the souls, bested the devil and got your own soul back!
			Well done! You {Cuphead.name} are the champion!
			"""))
		Game.quit()

	# Fighting mechanics.
	def two_character_fight(self, character1, character2, i):
#		print(">>> two_character_fight()")

		input(dedent(
			f"-Round {i}-\n"
			f"{character1.name} is getting ready to attack Press enter."
			))

		attack1 = (character1.attack*randint(0, 6))
		defence2 = (character2.defence*randint(0, 6))

		if (attack1 > defence2):
#			print(">first if")
			print(dedent(
				f"{character1.name} hurt {character2.name}"
				))
			character2.currentHP -= 1
			if character2.currentHP == 0:
#				print(">second if")
				return()

		elif (attack1 <= defence2):
#			print(">third if")
			print(f"{character2.name} blocked {character1.name}'s attack")

		input(dedent(
			f"{character2.name} is getting ready to attack Press enter."
			))

		attack2 = (character2.attack*randint(0, 6))
		defence1 = (character1.defence*randint(0, 6))

		if (attack2 > defence1):
#			print(">fourth if")
			print(dedent(
				f"{character2.name} hurt {character1.name}"
				))
			character1.currentHP -= 1
			if character1.currentHP == 0:
#				print(">fifth if")
				return()
		elif (attack2 <= defence1):
#			print(">sixth if")
			print(f"{character1.name} blocked {character2.name}'s attack")


		print(f"{character1.name}'s health is {character1.currentHP}")
		print(f"{character2.name}'s health is {character2.currentHP}")

		return(f"{character1.name} has {character1.currentHP}. {character2.name}"
			f" has {character2.currentHP}")


	# Sets a fight between 2 characters, loops until HP = 0
	def fight(self, character1, character2,):

		print(f"\n{character1.name} v {character2.name}")

		i = 1
		while character1.currentHP > 0 and character2.currentHP > 0:
			# A heal before every 3rd/6th/9th... round after killing Bat
			if i%3 == 0 and Cuphead.check_inv("BatBlood") == True:
				print("Vampire blood heal")
				Cuphead.restore_HP(1)

			result = Game.two_character_fight(character1, character2, i)
			i += 1
		if character1.currentHP == 0:
			Game.player_dies(
				f"{character2.name} kills you. Oops. Game over.."
				)
		elif character2.currentHP == 0:
			return(
				f"{character2.name} died. {character1.name} has {character1.currentHP}"
				)
		else:
			print("Don't know how you got here.")


HomeInstance = Home()
IntroInstance = Intro()
WoodsInstance = Woods()
TownInstance = Town()
BarInstance = Bar()
FieldInstance = Field()
TheNorthInstance = TheNorth()
CaveInstance = Cave()
MountainsInstance = Mountains()
HellInstance = Hell()

Game = Engine()
Game.play()

