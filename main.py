import discord
import requests
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

users = {}
allUsers = []
class userData:
    def __init__(self):
        self.user = ""
        self.favPoke = ""
        self.points = 0
        self.wins = 0
        self.losses = 0
        self.exp = 0
        self.teamName = "<None>"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('$'):
        #await message.channel.send('look at this jay LUL, we the best')

    

    pokemoves = []
    pokestats = []
    poketype = []
    pokeabl = []


    #1
    if message.content.startswith('*pokedex'):
        cmd = message.content.split(" ")
        await message.channel.send("First arg: " + cmd[0] + "\n" + "Second arg: " + cmd[1])

        
        if(cmd[1] != ""):
            try:

                #read json pokedatabase
                pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + cmd[1])
                #return json list
                pokejson = pokemon.json()
                #loop through moves and save to list
                for i in pokejson['moves']:
                    pokemoves.append(i['move']["name"])

                for i in pokejson['stats']:
                    pokestats.append(i['base_stat'])   

                for i in pokejson['types']:
                    poketype.append(i['type']['name'])   

                for i in pokejson['abilities']:
                    pokeabl.append(i['ability']['name'])       
    

                embed = discord.Embed(title=cmd[1])
                embed.set_thumbnail(url=pokejson['sprites']['front_default'])  
                embed.add_field(name='Type', value=poketype, inline=False)
                embed.add_field(name='abilities', value=pokeabl)
                embed.add_field(name='Stats', value=pokestats, inline=False)
                await message.channel.send(embed=embed)
            
            except Exception:
                pokemoves.clear()
                pokestats.clear()
                poketype.clear()
                pokeabl.clear()
                await message.channel.send("Something went wrong did you spell it correctly")




    
    #2
    if message.content.startswith('*join'):
        cmd = message.content.split(" ")
        #await message.channel.send("First arg: " + cmd[0] + "\n" + "Second arg: " + cmd[1])
        try:
            #add name to object
            p1 = userData()
            p1.user = cmd[1]
            allUsers.append(p1)

            embed = discord.Embed(title="Welcome")
            embed.add_field(name='name', value=cmd[1], inline=False)
            embed.add_field(name='Commands', value="*join [name] : add user\n *fav [poke name] [name] : add poke\n *profile [name] : view profile\n *win [name] : add points\n *loose [name] : remove points", inline=False)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*join [your name]\n\nYou do not need brackets")      
            await message.channel.send(embed=embed)






    if message.content.startswith('*fav'):
        cmd = message.content.split(" ")
        #await message.channel.send("First arg: " + cmd[0] + "\n" + "Second arg: " + cmd[1] + )

        try:
            pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + cmd[1])
            #return json list
            pokejson = pokemon.json()
            for obj in allUsers:
                if cmd[2] == obj.user:
                    obj.favPoke = pokejson['sprites']['front_default']
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*fav [poke name] [your name]\n\nYou do not need brackets\nCan not connect to API?")      
            await message.channel.send(embed=embed)    

        
        try:
            for obj in allUsers:        
                if cmd[2] == obj.user:
                    embed = discord.Embed(title=obj.user)
                    embed.set_thumbnail(url=obj.favPoke)
                    embed.add_field(name="new fav pokemon added " + cmd[1], value="just run the command again to change your fav")  
                    await message.channel.send(embed=embed)
                    break
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*fav [poke name] [your name]\n\nYou do not need brackets")      
            await message.channel.send(embed=embed)    
            






    if message.content.startswith('*profile'):    
        cmd = message.content.split(" ")
        try:
            for obj in allUsers:        
                if cmd[1] == obj.user:
                    embed = discord.Embed(title=obj.user)
                    embed.add_field(name="Team", value=obj.teamName, inline=False)
                    embed.set_thumbnail(url=obj.favPoke)
                    embed.add_field(name="Points", value=obj.points)  
                    embed.add_field(name="Wins", value=obj.wins)
                    embed.add_field(name="Losses", value=obj.losses)
                    embed.add_field(name="EXP", value=obj.exp, inline=False)
                    embed.set_footer(text="--------------------------------------------------")
                    await message.channel.send(embed=embed)
                    break
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*profile [your name]\n\nYou do not need brackets\nIssue reading the object")      
            await message.channel.send(embed=embed)    






    if message.content.startswith('*win'):  
        cmd = message.content.split(" ")
        try:
            for obj in allUsers:        
                if cmd[1] == obj.user:
                    obj.wins += 1 
                    obj.points += 10
                    obj.exp += 13

            for obj in allUsers:        
                if cmd[1] == obj.user:
                    embed = discord.Embed(title=obj.user)
                    embed.set_thumbnail(url=obj.favPoke)
                    embed.add_field(name="Points", value=obj.points)  
                    embed.add_field(name="Wins", value=obj.wins)
                    embed.add_field(name="Losses", value=obj.losses, inline=True)
                    embed.add_field(name="EXP", value=obj.exp, inline=False)
                    await message.channel.send(embed=embed)
                    break
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*win [poke name] [your name]\n\nYou do not need brackets\n Issue adding up the points")      
            await message.channel.send(embed=embed)           
            





            
    if message.content.startswith('*loose'):  
        cmd = message.content.split(" ")
        try:
            for obj in allUsers:        
                if cmd[1] == obj.user:
                    obj.losses += 1
                    obj.points -= 3
                    obj.exp += 5

            for obj in allUsers:        
                if cmd[1] == obj.user:
                    embed = discord.Embed(title=obj.user)
                    embed.set_thumbnail(url=obj.favPoke)
                    embed.add_field(name="Points", value=obj.points)  
                    embed.add_field(name="Wins", value=obj.wins)
                    embed.add_field(name="Losses", value=obj.losses, inline=True)
                    embed.add_field(name="EXP", value=obj.exp, inline=False)
                    await message.channel.send(embed=embed)
                    break     
        except:
            embed = discord.Embed(title="Error")   
            embed.add_field(name="details", value="*loose [your name]\n\nYou do not need brackets\n Issue subtracting points")      
            await message.channel.send(embed=embed)               

client.run('Discord token')
