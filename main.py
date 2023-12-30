import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}",format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Hello")
    if message.content.startswith('image'):
        await message.channel.send(file = discord.File("trial.png"))
    if message.content.startswith('video'):
        await message.channel.send(file = discord.File("trial1.mp4"))
    if message.content.startswith('music'):
        await message.channel.send(file = discord.File("trial2.mp3"))
    if message.content.startswith('pdf'):
        await message.channel.send(file = discord.File("trial3.pdf"))

token = "MTE5MDMzMzQ1MTIxMjE2OTMxNg.GFw_qO.hYalzgv3T4ixSH6GPa5vKWW_h8SuJktZWJ2sk8"
client.run(token)
 