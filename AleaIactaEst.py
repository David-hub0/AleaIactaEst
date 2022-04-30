import discord
import json
import unifier

from pathlib import Path

conf = json.loads(Path("./conf.json").read_text())
client = discord.Client()
discordBotToken = conf["token"]


@client.event
async def on_ready():
    """
    Ein rdy-check ob der bot sich mit discord verbinden kann
    """
    print('We have logged in as {0.user}'.format(client))


# Geschriebene Nachrichten werden nach '!Die' gescannt und dann wird gewürfelt
# das Schema ist immer: #Anzahl für wieviele Würfel geworfen werden sollen
#                       #D als Zeichen dafür, dass es sich um einen Würfel handelt
#                       #Typ für den Typen des Würfels
#                       #+ um eine einfache Zahl oder einen weiterern Würfel hinzuzufügen
# Beispiel '!Die 1D8+2D6+5' oder '1D20 +-1'
@client.event
async def on_message(message):
    content = message.content.strip().upper()
    chan = message.channel

    if str(chan.id) == conf["chanID"] and content.startswith('!DIE'):
        await chan.send(unifier.calculate(content))
    return


client.run(discordBotToken)
