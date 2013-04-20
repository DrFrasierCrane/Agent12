# Agent12 written by Tyler Sartin 20 April 2013
# Enjoy!

from random import randint

# This class defines the Player. The player has a 'moves' attribute that inclues all possible
# moves they can perform. 
class Player(object):
	moves = ["Punch", "Kick", "Stab", "Shoot", "Run"]
	
	# The fight method marks the start of a fight. It shows the Player's moves that are available
	# and proceeds to take input. It then calls the Enemy's fight attribute. Then the program
	# compares the moves selected by the Player and the Enemy. Different scenarios are returned
	# depending on what the result is.
	def fight(self):
		print "Your heart begins to beat quickly as you analyze the situation around you.\n"
		self.show_moves()
		
		move = raw_input("\nWhat do you choose to do? > ")
		enemy_move = Enemy().fight()
		
		if "Run" in move or "run" in move or "alarm" in enemy_move:
			return ("capture", move, enemy_move)
		elif enemy_move == "shoot" or enemy_move == "stab":
			return ("fail", move, enemy_move)
		else:
			return ("success", move, enemy_move)
			
					
	def show_moves(self):
		print "Your fighting options are:\n"
		
		i = 0
		while i < len(self.moves):
			print self.moves[i]
			i += 1


	def engage(self, next_scene):
		outcome = Player().fight()
		if outcome[0] == "success":
			print "\nYou tried %s and the guard tried %s.\n" % (outcome[1], outcome[2])
			print "You successfully defeated the guard!"
			return next_scene
		elif outcome[0] == "capture":
			print "\nYou tried %s and the guard tried %s.\n" % (outcome[1], outcome[2])
			return "capture"
		else:
			print "\nYou tried %s and the guard tried %s.\n" % (outcome[1], outcome[2])
			return "death"


class Agent(Player):
	
	def fight(self):
		pass
		
	def show_moves(self):
		pass


class Enemy(Player):
	moves = ["punch", "kick", "stab", "shoot", "run", "alarm"]
	
	def fight(self):
		return self.moves[randint(0, 5)]
		

class Scene(object):
	def enter(self):
		print "This scene is not defined."
		return "sewers"
		
		
class Death(Scene):

	enemy_deaths = ["The MSS agent grabs you by the throat and squeezes your larnyx, he "
					"laughs as you choke to death.", "The MSS agent points the standard "
					"issue Chinese rifle to your forehead and blows your brains out.",
					"The MSS agent runs at you and performs an expertly crafted bicycle "
					"kick straight to your face. Your neck breaks instantly.",
					"A very racist judo chop is applied to your neck, you pass out and "
					"die shortly afterward."]
					
	def enter(self):
		print self.enemy_deaths[randint(0, len(self.enemy_deaths) - 1)]
		again = raw_input("Play again? (Y/N)> ")
		
		if again == "Y":
			return "sewers"
		else:
			exit()
		
		
class Capture(Scene):			
	def enter(self):
		print "You are knocked out cold by the MSS agent and taken into a secret POW camp."
		print "You're probably going to grow old here; painfully."
		again = raw_input("Play again? (Y/N)> ")
		
		if again == "Y":
			return "sewers"
		else:
			exit()
		
		
class Sewers(Scene):

	def enter(self):
		print "\n\nYour name is A12. You have no identity..."
		print ""
		print "You are one of the elite. One of the CIA's finest. For the past three years "
		print "you have been working toward this moment. You were selected as the top agent "
		print "and the number one choice to infiltrate the Ministry of State Security of "
		print "People's Republic of China. You leave the safe house 4 blocks from the MSS. "
		print "You check your GPS to find the nearest sewage entry. This will be the least "
		print "likely to have any guards. You locate a manhole, look around, and remove "
		print "the cover.\n"
		print "You crawl through the manhole behind the MSS. Once you arrive at the bottom "
		print "you encounter a guard!\n"
		
		return Player().engage("secondfloor")

		
