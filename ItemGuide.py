from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import math
import urllib
import ssl
from itertools import groupby
app = Flask(__name__, static_url_path = "/static", static_folder = "static")
@app.route('/')
def display():
    return render_template('index.html')
@app.route('/home')
def main():
    return render_template('index.html')
@app.route('/wynn')
def load():
    return render_template('index.html')

@app.route('/wynn/itemSearch')
def itemSearch():
    global itemTier
    global displayName
    global identification
    itemTier = None
    displayName = None
    identification = None
    itemName = request.args.get("itemName")
    print (itemName)
    if itemName != None:
        context = ssl._create_unverified_context()
        itemName = itemName.replace(' ', '%20')
        itemStats = requests.get('https://api.wynncraft.com/public_api.php?action=itemDB&search=' + itemName)
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=itemDB&search=' + itemName, context=context)
        str_response = response.read().decode('utf-8')
        itemStats = (json.loads(str_response))
        itemStats = itemStats["items"]
        for identification in itemStats :
            displayName = identification["name"]
            itemTier = identification["tier"]
        itemName = itemName.replace('%20', ' ')
        return render_template("item.html", itemStats = itemStats, displayName = displayName, identification=identification, itemName=itemName)
    else:
        return render_template("itemSearch.html")

@app.route('/wynn/itemSearch/<itemName>')
def itemDisplay(itemName):
    global itemTier
    global displayName
    global identification
    itemTier = None
    displayName = None
    identification = None
    healthRegen = None
    if itemName != None:
        itemName = itemName.replace(' ', '%20')
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=itemDB&search=' + itemName, context=context)
        str_response = response.read().decode('utf-8')
        itemStats = (json.loads(str_response))
        itemStats = itemStats["items"]
        return render_template("itemResult.html", itemStats = itemStats, displayName = displayName, identification=identification, itemName=itemName, healthRegen=healthRegen)
    else:
        return render_template("itemSearch.html")

@app.route('/wynn/guildLeaderboard')
def guildLeaderboard():
    global n
    n = 1
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe=alltime', context = context)
    str_response = response.read().decode('utf-8')
    guildLeaderboard = (json.loads(str_response))
    guildLeaderboard = guildLeaderboard["data"]
    return render_template("guildLeaderboard.html", guildLeaderboard = guildLeaderboard, n=n)

@app.route('/wynn/guildLanding')
def guildLanding():
    return render_template("guildLanding.html")

@app.route('/wynn/guildSearch')
def guildSearch():
    global guild
    guild = None
    guildName = request.args.get("guildName")
    print (guildName)
    if guildName != None:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=statsSearch&search=' + guildName, context=context)
        str_response = response.read().decode('utf-8')
        guildResults = (json.loads(str_response))
        guildResults = guildResults["guilds"]
        return render_template("guildResults.html", guildResults=guildResults, guildName=guildName, guild=guild)
    else:
        guildName = request.args.get("guildName")
        return render_template("guild.html")

@app.route('/wynn/guildSearch/<guildName>')
def guildDisplay(guildName):
    if guildName != None:
        guildName = guildName.replace(' ', '%20')
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=guildStats&command=' + guildName, context=context)
        str_response = response.read().decode('utf-8')
        guildStats = (json.loads(str_response))
        guildMembers = guildStats["members"]
        return render_template("guildDisplay.html", guildStats = guildStats, guildMembers = guildMembers)
    else:
        return render_template("guildResults.html")

@app.route('/wynn/playerSearch')
def playerSearch():
    global player
    player = None
    playerName = request.args.get("playerName")
    print (playerName)
    if playerName != None:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=statsSearch&search=' + playerName, context=context)
        str_response = response.read().decode('utf-8')
        playerResults = (json.loads(str_response))
        playerResults = playerResults["players"]
        return render_template("playerResults.html", playerResults=playerResults, playerName=playerName, player=player)
    else:
        guildName = request.args.get("guildName")
        return render_template("player.html")

@app.route('/wynn/playerSearch/<playerName>')
def playerDisplay(playerName):
    if playerName != None:
        playerName = playerName.replace(' ', '%20')
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=playerStats&command=' + playerName, context=context)
        str_response = response.read().decode('utf-8')
        playerStats = (json.loads(str_response))
        playerClasses = list(playerStats["classes"])
        playTime =  round(playerStats["playtime"]/60)
        return render_template("playerDisplay.html", playerStats = playerStats, playerClasses = playerClasses, playTime=playTime)
    else:
        return render_template("playerResults.html")

@app.route('/wynn/playerSearch/<playerName>/<playerClass>')
def classDisplay(playerName, playerClass):
    if playerName != None and playerClass != None:
        playerName = playerName.replace(' ', '%20')
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen('https://api.wynncraft.com/public_api.php?action=playerStats&command=' + playerName, context=context)
        str_response = response.read().decode('utf-8')
        playerStats = (json.loads(str_response))
        classInformation = playerStats["classes"][playerClass]
        playerClassInfo = playerClass
        quests = playerStats["classes"][playerClass]["questsAmount"]
        questsToGo = quests.replace('/', '-')
        questsToGo = int((eval(quests)))
        l = [int(''.join(i)) for is_digit, i in groupby(quests, str.isdigit) if is_digit]
        questsCompleted = int((eval(quests))*100)
        questsCompleted = int((eval(quests))*100)
        questsToGo = quests.replace('/', '-')
        questsToGo = int((eval(questsToGo)))
        questsToGo = abs(questsToGo)
        return render_template("classDisplay.html", playerStats = playerStats, playerClass = playerClass, classInformation = classInformation, questsCompleted=questsCompleted, questsToGo=questsToGo)
    else:
        return render_template("guildResults.html")
if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0", port="8080")
