import math
import random
from typing import ClassVar
import requests
import pyspectrum
import os

c = pyspectrum.Colors() 
nounurl = "https://raw.githubusercontent.com/taikuukaits/SimpleWordlists/master/Wordlist-Nouns-All.txt"
nouns = requests.get(nounurl).text.split("\n")
random.shuffle(nouns)


loot = [
	("Breastplate", 19.865, "Common"),
	("Sword", 14.0, "Common"), 
	("Helmet", 12.9, "Common"),
	("Longbow", 10.5, "Common"),
	("Kukri", 8.32, "Uncommon"),
	("Shield", 8.32, "Uncommon"), 
	("Crossbow", 6.3, "Uncommon"), 
	("Spear", 4.850, "Uncommon"), 
	("Battleaxe", 4.850, "Uncommon"), 
	("Ootsuchi", 4.2, "Rare"), 
	("Sai", 2.25, "Rare"), 
	("Rapier", 1.67, "Rare"), 
	("Mace", 0.75, "Rare"), 
	("Shikomizue", 0.6, "Super Rare"), 
	("Pike", 0.45, "Super Rare"), 
	("Katana", 0.075, "Exotic"),
	("Scythe", 0.06, "Exotic"),
	("Naginata", 0.02, "Exotic"),
	("Estoc", 0.01, "Invaluable"),
	("Wakizashi", 0.01, "Invaluable")
]

classes = {
	"Berserker":{
		"color":c.Hexadecimal("#bf5615").to_rgb()
	},
	"Mage":{
		"color":c.Hexadecimal("#328bf0").to_rgb()
	},
	"Rogue":{
		"color":c.Hexadecimal("#0c4d02").to_rgb()
	},
	"Warlock":{
		"color":c.Hexadecimal("#4338ba").to_rgb()
	},
	"Paladin":{
		"color":c.Hexadecimal("#F58CBA").to_rgb()
	},
	"Shaman":{
		"color":c.Hexadecimal("#4dbfc9").to_rgb()
	},
	"Vagabond":{
		"color":c.Hexadecimal("#ad1f72").to_rgb()
	}
}

rarities = {
	"Common":c.RGB(235, 235, 235),
	"Uncommon":c.RGB(38, 173, 104),
	"Rare":c.RGB(56, 113, 199),
	"Super Rare":c.RGB(8, 59, 135),
	"Exotic":c.RGB(113, 45, 227),
	"Invaluable":c.RGB(230, 41, 123)
}

loot_rarities = dict([(item, rarity) for item, drop, rarity in loot])
loot_rates = dict([(item, drop) for item, drop, rarity in loot])
denom = 10**(max([float(str(drop)[::-1].find(".")) for item, drop, rarity in loot])+1)
items = sum(list([item]*math.floor(denom*(droprate/100)) for item, droprate, rarity in loot), [])

#__name = input("What is the name of your Hero? ")
#__class = input("What class would you like your Hero to be? ")
__name = "Goose"
__class = "Vagabond"
__item = random.choice(items) + " of the " + random.choice(nouns).capitalize()
__inventory = [type("Item", (object,),{
	"name":item + " of the " + random.choice(nouns).capitalize(),
	"level":0,
	"type":item
}) for item in random.choices(items, k=100)]

Hero = type("Hero", (object,), {
	"item": __item,
	"name":__name,
	"_class":__class,
	"inventory":__inventory,
	"health":100,
	"gold":250
	#"__init__":test
})

os.system("cls")
def viewInventory(Hero):
	print(c.color_text(f"{Hero.name}: {Hero._class}", classes[Hero._class]["color"]))
	print(" ")
	print("\033[4mInventory\033[0m\n")
	for item in Hero.inventory:
		item.drop = loot_rates[item.type]
		item.rarity = loot_rarities[item.type]
		print(c.color_text(f"{item.name} ; {item.rarity}, {item.drop}%", rarities[item.rarity]))
viewInventory(Hero)
while True:
	pass