class SecondFloor(Scene):
	def enter(self):
		print "You climb out through the sewage system and remove your wetsuit. You check "
		print "your map and locate the service elevator. You take the elevator to the "
		print "second floor and sneak around until you find the low-level MSS staff cubicles."
		print "You sit down at a desk with the name tag 'Chang.'"
		
		result = self.computer()
		if result == "success":
			return "securityroom"
	
	def computer(self):
		
		while True:
			print "\nYou have two options: 1) Try to hack, or 2) Consult your PDA for "
			print "information on Chang.\n"
			choice = raw_input("What do you want to choose? (1 or 2) > ")
			if choice == "1":
				passw = raw_input("PLEASE ENTER PASSWORD > ")
				if passw == "basketball" or passw == "Basketball":
					print "\nACCESS GRANTED"
					return "success"
				else:
					print "ACCESS DENIED"
			elif choice == "2":
				PDA().startup()

		
class SecurityRoom(Scene):
	def enter(self):
		print "Nice work! You successfully hacked Chang's computer, you quickly locate "
		print "the MSS map and additional files located on his computer."
		print "You download the MSS map onto your PDA and make your way to the main security "
		print "room. You take the main elevator as you're disguised as a MSS guard. You "
		print "look out the glass windows of the elevator and admire the numerous lights "
		print "sparkling across Beijing."
		print "\nYou enter the main security room and nod to the desk agent named 'Lee'. "
		print "You walk over to the entrance keypad and scan a counterfeit keycard made "
		print "from Chang's desk."
		
		result = self.keypad()
		if result == "success":
			pass
		else:
			self.keypad()
			
		print "\nYou walk into the main security room and sit down at the main computer "
		print "station. You need to loop the security cameras so you can move to the main "
		print "server room to upload the virus. To do this, you must solve the following "
		print "puzzle.\n"
		
		input = raw_input("Press any key to continue > ")
		answer = self.looper()
		if answer == "success":
			print "\nNice work! You've successfully looped the video feed. You now exit the "
			print "security room and head toward the main server room. Your final mission "
			print "awaits."
			return "serverroom"
		
	def looper(self):

		while True:
			print "What number divided by 4, is equal to that same number minus 4?"
			guess = raw_input("> ")
			if guess ==  "16/3":
				return "success"
			else:
				print "Sorry, try again."
				
	
	def keypad(self):
		key = "0524"
		
		while True:
			print "\nYou have two options: 1) Try to hack, or 2) Consult your PDA for "
			print "information on Chang.\n"
			choice = raw_input("What do you want to choose? (1 or 2) > ")
			if choice == "1":
				pin = raw_input("PLEASE ENTER 4-DIGIT PIN > ")
				if pin == key:
					print "\nACCESS GRANTED"
					return "success"
				else:
					print "\nACCESS DENIED"
					print "\nThe guard peers at you suspiciously, maybe you should consult your "
					print "PDA so you don't fail again..."
			elif choice == "2":
				PDA().startup()

		
class ServerRoom(Scene):
	def enter(self):
		print "As you make your way to the main server room, you encounter a guard who "
		print "eyes you suspiciously. He ask for your credentials. When you hesitate he "
		print "engages you in a fight!\n"
		
		fight1 = Player().engage("rooftop")
		if fight1 == "rooftop":
			None
		elif fight1 == "capture":
			return "capture"
		else:
			return "death"
		
		print "After defeating the guard you make your way to the main server terminal. "
		print "This, to use an American term, in which discovery, retribution, torture, "
		print "death, eternity appear in the shape of a singularly repulsive nutshell, "
		print "was it.\n"
		print "PLEASE ENTER USERNAME AND PASSWORD:"
		
		i = 6
		while i > 0:
			print "\nYou have two options: 1) Try to hack, or 2) Consult your PDA for information. "
			choice = raw_input("What do you want to choose? (1 or 2) > ")
			if choice == "1":
				user = raw_input("USERNAME: ")
				password = raw_input("PASSWORD: ")
				if user == "Wong" or user == "wong" and password == "Asimov" or password == "asimov":
					print "\nACCESS GRANTED"
					break
				else:
					print "\nACCESS DENIED"
					i -= 1
					print "YOU HAVE %d TRIES REMAINING" % (i)
			elif choice == "2":
				PDA().startup()
					
		if i == 0:
			return "death"
		else:
			print "\nCongratulations, you have successfully hacked into the main server. You "
			print "may now begin to upload 'virus.exe'."
			print ".\n.\n.\n.\n.\n.\n.\n."
			raw_input("Are you ready? > ")
			
			
			print "\nNOW LOADING 'virus.exe' YOU NEED 5 MINUTES FOR FULL UPLOAD."
			print "\nAs you begin uploading the virus you hear a guard burst through "
			print "the door! You need to fight him to finish the upload!\n"
			
			return Player().engage("rooftop")
		
	
