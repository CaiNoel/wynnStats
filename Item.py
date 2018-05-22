# Imports packages
import requests
import json
import flask
import math
# Gets the name of the players item
item = input(("What item are you looking for?"))

# Accesses item site
itemStats = requests.get('https://api.wynncraft.com/public_api.php?action=itemDB&search=' + item)
itemStats = json.loads(itemStats.text)
# Gets the item stats
for identification in (itemStats["items"]) :
    # Print item name, tier, and type
    displayName = identification["name"]
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print (displayName.upper())
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    if (identification["category"] != "accessory"):
        print (identification["tier"], (identification["type"]), "// Level Minimum:", identification["level"])
    else:
        print(identification["tier"], identification["accessoryType"], "// Level Minimum:", identification["level"])
    if (identification["strength"] != 0):
        print("Strength Required:", identification["strength"])
    if (identification["dexterity"] != 0):
        print("Dexterity Required:", identification["dexterity"])
    if (identification["intelligence"] != 0):
        print("Intelligence Required:", identification["intelligence"])
    if (identification["defense"] != 0):
        print("Defense Required:", identification["defense"])
    if (identification["agility"] != 0):
        print("Agility Required:", identification["agility"])
    if (identification["quest"] != None):
        print("Quest Required:", identification["quest"])
    if (identification["category"] == "armor") :
        if (identification["classRequirement"] != None) :
            print("Class Required:", identification["classRequirement"])
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    # Print item's base health and defenses (ONLY IF ARMOR)
    if (identification["category"] == "armor"):
        if (identification["health"] > 0):
            print (identification["name"], "gives", identification["health"], "health.", "(", "+", identification["health"], ")")
        if (identification["health"] < 0):
            print (identification["name"], "takes away", (identification["health"] * -1),  "health.", "(", identification["health"], ")")

        # For EARTH defense
        if (identification["earthDefense"] > 0):
            print (identification["name"], "gives", identification["earthDefense"], "earth defense.", "(", "+", identification["earthDefense"], "✤)")
        if (identification["earthDefense"] < 0):
            print (identification["name"], "takes away", (identification["earthDefense"] * -1),  "earth defense.", "(", identification["earthDefense"], "✤)")
        # For THUNDER defense
        if (identification["thunderDefense"] > 0):
            print (identification["name"], "gives", identification["thunderDefense"], "thunder defense.", "(", "+", identification["thunderDefense"], "✦)")
        if (identification["thunderDefense"] < 0):
            print (identification["name"], "takes away", (identification["thunderDefense"] * -1),  "thunder defense.", "(", identification["thunderDefense"], "✦)")
        # For WATER defense
        if (identification["waterDefense"] > 0):
            print (identification["name"], "gives", identification["waterDefense"], "water defense.", "(", "+", identification["waterDefense"], "❉)")
        if (identification["waterDefense"] < 0):
            print (identification["name"], "takes away", (identification["waterDefense"] * -1),  "water defense.", "(", identification["waterDefense"], "❉)")
        # For FIRE defense
        if (identification["fireDefense"] > 0):
            print (identification["name"], "gives", identification["fireDefense"], "fire defense.", "(", "+", identification["fireDefense"], "✹)")
        if (identification["fireDefense"] < 0):
            print (identification["name"], "takes away", (identification["fireDefense"] * -1),  "fire defense.", "(", identification["fireDefense"], "✹)")
        # For AIR defense
        if (identification["airDefense"] > 0):
            print (identification["name"], "gives", identification["airDefense"], "air defense.", "(", "+", identification["airDefense"], "❋)")
        if (identification["airDefense"] < 0):
            print (identification["name"], "takes away", (identification["airDefense"] * -1),  "air defense.", "(", identification["airDefense"], "❋)")
    # Print item's base damage (ONLY IF WEAPON)
    if (identification["category"] == "weapon"):
        # For NEUTRAL damage
        if (identification["damage"] != "0-0"):
            print (identification["name"], "deals", identification["damage"], "neutral damage.")
        # For EARTH damage
        if (identification["earthDamage"] != "0-0"):
            print (identification["name"], "deals", identification["earthDamage"], "earth damage.")
        # For THUNDER damage
        if (identification["thunderDamage"] != "0-0"):
            print (identification["name"], "deals", identification["thunderDamage"], "thunder damage.")
        # For WATER damage
        if (identification["waterDamage"] != "0-0"):
            print (identification["name"], "deals", identification["waterDamage"], "water damage.")
        # For FIRE damage
        if (identification["fireDamage"] != "0-0"):
            print (identification["name"], "deals", identification["fireDamage"], "fire damage.")
        # For AIR damage
        if (identification["airDamage"] != "0-0"):
            print (identification["name"], "deals", identification["airDamage"], "air damage.")
    # HEALTH REGEN %
    if (identification["healthRegen"] > 0):
        healthRegenPercent = math.floor(identification["healthRegen"])
        print((round(healthRegenPercent * 0.3)), "%", "   HEALTH REGEN   ", (round(healthRegenPercent * 1.3)), "%")
    if (identification["healthRegen"] < 0):
        healthRegenPercent = math.floor(identification["healthRegen"])
        print((round(healthRegenPercent * 1.3)), "%", "   HEALTH REGEN   ", (round(healthRegenPercent * 0.7)), "%")
    # MANA REGEN
    if (identification["manaRegen"] > 0):
        manaRegen = (identification["manaRegen"])
        if (round(manaRegen * 0.3) != 0):
            print((round(manaRegen * 0.3)), "/4s","   MANA REGEN   ",(round(manaRegen * 1.3)),"/4s")
        else:
            print("1", "/4s","   MANA REGEN   ",(round(manaRegen * 1.3)),"/4s")
    if (identification["manaRegen"] < 0):
        manaRegen = (identification["manaRegen"])
        print((round(manaRegen * 1.3)), "/4s","   MANA REGEN   ",(round(manaRegen * 0.7)),"/4s")
    # SPELL DAMAGE %
    if (identification["spellDamage"] > 0):
        spellDamage = (identification["spellDamage"])
        print((round(spellDamage * 0.3)), "%","   SPELL DAMAGE   ",(round(spellDamage * 1.3)),"%")
    if (identification["spellDamage"] < 0):
        spellDamage = (identification["spellDamage"])
        print((round(spellDamage * 1.3)), "%","   SPELL DAMAGE   ",(round(spellDamage * 0.7)),"%")
    # MELEE DAMAGE %
    if (identification["damageBonus"] > 0):
        damageBonus = (identification["damageBonus"])
        print((round(damageBonus * 0.3)), "%","   MELEE DAMAGE   ",(round(damageBonus * 1.3)),"%")
    if (identification["damageBonus"] < 0):
        damageBonus = (identification["damageBonus"])
        print((round(damageBonus * 1.3)), "%","   MELEE DAMAGE   ",(round(damageBonus * 0.7)),"%")
    print()
    print()
