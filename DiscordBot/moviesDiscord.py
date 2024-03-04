'''
pip install imdbpy
pip install discord.py
pip install pycord
'''


'''
This is a simple script that uses IMDbPY to get the 
This script is used to fetch movie data from IMDb and send it as a message in Discord

'''
import discord
from imdb import Cinemagoer
import time
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
prefix = os.getenv('DISCORD_PREFIX')
link = os.getenv('DISCORD_LINK')
ownerid = os.getenv('DISCORD_OWNERID')


im = Cinemagoer()
command_prefix="!"
bot = discord.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("----------------------")
    print(command_prefix)

#COGS
#This loads the cogs like in line 16


@bot.slash_command(name='ping')
async def ping(ctx):
    print("ping")
    await ctx.send("I did something")
    #See if The Bot is Working#
    pingtime = time.time()
    pingms = await ctx.send("Pinging...")
    ping = time.time() - pingtime
    await ctx.send(":ping_pong:  time is `%.01f seconds`" % ping)


@bot.slash_command(name='hello')
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(name='botinvite')
async def botinvite(ctx):
    #A Link To Invite This Bot To Your Server!#
    await ctx.send("Check Your Dm")
    await ctx.whisper(link)

@bot.slash_command(pass_context=True,name='serverinvite')
async def serverinvte(ctx):
	"""Pm's A Invite Code (To The Server) To The User"""
	invite = await bot.create_invite(ctx.guild,max_uses=1,xkcd=True)
	await bot.send_message(ctx.message.author,"Your invite URL is {}".format(invite.url))
	await bot.say ("Check Your Dm: ")

@bot.slash_command(pass_context = True,name='serverinfo')
async def serverinfo(ctx):
    #Displays Info About The Server!#

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await bot.respond(embed = join);

@bot.slash_command(pass_context=True, name='setgame')
async def setgame(ctx, *, game):
    """Sets my game (Owner)"""
    if ctx.message.author.id == (ownerid):
        message = ctx.message
        await bot.delete_message(message)
        await bot.whisper("Game was set to **{}**!".format(game))
        await bot.change_presence(game=discord.Game(name=game))



@bot.slash_command(name='movie')
async def movie(ctx, *, arg):

    await ctx.defer()
    search = arg
    results = im.search_movie(search)

    try:
        global title,movies, ID
        title = results[0]
        movies = title.getID()
        ID = im.get_movie(movies)
        cast = ID['cast']
        topActors = 5
        


        print('\nMovie Information:\n')
        print('Title: ',title.get('title'))
        print('Year: ',ID['year'])
        print('Rating: ',ID['rating'],'/10')
        print('Genre: ',', '.join([i for i in ID['genres']]))
        print('Country: ',', '.join([i for i in ID['countries']]))
        print('Language: ',', '.join([i for i in ID['languages']]))
        #print('Director(s): ',ID['directors'])
        print('Top 5 Actors')
        for i in range(5): 
            print("    ", cast[i]) 
        

        embed = discord.Embed(
            
        title=f"Movie  Info - {title.get('title')}",
        description=f"This is the Information For The Movie {title.get('title')}",
        color=discord.Color.blue())
        
        embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/724567148030197781/86955239ccb703bd3361cfd8c74d0345.webp")
        embed.add_field(name='Title',value=f"{title.get('title')} ({ID['year']})",inline=True)
        embed.add_field(name="Ratings", value=f"{ID['rating']}")
        embed.add_field(name="Genre", value=f"{ID['genres']}")
        embed.add_field(name="Country", value=f"{ID['countries']}")
        embed.add_field(name="Languages", value=f"{ID['languages']}")
        #embed.add_field(name="Directors", value=f"{[d['name'] for d in ID['director']]}")
        embed.add_field(name="Actors", value=f"{[d['name'] for d in ID['cast']]}")
        embed.add_field(name="Plot",value=f"{ID['plot outline']}",)
        embed.set_author(name=bot.user.name,icon_url=bot.user.avatar.url)
        embed.set_footer(text= "Created By SargentRaju") #icon= "https://cdn.discordapp.com/avatars/354879221044084737/e5c6c1d9899ab42d26848de4dce4bb77.webp")


        await ctx.send_followup(embed=embed)
    except IndexError:
        await ctx.send_followup('No movies found with that title')

    

        


bot.run(token)