class Rooftop(Scene):
	def enter(self):
		print ".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
		print "'virus.exe' has been successfully loaded! You have done your country a "
		print "great service. This bug will locate all Chinese intelligence related "
		print "to American secrets.\n\n"
		print "You run to the nearest window and climb up the fire escape. After climbing "
		print "to the rooftop, in true CIA fashion, you base jump to safety."
		print "\n\nCONGRATULATIONS!\n\n\n"

		again = raw_input("Play again? (Y/N)> ")
		
		if again == "Y":
			return "sewers"
		else:
			exit()		

class PDA(object):
	
	def startup(self):
		print "/////////////////////////////////////////////////////////////////////////////"
		print "/                                                                           /"
		print "/   WELCOME TO YOUR PERSONAL DIGITAL ASSISTANT PROVIDED TO YOU BY THE U.S.  /"
		print "/   GOVERNMENT. PLEASE ENTER THE INDIVIDUAL YOU WOULD LIKE TO QUERY.        /"
		print "/                                                                           /"
		print "/   OFFICIALS CURRENTLY LOCATED IN PDA STORAGE: Chang, Lee, Wong.           /"
		print "/                                                                           /"
		print "/////////////////////////////////////////////////////////////////////////////"
		input = raw_input("> ")
		self.query(input)
	
	def query(self, input):
		if input not in dossiers:
			print "PLEASE INPUT A VALID NAME."
			input = raw_input("> ")
			self.query(input)
		else:
			dossiers[input].display()
		

class Dossier(object):
		
	def __init__(self, name, birthday, interests):
		self.name = name
		self.birthday = birthday
		self.interests = interests
		
	def display(self):
		print "\nNOW DISPLAYING INFORMATION ON MINISTY OF STATE SECURITY CITIZEN:", self.name
		print "NAME: ", self.name
		print "DATE OF BIRTH: ", self.birthday
		print "KNOWN INTERESTS: ", self.interests
				

class Engine(object):

	def __init__(self, map):
		self.map = map
		
	def play(self):
		print "==========================================================================\n"
		print "| WELCOME TO AGENT12. YOU WILL TAKE THE POSITION OF A CIA AGENT KNOWN    | "
		print "| ONLY BY THE CODENAME A12. YOUR MISSION, SHOULD YOU CHOOSE TO ACCEPT IT,| "
		print "| IS TO INFILTRATE CHINA'S MINISTRY OF STATE SECURITY, HACK INTO THE     | "
		print "| MAIN SERVER, AND RUN 'virus.exe' DESIGNED TO STREAM ALL U.S. SECRETS   | "
		print "| IN CHINA'S POSESSION TO THE PENTAGON.                                  | "
		print "|                                                                        | "
		print "| GOOD LUCK...                                                           |\n"
		print "==========================================================================\n"
		begin = raw_input("Press any key to begin > ")
		
		current_scene = self.map.opening_scene().enter()
		
		while True:
			print "======================================================================\n"
			current_scene = self.map.next_scene(current_scene).enter()


class Map(object):

	maps = {
	"sewers": Sewers(),
	"secondfloor": SecondFloor(),
	"securityroom": SecurityRoom(),
	"serverroom": ServerRoom(),
	"rooftop": Rooftop(),
	"death": Death(),
	"capture": Capture()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def opening_scene(self):
		return self.maps[self.start_scene]
	
	def next_scene(self, next_scene):
		return self.maps[next_scene]

# Instantiate a Map object and an Engine object.
new_map = Map("sewers")
new_game = Engine(new_map)

# Instantiate three Dossier objects with their credentials.
chang = Dossier("Chang", "May 24, 1986", "Basketball")
lee = Dossier("Lee", "December 15, 1956", "Swimming")
wong = Dossier("Wong", "January 7, 1972", "Science Fiction (Isaac Asimov novels)")

# Collect the three dossier objects into a dictionary by name. This will allow querying later.
dossiers = {
	"chang": chang,
	"lee": lee,
	"wong": wong,
	"Chang": chang,
	"Lee": lee,
	"Wong": wong
}

# Start the game.
new_game.play()