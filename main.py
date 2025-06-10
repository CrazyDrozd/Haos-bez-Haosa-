from time import sleep
from rich.panel import Panel
from rich.console import Console
import random
import json

console = Console()

'''Importing .JSON config files data and information'''
with open('data/localization.json', 'r', encoding='UTF-8') as local_file:
    Localization = json.load(local_file)
    prototypeName = Localization['prototypeInfo']['name']
    prototypeVersion = Localization['prototypeInfo']['version']
    prototypeBuildDate = Localization['prototypeInfo']['buildDate']
    prototypeAuthor = Localization['prototypeInfo']['author']
    prototypeDescription = Localization['prototypeInfo']['description']
    listOfTypes = Localization['gameData']['types']
    listOfFirstNames = Localization['gameData']['firstNames']
    listOfSecondNames = Localization['gameData']['secondNames']
    listOfArmor = Localization['gameData']['armor']
    listOfDescriptions = Localization['gameData']['descriptions']

with open('data/weapons.json', 'r', encoding='UTF-8') as local_file:
	weaponsList = json.load(local_file)
	print(weaponsList)
Characters = []
	
class Character: 
	'''Character class, contains methods of:
		╰┈➤ __init__: Initializing character characteristics, such as health, name, damage and other.
				╰┈ If any of attributes was not writted in creating an object, then the default ones would be put.
		╰┈➤ randomize: Creates a character with fully randomized characteristics.
		╰┈➤ showInformation: Prints a character intuitive panel with all characteristics.
		╰┈➤ __str__: Returns proper string information of an object.'''
	def __init__(self, 
		Initiative = 1, Type = "Civilian", firstName = "Mister", secondName = "Template", 
		Health = 80, currentHealth = 80, Attack = 8, Defence = 0, evasionRate = 5, 
		Weapon = {"id": 1, "name": "Bare-Handed", "attack": 0}, Armor = None, Description = "This is a template character."):
		'''--- Basic Info ---'''
		self.Initiative = Initiative
		self.Type= Type
		self.firstName = firstName
		self.secondName = secondName
		'''--- Equipment ---'''
		self.Weapon = Weapon
		self.weaponID = self.Weapon['id']
		self.weaponName = self.Weapon['name']
		self.weaponAttack = self.Weapon['attack']
		'''--- Characteristics ---'''
		self.Health = Health
		self.currentHealth = currentHealth
		if self.currentHealth == None:
			self.currentHealth = self.Health
		self.Attack = Attack + self.Weapon['attack']
		self.Defence = Defence
		self.evasionRate = evasionRate
		self.Armor = Armor
		self.Description = Description
		
	def randomize(self, 
		Initiative = None, Type = None, firstName = None, secondName = None, 
		Health = None, currentHealth = None, Attack = None, Defence = None, evasionRate = None, 
		Weapon = {"id": None, "name": None, "attack": None}, Armor = None, Description = None):
		'''--- Basic Info ---'''
		self.Initiative = random.randint(1, 20)
		self.Type = random.choice(listOfTypes)
		self.firstName = random.choice(listOfFirstNames)
		self.secondName = random.choice(listOfSecondNames)
		'''--- Equipment ---'''
		self.Weapon = random.choice(weaponsList)
		self.weaponID = self.Weapon['id']
		self.weaponName = self.Weapon['name']
		self.weaponAttack = self.Weapon['attack']
		'''--- Characteristics ---'''
		self.Health = random.randint(80, 120)
		self.currentHealth = random.randint(1, 100)
		self.Attack = self.Attack + self.Weapon['attack']
		self.Defence = random.randint(0, 6)
		self.Armor = random.choice(listOfArmor)
		self.Description = random.choice(listOfDescriptions)

	def showInformation(self):	
		if self.Weapon != None:
			console.print(Panel(f'''
[♻ {self.Initiative}] [cyan]{self.firstName} {self.secondName}[/cyan] | {self.Type}
♡ Health [{"▰" * (self.currentHealth // 3)}{"▱" * ((self.Health // 3) - (self.currentHealth // 3))}] {self.currentHealth} | {self.Health}
⚔︎ ATK [{self.Attack}] [[yellow]{self.weaponName}[/yellow]]
⚒ DEF [{self.Defence}] [[yellow]{self.Armor}[/yellow]]
💦 Evasion Rate [{self.evasionRate}%]
{self.Description}\n''', title = "Character", expand = False))

	def __str__(self): 
		return f'''<Character: Initiative: {self.Initiative} | Type: {self.Type} | Name: {self.firstName} {self.secondName} | Health [CURRENT/MAX]: {self.currentHealth}/{self.Health} | Damage: {self.Attack} | Defence: {self.Defence} | Evasion Rate: {self.evasionRate} | Weapon: {self.Weapon} | Armor: {self.Armor} | Description: {self.Description}>'''

if __name__ == "__main__":
	'''Basic testing calls to see if everything works pretty fine, aka:
	╰┈➤ Randomized character creation
	╰┈➤ Non-Randomized character creation
	╰┈➤ Printing basic information about prototype and characters '''
	

	for i in range(2):
		randomCharacter  = Character()
		randomCharacter.randomize()
		Characters.append(randomCharacter)

	Drozd = Character(13, "Anarchist", "Drozd", "Sandpiper", 80, 45, 8, 0, 5, {"id": 4, "name": "Long-Handed Wrench", "attack": 12}, "Brown Bear-Symbol Hoodie", "an ADHD crazy catfeine and onyn ring fav kins person appeared! beware!")
	Characters.append(Drozd)
	print(Characters)
	for character in Characters:
		print(str(character))
	# print(listOfDescriptions)

	console.print(Panel(f'''
[cyan]name[/cyan]: {prototypeName}
[cyan]version[/cyan]: {prototypeVersion}
[cyan]buildDate[/cyan]: {prototypeBuildDate}
[cyan]author[/cyan]: {prototypeAuthor}
[cyan]description[/cyan]: {prototypeDescription}\n''', title = "Prototype Information", expand = False))
	templateCharacter = Character()
	templateCharacter.showInformation()
	for character in Characters:
		character.showInformation()