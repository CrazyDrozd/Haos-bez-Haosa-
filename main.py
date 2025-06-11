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
    characterTypes = Localization['gameData']['types']
    firstNames = Localization['gameData']['firstNames']
    secondNames = Localization['gameData']['secondNames']
    characterDescriptions = Localization['gameData']['descriptions']

with open('data/weapons.json', 'r', encoding='UTF-8') as local_file:
	weaponsList = json.load(local_file)
	print(weaponsList)

with open('data/armor.json', 'r', encoding='UTF-8') as local_file:
	armorList = json.load(local_file)
	print(armorList)

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
		Weapon = {"id": 1, "type": "Blunt", "name": "Bare-Handed", "description": "A regular punch, what else to say?", "attack": 0},
		Armor = {"id": None, "name": None, "description": "Nothing equipped on.", "defence": 0, "resistances%": {"Blunt%": 0, "Slashing%": 0, "Piercing%": 0, "Otherwordly%": 0}}, 
		Description = "This is a template character.",
		minDamage = None, maxDamage = None):
		'''--- Basic Info ---'''
		self.Initiative = Initiative
		self.Type= Type
		self.firstName, self.secondName = firstName, secondName
		'''--- Equipment ---'''
		self.Weapon = Weapon
		self.weaponID, self.weaponType, self.weaponName, self.weaponDescription, self.weaponAttack = self.Weapon['id'], self.Weapon['type'], self.Weapon['name'], self.Weapon['description'], self.Weapon['attack']
		self.Armor = Armor
		self.armorID, self.armorName, self.armorDescription, self.armorDefence = self.Armor['id'], self.Armor['name'], self.Armor['description'], self.Armor['defence']
		'''--- Characteristics ---'''
		self.Health, self.currentHealth = Health, currentHealth
		self.Attack = Attack + self.Weapon['attack']
		self.Defence = Defence + self.Armor['defence']
		self.evasionRate = evasionRate
		self.Description = Description
		self.minDamage = (self.Attack * 2.25) * 0.65
		self.maxDamage = (self.Attack * 2.25) * 1.35
		self.minDamage, self.maxDamage = round(self.minDamage), round(self.maxDamage)
		
	def randomize(self, 
		Initiative = None, Type = None, firstName = None, secondName = None, 
		Health = None, currentHealth = None, Attack = 8, Defence = 0, evasionRate = 5, 
		Weapon = {"id": None, "type": None, "name": None, "description": None, "attack": None}, 
		Armor = {"id": None, "name": None, "description": None, "defence": None, "resistances%": {"Blunt%": 0, "Slashing%": 0, "Piercing%": 0, "Otherwordly%": 0}}, 
		Description = None,
		minDamage = None, maxDamage = None):
		'''--- Basic Info ---'''
		self.Initiative = random.randint(1, 20)
		self.Type = random.choice(characterTypes)
		self.firstName, self.secondName = random.choice(firstNames), random.choice(secondNames)
		'''--- Equipment ---'''
		self.Weapon = random.choice(weaponsList)
		self.weaponID, self.weaponType, self.weaponName, self.weaponDescription, self.weaponAttack = self.Weapon['id'], self.Weapon['type'], self.Weapon['name'], self.Weapon['description'], self.Weapon['attack']
		self.Armor = random.choice(armorList)
		self.armorID, self.armorName, self.armorDescription, self.armorDefence = self.Armor['id'], self.Armor['name'], self.Armor['description'], self.Armor['defence']
		'''--- Characteristics ---'''
		self.Health, self.currentHealth = random.randint(80, 120), random.randint(1, 100)
		self.Attack = self.Attack + self.Weapon['attack']
		self.Defence = self.Defence + self.Armor['defence']
		self.Description = random.choice(characterDescriptions)
		self.minDamage = (self.Attack * 2.25) * 0.65
		self.maxDamage = (self.Attack * 2.25) * 1.35
		self.minDamage, self.maxDamage = round(self.minDamage), round(self.maxDamage)

	def showInformation(self):	
		if self.Weapon != None:
			console.print(Panel(f'''
[♻ {self.Initiative}] [cyan]{self.firstName} {self.secondName}[/cyan] | {self.Type}
♡ Health [{"▰" * (self.currentHealth // 3)}{"▱" * ((self.Health // 3) - (self.currentHealth // 3))}] {self.currentHealth} | {self.Health}
⚔︎ ATK [{self.Attack}] [[yellow]{self.weaponName}[/yellow]]
╰┈   Deals [red]{self.minDamage}[/red]-[red]{self.maxDamage}[/red] damage.
╰┈   {self.weaponDescription}
⚒ DEF [{self.Defence}] [[yellow]{self.armorName}[/yellow]]
╰┈   {self.armorDescription}
💦 Evasion Rate [{self.evasionRate}%]
{self.Description}\n''', title = "Character", expand = False))

	def __str__(self): 
		return f'''<Character: Initiative: {self.Initiative} | Type: {self.Type} | Name: {self.firstName} {self.secondName} | Health [CURRENT/MAX]: {self.currentHealth}/{self.Health} | Attack: {self.Attack} | Damage [MIX/MAX]: {self.minDamage}/{self.maxDamage} | Defence: {self.Defence} | Evasion Rate: {self.evasionRate} | Weapon: {self.Weapon} | Armor: {self.Armor} | Description: {self.Description}>\n'''

if __name__ == "__main__":
	'''Basic testing calls to see if everything works pretty fine, aka:
	╰┈➤ Randomized character creation
	╰┈➤ Non-Randomized character creation
	╰┈➤ Printing basic information about prototype and characters '''
	

	for i in range(2):
		randomCharacter  = Character()
		randomCharacter.randomize()
		Characters.append(randomCharacter)

	Drozd = Character(13, "Anarchist", "Drozd", "Sandpiper", 80, 45, 8, 0, 5, {"id": 4, "type": "Blunt", "name": "Long-Handed Wrench", "description": "Decent for fixing and repairing stuff.", "attack": 12}, {"id": 37, "name": "Brown Bear-Symbol Hoodie", "description": "FNAF cosplayer, lol", "defence": 3}, "an ADHD crazy catfeine and onyn ring fav kins person appeared! beware!")
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