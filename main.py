import discord
import requests
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

users = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('$'):
        #await message.channel.send('look at this jay LUL, we the best')

    #this has 200+ moves for selected pokemon 
    pokemoves = []
        #######################################
    pokestats = []
    poketype = []
    pokeabl = []

    if message.content.startswith('$pokedex'):
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
                #can only write 1024 chars in one writing
                #arraySplitMoves = []
                #index = 0
                #count = 0
                #temp = []
                #bool = True
                #while bool:
                    #while count > 25:
                        #temp.append(pokemoves[index])
                        #index += 1
                        #count+=1
                    #count = 0
                    
                    #arraySplitMoves.append(temp)
                    #temp.clear()

                    #if index == len(pokemoves):
                        #break

                #bool = False
                #for i in arraySplitMoves:
                 
                    #embed1 = discord.Embed(title='moves')
                    #embed1.add_field(name="moves", value=arraySplitMoves[0])
                    #await message.channel.send(embed=embed1)        

                #print(arraySplitMoves)                 

            except Exception:
                pokemoves.clear()
                pokestats.clear()
                poketype.clear()
                pokeabl.clear()
                await message.channel.send("Something went wrong did you spell it correctly")




    
    if message.content.startswith('$join'):
       
        cmd1 = message.content.split(" ")
        await message.channel.send("First arg: " + cmd1[0] + "\n" + "Second arg: " + cmd1[1])

        users.append(cmd1[1])

        reEmbed = discord.Embed(title="thank you for registering")
        reEmbed.add_field(name="Your Rivals", value=users)
        await message.channel.send(embed=reEmbed)


    pokeFav = {}
    if message.content.startswith('$team'):
        
        cmd1 = message.content.split(" ")
        await message.channel.send("First arg: " + cmd1[0] + "\n" + "Second arg: " + cmd1[1])

        #read json pokedatabase
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/' + cmd1[1])
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


                   
    
        embed = discord.Embed(title=cmd1[1])
        embed.set_thumbnail(url=pokejson['sprites']['front_default'])  
        embed.add_field(name='Type', value=poketype, inline=False)
        embed.add_field(name='abilities', value=pokeabl)
        embed.add_field(name='Stats', value=pokestats, inline=False)
        await message.channel.send(embed=embed)

        

                
            
    
       
        

client.run('ODA1NTQxOTc0NTg4MjYwMzgy.YBcZbA.owxnZiYqYrqKLPFEOzQX7rgA08I')