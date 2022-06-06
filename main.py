from operator import length_hint
from re import A, L
import re
from turtle import st
import discord
from PIL import Image
from io import BytesIO
from discord import activity
from discord import member
from discord.embeds import EmptyEmbed
from discord.member import Member  # discord.py lib
import requests
import asyncio
import random
import json
from discord.ext.commands import cooldown, BucketType
from PIL import Image, ImageFilter
import datetime
from discord.client import Client
from discord.colour import Color
from discord.ext import commands
from requests import get
from discord import Button, ButtonStyle
from aiohttp import request
import urllib.request
prefix = ['l-' , 'L-']


client = commands.Bot(command_prefix=prefix , case_insensitive = True )
namex = ['']
namey = ['']
namew = ['']
namez = ['']
nameu = ['']
namev = ['']
client.remove_command('help')
client.remove_command('outlaw')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('l-'))
    print("ONLINE ! ")





@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.reply('Pong!')
    await ctx.send(f'`Bot Latency = {int(latency * 1000)}ms`')






@client.command(name="hi", aliases=["hello"])
async def hi(ctx):
    await ctx.reply('https://tenor.com/view/hello-gif-19947459')



@client.command(name="bye", aliases=["gn"])
async def bye(ctx):
    await ctx.reply('https://tenor.com/view/milk-and-mocha-hugs-bear-couple-love-cute-gif-17896170')

@client.command(name = 'samuray', aliases=['samu'])
async def samuray(message):
    await message.reply('<:PepeSmile:787405150603575336>')
    #await message.add_reaction('<:PepeSmile:787405150603575336>')
    #await message.add_reaction('<:PepeSmile:787405150603575336>')
@client.command(aliases = [ 'rage' ])
async def weeb(ctx):
    await ctx.reply('in work <:theekhaivaii:903334965956198450>')
# @client.event
# async def on_message(message):
#  if message.content.startswith('?afk gn'):
#     await message.reply('https://media.tenor.co/videos/d291ad85a526a4f3267970f156193440/mp4')

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def nsfw(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.reply(format(member.mention) + ', check dm ;)')
    await member.send(
        "https://cdn.discordapp.com/attachments/858743303252344845/944673099968815135/SPOILER_trolled-epic-trolling-troll-face-adriozer-trolling.gif")
    await member.send(
        "<https://bit.do/YeetYeet>")
    




@client.command(aliases=['sven'])
async def gintoki(ctx):
    toki = ['Randigami' ,'Gandugami' ,'Chutiyagami', 'Loduditya']

    embed_toki = discord.Embed(color= ctx.author.color, description ='**Gintoki Moment**')
    embed_toki.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/830328082724290611/bc40e3432b248b159c52e5da340ff710.webp?size=512')
    embed_toki.add_field(name="Akagami:", value = 'Exists', inline=False)
    embed_toki.add_field(name="Gintoki: ", value= random.choice(toki), inline=True)
    
    
    await ctx.reply(embed=embed_toki)



@client.command(name="seggs", aliases=["threesome"])
async def seggs(ctx, member: discord.Member = None, member1: discord.Member = None, member2: discord.Member = None):
    global i, j, k

    if not member:
        member = ctx.author
    if not member1:
        member1 = ctx.author
    if not member2:
        member2 = ctx.author
    name = member.display_name
    name1 = member1.display_name
    name2 = member2.display_name
    namez = name
    namev = name1
    nameu = name2

    i = int(len(namez))
    j = int(len(nameu))
    k = int(len(namev))
    if i > 15:
        i = int(i / 2)
        namex = namez[:i]
        namey = nameu[2:]
        namew = namev[2:2]
    elif k > 15:
        i = int(i / 4)
        k = int(k / 2)
        j = int(j / 4)
        namex = namez[:-i]
        namew = namev[-k:]
        namey = nameu[j:]
    elif j > 15:
        j = int(j / 2)
        namex = namez
        namey = nameu[j:]
        namew = namev
    elif i > 15 and j > 15 and k > 15:
        i = int(i / 2)
        j = int(j / 2)
        k = int(k / 2)
        namex = namez[:-i]
        namey = nameu[-3:]
        namew = namev[k:]
    else:
        i = int(i / 2)
        j = int(j / 2)
        k = int(k / 2)
        namex = namez[:-i]
        namey = nameu[-3:]
        namew = namev[k:]
    percent = random.randrange(101)
    if percent < 30:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}  💏  {name2}',description=f'**Seggs Quality**: {percent}%  😕\n\n**Seggs Alias**: {namex}{namew}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Seggs Chamber', icon_url= ctx.author.avatar_url)
    elif  69 > percent > 30:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}  💏  {name2}',description=f'**Seggs Quality**: {percent}%  😃\n\n**Seggs Alias**: {namex}{namew}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Seggs Chamber', icon_url= ctx.author.avatar_url)
    elif percent == 69:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}  💏  {name2}',description=f'**Seggs Quality**: {percent}%  🙀\n\n**Seggs Alias**: {namex}{namew}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Seggs Chamber', icon_url= ctx.author.avatar_url)
    elif percent > 90:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}  💏  {name2}',description=f'**Seggs Quality**: {percent}%  🤰\n\n**Seggs Alias**: {namex}{namew}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Seggs Chamber', icon_url= ctx.author.avatar_url)
    else:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}  💏  {name2}',description=f'**Seggs Quality**: {percent}%  💋\n\n**Seggs Alias**: {namex}{namew}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Seggs Chamber', icon_url= ctx.author.avatar_url)
    #await ctx.reply('**' + name + '  :flushed::point_right::ok_hand:  ' + name1 + ' = ' + namex + namey + '**')
    await ctx.reply(embed = segs) 
    #await ctx.reply(
        #'**' + name + '  :flushed::point_right::ok_hand:  ' + name1 + '   :flushed::point_right::ok_hand:  ' + name2 + ' = ' + namex + namew + namey + '**')


@client.command()
async def invite(ctx):
    await ctx.reply('use this link to add this shitty bot 😎🙏\nhttps://discord.com/api/oauth2/authorize?client_id=944235413499945000&permissions=1274666151121&scope=bot')


@client.command()
async def winter(ctx):
    await ctx.reply('https://cdn.discordapp.com/attachments/858743303252344845/950456155677818890/GIF-220307_234312.gif')


@client.command(name="segs", aliases=["sex", "fuck", "ship"])
async def segs(ctx, member: discord.Member = None, member1: discord.Member = None, ):
    global i, j

    if not member:
        member = ctx.author
    if not member1:
        member1 = ctx.author
    name = member.display_name
    name1 = member1.display_name

    namez = name
    nameu = name1

    i = int(len(namez))
    j = int(len(nameu))
    if i > 15:
        i = int(i / 2)
        namex = namez[:i]
        namey = nameu
    elif j > 15:
        j = int(j / 2)
        namex = namez
        namey = nameu[j:]
    else:
        i = int(i / 2)
        j = int(j / 2)
        namex = namez[:-i]
        namey = nameu[j:]

    percent = random.randrange(101)
    if percent < 30:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}',description=f'**Segs Quality**: {percent}%  😕\n\n**Segs Alias**: {namex}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Segs Chamber', icon_url= ctx.author.avatar_url)
    elif  69 > percent > 30:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}',description=f'**Sggs Quality**: {percent}%  😃\n\n**Segs Alias**: {namex}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Segs Chamber', icon_url= ctx.author.avatar_url)
    elif percent == 69:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}',description=f'**Segs Quality**: {percent}%  🙀\n\n**Segs Alias**: {namex}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Segs Chamber', icon_url= ctx.author.avatar_url)
    elif percent > 90:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}',description=f'**Seggs Quality**: {percent}%  🤰\n\n**Segs Alias**: {namex}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Segs Chamber', icon_url= ctx.author.avatar_url)
    else:
        segs = discord.Embed(title= f'\n{name}  💏  {name1}',description=f'**Segs Quality**: {percent}%  💋\n\n**Segs Alias**: {namex}{namey}', color=ctx.author.color)
        segs.set_author(name =f'{ctx.author.name}\'s Segs Chamber', icon_url= ctx.author.avatar_url)
    #await ctx.reply('**' + name + '  :flushed::point_right::ok_hand:  ' + name1 + ' = ' + namex + namey + '**')
    await ctx.reply(embed = segs) 


@client.command(case_insensitive=True)
async def slowmode(ctx, time: int):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.reply('Cannot Run Command ! Requires : ``Manage Messages``')
        return
    if time == 0:
        await ctx.reply('Slowmode Has Been Removed !')
        await ctx.channel.edit(slowmode_delay=0)
    elif time > 21600:
        await ctx.reply('You Cannot Set The Slowmode Higher Than `6 hours` !')
    else:
        await ctx.channel.edit(slowmode_delay=time)
        await ctx.reply(f'Slowmode Has Been Set To `{time} seconds` !')


@client.command(aliases=['clear'])
async def purge(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.reply('Cannot run command! Requires: ``Manage Messages``')
        return
    # await ctx.reply(':taocri:')
    amount = amount + 1
    if amount > 1010:
        await ctx.send('I can\'t delete more than `100` messages at a time!')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Sucessfully deleted `{amount - 1}` messages!')
        await ctx.channel.purge(limit=1)

@client.command()
async def pray(ctx, member: discord.Member = None ):
    #name = member.display_name
    #name_1 = name
    if not member or member == ctx.author:
        await ctx.reply('You Pray For Yourselves  <:AyaPray:916508556839256155> <:prayge:915560131612258314>')
    else:
        await ctx.reply(format(ctx.author.mention) + ' Prays For ' + member.mention + ' <:AyaPray:916508556839256155> <:prayge:915560131612258314>')

@client.command()
async def roast(ctx, member: discord.Member = None):
    if not member:
        # await ctx.send('Self roast? :moyai:\n')
        member = ctx.author
    content = get('https://evilinsult.com/generate_insult.php?lang=en&type=json').text
    data = json.loads(content, )
    # await ctx.send(format(member.mention)+',spam band kr :qiqidisgust:')
    await ctx.reply(format(member.mention) + ', ' + data["insult"] + ' ' + ':sob:')


@client.command(aliases = ['massping'])
@commands.is_owner()
async def griff(ctx, member: discord.Member = None, amount = 1 ):
    
    #await ctx.channel.purge(limit=1)


    if member is None:
              for i in range(0, amount):
                await ctx.send('<@905068632801943563> <:sedlyf:909883405108412447>')
                #await ctx.channel.purge(limit=1)

    else:
            for i in range(0, amount):
                await ctx.send(format(member.mention) + '<:sedlyf:909883405108412447>')
                #await ctx.channel.purge(limit=1)
    
    return


@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)
    
   

@client.command(aliases=['sus', 'amogus'])
async def varka(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    amogus = Image.open('images/amogus.png')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)

    avatar.resize((129, 128))
    amogus.paste(avatar, (297, 379))
    amogus.save('images/amogusav.png')
    await ctx.reply(file=discord.File('images/amogusav.png'))


@client.command()
async def sedlyf(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    amogus = Image.open('images/sed.png')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)

    avatar.resize((129, 128))
    amogus.paste(avatar.resize((150, 150)), (340, 150))
    amogus.save('images/sedav.png')
    await ctx.reply(file=discord.File('images/sedav.png'))

@client.command()
async def sick(ctx):

    message = await ctx.reply('<:wuttheee:955496232690794608>')
    await message.add_reaction('<:wuttheee:955496232690794608>')
@client.command(aliases = ['kr0n0s ', 'kronii'])
async def kronos(ctx):
    await ctx.reply('https://tenor.com/view/kotaro-gakuenbabysitters-gif-21075280')
@client.command(aliases = ['sob'])
async def crunchy(ctx, member: discord.Member = None):
    # await ctx.send('rukjao vai abhi nahi bani')
    if not member:
        member = ctx.author

    asset = member.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)
    avatar.resize((512, 512))
    avatar = avatar.convert("RGBA")

    img = Image.open('images/sobpng.png')

    img = img.convert("RGBA")
    a = 499
    l = random.sample(range(0,499), 11)
    for i in range(10):

        avatar.paste(img.resize((50, 50)), (l[i],l[i+1]) , img.resize((50, 50)))

    avatar.save('images/sobav.png')
    await ctx.reply(file=discord.File('images/sobav.png'), content=':sob:')


@client.command()
async def hasde(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    asset = member.avatar_url_as(size=256)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)
    avatar.resize((250, 250))
    avatar = avatar.convert("RGBA")

    img = Image.open('images/pensive.png')
    img = img.convert("RGBA")

    avatar.paste(img.resize((250, 250)), (0, 0), img.resize((250, 250)))

   
    avatar.resize((250, 250))
    avatar.save('images/hasde_av.png')
    await ctx.reply(file=discord.File('images/hasde_av.png'))


@client.command()
async def outlaw(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    amogus = Image.open('images/outlaw.png')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)

    avatar.resize((129, 128))
    amogus.paste(avatar.resize((190, 190)), (140, 89))
    amogus.save('images/lawav.png')
    await ctx.reply(file=discord.File('images/lawav.png'))


@client.command()
async def akagami(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    amogus = Image.open('images/gaki.png')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)

    avatar.resize((129, 128))
    amogus.paste(avatar.resize((320, 320)), (148, 74))
    amogus.paste(avatar.resize((320, 320)), (148, 74))
    amogus.save('images/gakiav.png')
    await ctx.reply(file=discord.File('images/gakiav.png') )


@client.command()
async def bruh(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    bruh = Image.open('images/moyai.png')
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    avatar = Image.open(data)

    bruh.paste(avatar.resize((425, 219)), (0, 100))
    bruh.save('images/moyaiav.png')
    await ctx.reply(file=discord.File('images/moyaiav.png'))


@client.command(aliases= ['avatar'])
async def av(ctx, member: discord.Member = None):
    if not member:
    
        member = ctx.author

    embed2 = discord.Embed(title=f"{member}'s Avatar \nNickname: `{member.display_name}`\n", colour=member.colour, timestamp=ctx.message.created_at)
    embed2.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed2.set_image(url='{}'.format(member.avatar_url))
    await ctx.reply(embed=embed2)




@client.command(name='gay' , aliases = ['weebkun'] )
@commands.cooldown(1, 10, commands.BucketType.user)
async def gay(ctx,member: discord.Member = None):
    gay = str(random.randrange(101))
    if member is None:
        member = ctx.author
    if member.id == 549023304124465163:
        gay = '10000'; 
    elif member.id == 434254619842183168 or member == ctx.author:
        gay = '-100'
        
    embed=discord.Embed(title= format(member.display_name) + "'s " 'Gay percentage', colour=member.colour,description = format(member.display_name) + ' is ' + gay + '%'  + ' Gay <:kokoOnegai:916355927219798016>' )   
    embed.set_thumbnail(url='https://c.tenor.com/hoek3uzGwQAAAAAC/u-are-gay-gay.gif')
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  

    if gay == '100':    
        await ctx.send(format(member.mention) + 'Lmao Gay ')

@client.command(name = 'pp', aliases=['dick'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def pp(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    length = '='
    n = random.randint(0,10)
    if member.id ==434254619842183168:
        n = 9
    embed1=discord.Embed(title= format(member.display_name) + "'s " 'pp size', colour=member.colour,description = '8' + (length*n)+ 'D'  )
    embed1.set_thumbnail(url='https://c.tenor.com/5xQcctB4hTwAAAAC/yes-chad.gif')
    embed1.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)

    embed2=discord.Embed(title= format(member.display_name) + "'s " 'pp size', colour=member.colour,description = '8' + (length*n)+ 'D'  )
    embed2.set_thumbnail(url='https://preview.redd.it/afp0ri5iq3u51.png?auto=webp&s=1f4cbdac2563cfa9526a62b0e77331ff140b97c2')
    embed2.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    if n <= 4:
        await ctx.reply(embed=embed2)
    
    else:
        await ctx.reply(embed=embed1)


@client.command(case_insensitive=True, aliases=["remind", "remindme"])
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    #print(time)
    #print(reminder)
    user = ctx.message.author
    #embed = discord.Embed(color=0x55a7f7, timestamp=ctx.message.created_at)
    #embed.set_footer(
        #icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        await ctx.reply('specify what do you want me to remind you about <:TaoCri:924350922497347644>')  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h") :
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        await ctx.reply('Specify a proper duration <:TaoCri:924350922497347644>')
    elif seconds < 5:
        await ctx.reply('Min 5 seconds <:TaoCri:924350922497347644>')
    elif seconds > 7776000:
        await ctx.reply('Max 90 days <:TaoCri:924350922497347644>')
    else:
        remind  = discord.Embed(title = 'Reminder Set' , colour=user.colour ,  description = f"will remind you about {reminder} in {counter} , <:sedlyf:909883405108412447>")
        await ctx.reply(embed = remind)
        #await ctx.reply(f"will remind you about {reminder} in {counter} , <:sedlyf:909883405108412447>")
        await asyncio.sleep(seconds)
        await ctx.author.send(f"reminder about {reminder} ")
        return

@client.command(aliases = ['emojipasta'])
#@commands.is_owner()
async def emoji(ctx, *, message):
 
    msg = message.split()
    emotes = [

        
            '😈', '😎','💫', '👻', '👹', '👿', '💩', '👺', '💛', '💕', '😬', '😏', '😊' ,'💯', '💥', '👾', '💣', '💟', '😂', '😍', '😘', '🙄', '😀', '😁', '🤣', '😃', '😄', '😅', '😋', '😗', '😆', '😉', '😙', '😚', '☺️', '🙂', '🤗', '😐', '😑', '😶', '😥', '😮', '🤐', '😯', '😪', '😫', '😴', '😌','😛', '😜', '😝', '🤤' ,'😒', '😓', '😔', '😕', '🙃', '☹️', '🤑', '😲', '🙁', '😖', '😞', '😟' ,'😤', '😢', '😭', '😦', '😧', '😨', '😩', '😰', '😱', '😳','😵',  '😡', '😠' ,'😷', '🤒', '🤢', '🤕', '🤧', '😇', '🤠', '🤡', '🤥', '🤓', '💀', '👽', '🤖','😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '💨', '🕳', '💋', '💌', '🙈', '☠️', '🙊', '💦', '👁️‍🗨️', '💓', '💔', '💖', '💗', '💘','💙', '💚', '💜', '💝', '💞', '💢', '💤', '💬', '💭', '🖤', '🗨', '🗯', '🧡', '❣️', '🤪', '🤬', '🤯', '🥵', '🥶', '🤨', '🤩', '🥰', '🤫', '🤭', '🥳', '🥴', '🥺' ,'🧐' ,'🤮', '🥱', '🤎', '🤍'
                ]
    emo = ''
    
    for i in range(len(msg)):
        n = random.randint(0,1)
        if n == 1 :
            emo = emo + f' { (random.choice(emotes))} ' + str(msg[i])
        else:
            emo = emo + f' { (random.choice(emotes))}{(random.choice(emotes))} ' + str(msg[i])
    embed = discord.Embed(color = discord.Color.red())
    embed.add_field(name= 'Emojipasta', value = emo)
    await ctx.send(embed = embed)
@client.command()
@commands.is_owner()
async def test3(ctx, *,message):
    #mention = message.mentions
   # tag = str(mention[0])
    message = message.lower()
    msg = list(message.strip(""))
    await ctx.send(msg)
    emoji = ''

    for i in range(0, len(msg)):
        if msg[i] == ' ':
            emoji = emoji + '  '
        elif msg[i] == '@':
            emoji = emoji + f'🌀'
        else:
            emoji = emoji + f':regional_indicator_{msg[i]}: '
    await ctx.send(emoji)


@client.command()
async def whois(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
        roles = [role for role in ctx.author.roles]

    else:
        roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name="User Info: ")
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="User Name:", value=member.display_name, inline=False)
    # embed.add_field(name="Discriminator:", value=member.discriminator, inline=False)
    # embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
    # embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
    embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"),
                    inline=False)
    embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Top Role:", value=member.top_role, inline=False)
    embed.add_field(name="Bot?:", value=member.bot, inline=False)
    await ctx.reply(embed=embed)


client.sniped_messages = {}


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)


@client.command()
async def snipe(ctx):
    embed_error = discord.Embed(color=discord.Color.red())
    embed_error.add_field(name="**Error !**", value=str("Could not find any message to snipe"))
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send(embed=embed_error)
        return

    embed_snipe = discord.Embed(color=discord.Color.from_rgb(47, 61, 222), timestamp=time)
    embed_snipe.add_field(name = 'Sniped message:', value = str(contents))
    embed_snipe.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed_snipe.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed_snipe)


client.esniped_messages = {}
client.esniped_messages_after = {}

@client.event
async def on_message_edit(message_before, message_after):
    client.esniped_messages[message_before.guild.id] = (
        message_before.content, message_before.author, message_before.channel.name, message_before.created_at)
    client.esniped_messages_after[message_after.guild.id] = (message_after.content, message_after.created_at)

@client.command()
async def esnipe(ctx):
    embed4 = discord.Embed(color=discord.Color.red())
    embed4.add_field(name="**Error !**", value=str("Could not find any message to snipe"))
    try:
        contents, author, channel_name, time = client.esniped_messages[ctx.guild.id]
        contents_after,time_after = client.esniped_messages_after[ctx.guild.id]
        
    except:
        await ctx.channel.send(embed=embed4)
        return

    embed_esnipe = discord.Embed(color=discord.Color.from_rgb(47, 61, 222), timestamp=time)
    embed_esnipe.add_field(name = 'Original Message:', value = str(contents), inline=False)
    embed_esnipe.add_field(name = 'Edited Message:', value = str(contents_after))
    embed_esnipe.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed_esnipe.set_footer(text=f" in : #{channel_name}")

    await ctx.channel.send(embed=embed_esnipe)

@client.command()
async def test(ctx, member: discord.Member = None):
  #user = client.get_user('434254619842183168')
  if member.id == 434254619842183168:
    await member.send(f'yes')
    #print(type(member.id))


@client.command(aliases=["commands"])
async def help(ctx, message = ''):
    page1 = discord.Embed(
        title = '      Help Page 1/3',
        description = " **General Commands**\n**Prefix** = 'l-'\n\n**COMMANDS**",
        colour = 0x0000ff
    
    )
    page1.set_author(name = f'{client.user.name}')
    page1.add_field(name='`help  `', value='Shows the list of commands', inline=False)
    #page1.add_field(name='``purge  ``', value='Clears the amount of messages mentioned', inline=False)
    page1.add_field(name='`hello  `', value='Hi;)', inline=False)
    page1.add_field(name='`av `', value='view the avatar of user ', inline=False)
    page1.add_field(name='`snipe `', value='Snipes the recently deleted message ', inline=False)
    page1.add_field(name='`esnipe `', value='Snipes the recently edited message ', inline=False)
    page1.add_field(name='`say <message content>`', value='make the bot say something ', inline=False)
    #page1.add_field(name='``say <message content>``', value='make the bot say something ', inline=False)
   # page1.add_field(name='``Invite  ``', value='Sends the link to invite this bot in your guild', inline=False)
   
   # page2 = discord.Embed (
    #    title = '      __Help Page 2/4__',
   #     description = "       Void's Bot's Music Commands\nPrefix = '_'\nThis bot uses a pre built music library 'dismusic'\n**COMMANDS**",
  #      colour = discord.Colour.purple()
  #  )
   # page2.add_field(name='``connect ``', value='Connect the player to voice channel', inline=False)
   # page2.add_field(name='``disconnect ``', value='Disconnect the player from voice channel', inline=False)
  #  page2.add_field(name='``equalizer ``', value='Set equalizer', inline=False)
  #  page2.add_field(name='``loop ``', value='Set loop to ``NONE``, ``CURRENT`` or ``PLAYLIST``', inline=False)
   # page2.add_field(name='``nowplaying ``', value="What's playing now?", inline=False)
  #  page2.add_field(name='``pause ``', value='Pause the player', inline=False)
  # page2.add_field(name='``play ``', value='Play or add song to queue', inline=False)
  #  page2.add_field(name='``queue ``', value="Player's current queue", inline=False)
  #  page2.add_field(name='``resume ``', value='Resume the player', inline=False)
   # page2.add_field(name='``seek ``', value='Seek the player backward or forward', inline=False)
   # page2.add_field(name='``skip ``', value='Skip currently playing song', inline=False)
   # page2.add_field(name='``volume ``', value='Set volume', inline=False)
  #  page2.set_author(name = f'{bot.user.name}',icon_url='https://media.discordapp.net/attachments/805723485372284932/912702901841981470/1634727211621.jpg')



    page2 = discord.Embed(
        title = '      Help Page 2/3',
        description = f"  **Cringe Commands**\n**Prefix** = 'l-'\n\n**COMMANDS**",
        colour = 0x0000ff
    
    
    )
    #page4.add_field(name='``meme  ``', value='Sends a random meme from a subreddit', inline=False)
    #page4.add_field(name='``joke  ``', value='Sends a joke', inline=False)
    page2.add_field(name='`roast  `', value='Get roasted by  a robot', inline=False)
    page2.add_field(name='`bruh  `', value='Turns anyone into a BRUH MOMENT', inline=False)
    page2.add_field(name='`sedlyf  `', value="<:sedlyf:909883405108412447> moment", inline=False)
    page2.add_field(name='`gay `', value='Idk man, thats pretty gay', inline=False)
    page2.add_field(name='`crunchy  `', value='Sobbing all the way', inline=False)
    page2.add_field(name='`akagami  `', value='Become a gaki', inline=False)
    page2.add_field(name='`gintoki  `', value='Bully akagami', inline=False)
    page2.add_field(name='`samu  `', value=':pepesmile:', inline=False)
    page2.add_field(name='`varka/amogus  `', value='Turn into amogus', inline=False)
    page2.add_field(name='`hasde  `', value='Hasde 😃chehreya 🙂da matlab ❓eh nhi 🚫hunda ki ohnanu koi 😔takleef 😖nhi hundi', inline=False)
    page2.add_field(name='`nsfw   `', value='For the horni peeps ;)', inline=False)
    page2.add_field(name='`segs @user   `', value='Have segs with someone ;)', inline=False)
    page2.add_field(name='`seggs @user1 @user2   `', value='Have threesome segs ;o', inline=False)
    page2.add_field(name='`pp/dick    `', value='Check pp size 0_0', inline=False)
    page2.add_field(name='`hug    `', value='hug someone', inline=False)
    page2.add_field(name='`pat    `', value='pat someone', inline=False)
    page2.add_field(name='`emoji    `', value='create an emojipasta', inline=False)
    
    page2.set_author(name = f'{client.user.name}')
    
    page3 = discord.Embed(
        title = '      Help Page 3/3',
        description = f"  **Action Commands**\n**Prefix** = 'l-'\n\n**COMMANDS**",
        colour = 0x0000ff
    )
    list = ['bully',
        'slap',
        'kill',
        'kick',
        'cuddle',
        'cry',
        'awoo',
        'kiss',
        'lick',
        'pat',
        'smug',
        'bonk',
        'yeet',
        'blush',
        'smile',
        'wave',
        'highfive',
        'handhold',
        'nom',
        'bite',
        'glomp',
        'wink',
        'poke',
        'dance',
        'cringe']

    for i in range (len(list)):


        
        page3.add_field(name=f'`{list[i]}`', value=f'{list[i]} someone', inline=True)





    


    pages = [page1, page2 , page3]
    
    if message == '':

        message = await ctx.send(embed = page1)
        await message.add_reaction('◀')
    
        await message.add_reaction('▶')
    

        def check(reaction, user):
            return user == ctx.author

        i = 0
        reaction = None

        while True:
            if i < 2:
            
                if str(reaction) == '◀':
                    i -= 1  
                    await message.edit(embed = pages[i])
                    print(i)
       # elif str(reaction) == '◀':
       #     if i > 0:
            #    i -= 1
           #     await message.edit(embed = pages[i])
                elif str(reaction) == '▶':
            #await message.remove_reaction
            
                    i += 1
                    await message.edit(embed = pages[i])
                    print(i)
            else:
                i = 0
                await message.edit(embed = pages[i])
                print(i)
        #elif str(reaction) == '⏭':
            #i = 4
            #await message.edit(embed = pages[i])

            try:
                reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break
        await message.clear_reactions()
    elif message == '1' or message == 'general':
        await ctx.send(embed = page1)
    elif message == '2' or message == 'cringe':
        await ctx.send(embed = page2)
    elif message == '3' or message == 'action':
        await ctx.send(embed = page3)
    

    
@client.command(name='meme') #meme command
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", colour=ctx.author.color ).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)




@client.command(name = 'cat')
@commands.cooldown(1, 10, commands.BucketType.user)
async def cat(ctx):
    link = 'https://api.thecatapi.com/v1/images/search'
    content = get(link).text
    data = json.loads(content, )
    d = data[0]
    cat = discord.Embed(
        title = 'Here, have a cat',
        description = 'a random cat image <:neko:851307202115010600>',
        colour = ctx.author.colour
        
            )
    cat.set_image(url = d['url'])
    await ctx.send(embed = cat)

@client.command(name = 'dog' , aliases = ['dogmelon'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def dog(ctx):
    link = 'https://dog.ceo/api/breeds/image/random'
    content = get(link).text
    data = json.loads(content, )

    dog = discord.Embed(
        title = 'Here, have a doggo',
        description = 'a random dog image <:DogMelon:889104049486569483>',
        colour = ctx.author.colour
        
            )
    dog.set_image(url = data['message'])
    await ctx.send(embed=dog)


@client.command()
@commands.is_owner()
async def test1(ctx,*, member: discord.Member = None):

  if not member:
        member = ctx.author
    
  hugAPI = urllib.request.urlopen('https://api.waifu.pics/sfw/waifu')
  hugData = json.load(hugAPI)
  hugUrl = hugData['url']
  embed=discord.Embed()
  embed.set_image(url=hugUrl)
  await ctx.send(embed=embed)
  
#client.remove_command('test1')

@client.command(name = 'waifu' , aliases = ['wifu'])
@commands.cooldown(1, 15, commands.BucketType.user)
async def waifu(ctx , member: discord.Member = None):
    link = 'https://api.waifu.pics/sfw/waifu'
    content = get(link).text
    data = json.loads(content, )
    if not member:
        member = ctx.author
    wifu = discord.Embed(
        title = f'{member.display_name} \'s waifu <:Ganyulove:920238111403937794>',
        colour = member.colour
            )
    wifu.set_image(url = data['url'])
    await ctx.send(embed=wifu)

f_reason = []
@client.command(name = 'f',aliases= ['respect'] )
@commands.cooldown(1, 15, commands.BucketType.user)
async def respect(ctx,*, message = ''):
    embed = discord.Embed(         
    
    colour = ctx.author.color
                )
    embed.set_author(name =f'{ctx.author.name}', icon_url = ctx.author.avatar_url)
    embed.add_field(name = f'Press F to pay respects for', value = f'{format(message)}' )
   # msg = await ctx.send(f'Press <:press_f:976042321940480030> to pay respects for **{message}**')
    msg = await ctx.send(embed = embed) 
    await msg.add_reaction('<:press_f:976042321940480030>')
    f_reason.append(message)

# global stop_var 
# @client.command(name='memestop')
# async def memestop(ctx):
#     await ctx.send("Stopped")
 
#     stop_var = True



# @client.command()
# async def memeloop(ctx):
#    # stop_var = False
#     #while (not stop_var):

#      content = get("https://meme-api.herokuapp.com/gimme").text
#      data = json.loads(content,)
#      meme = discord.Embed(title=f"{data['title']}", colour=discord.Color.purple() ).set_image(url=f"{data['url']}")
#      await ctx.reply(embed=meme)
#      print(stop_var)
#      await asyncio.sleep(2)
#      if stop_var == True:
#          return
#    #  def check(ctx):
#             #return not ctx.author.bot and ctx.command.name == "memestop"
#      #try:
#        #     if await bot.wait_for("command", check=check, timeout=1.5):
#                 #stop_var = True
#      #except asyncio.TimeoutError:
#       #      print()





#-------------------------------------------------------economy sys------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command(aliases=['bal'])
@commands.is_owner()
async def balance(ctx,user: discord.Member = None):
    if not user:
        user = ctx.author

    await open_account(user)
    user = user
    users = await get_eco_data()
    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']

    bal = discord.Embed(title = f"{user.name}'s GII balance ", colour= 0x000080  ,description ='**Wallet**: '+ '<:gems:919294512847786045> '+ str(wallet_amt) + '   ,  **Bank**:  ' + '<:gems:919294512847786045> ' +str(bank_amt) ,timestamp=ctx.message.created_at)
    bal.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    bal.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/858743303252344845/980106603707637840/FTh_5FxXoAIkxw_.jpg')
    await ctx.send(embed = bal)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.is_owner()
async def beg(ctx):
    user = ctx.author
    await open_account(ctx.author)
    beg_list= ['SamuRay','Griffin','YeXiU', 'Drake', 'Falme', 'Varka','Frosty','Crunchy','Kr0n0s', 'SiCK', 'Gintoki', 'Akagami', 'ITACHY', 'Matrix', 'Lordiee']

    response = ['true','false']

    beg_choice= random.choice(beg_list)
    response_res= random.choice(response)
    refuse = ['said : **GN**', 'said : *Go away you peasant*','*Whined like a cow and refused*','said : *Go beg somewhere else*','said : *Kal Ana*' ,'said : <:QiQiDisgust:851307847185989642>' ,'said : <:TaoReally:945658343022792715>']
    res_confirm=random.choice(response)
    earning = random.randrange(301)
    if response_res == res_confirm:

      await update_bank(ctx.author,1*earning)
      
      await ctx.send(f'**{ctx.author.mention} begged {beg_choice}**') 
      await ctx.send(f'*{beg_choice} gave you **{earning}** poros!*')
      return
    else:
      
      await ctx.send(f'**{ctx.author.mention} begged {beg_choice}.**')
      await ctx.send(f'{beg_choice} {random.choice(refuse)}')
      return
@client.command()
@commands.is_owner()    
async def slots(ctx,amount=None):  
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount you want to put in the comamand")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount> bal[0]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive! you dumbass')
        return
    if amount < 50:
        await ctx.send('Minimum amount must be at least 50')
        return
    
    slot = ["\💮" , "\💠" , "\🌟" ,"\👑" , "\💰" , "\💗"  , "\🌞"]
    slot1 = random.choice(slot)
    slot2 = random.choice(slot)
    slot3 = random.choice(slot)
    slotOutput = f' {slot1}  {slot2}  {slot3} '.format(slot1, slot2, slot3)

    if slot1 == slot2 == slot3:
        await update_bank(ctx.author,4*amount)
        em18 = discord.Embed(title = f"Slots Machine for {ctx.author}",color = discord.Color.green(), timestamp=ctx.message.created_at)
        em18.add_field(name = slotOutput.format(slotOutput), value = f"You quadrupled your **{amount}** Primos!:moneybag: :moneybag: ")
        await ctx.send(embed = em18)
        return

    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        await update_bank(ctx.author,2*amount)
        em17 = discord.Embed(title = f"Slots Machine for {ctx.author} ",color = discord.Color.green(), timestamp=ctx.message.created_at)
        em17.add_field(name = slotOutput.format(slotOutput), value = f"You doubled your **{amount}** Primos!:money_with_wings: :money_with_wings: ")
        await ctx.send(embed = em17)
        return

    else:
        await update_bank(ctx.author,-1*amount)
        em19 = discord.Embed(title = "Slots Machine",color = discord.Color.red(),timestamp=ctx.message.created_at)
        em19.add_field(name = slotOutput.format(slotOutput), value = f"You lost **{amount}** poros!**\n **Better luck next time.")
        await ctx.send(embed = em19)
        return

@client.command(aliases=['give'])
@commands.is_owner()
async def send(ctx,member: discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    
    if amount == None:
        await ctx.send("Please enter the amount you want to send in the command")
        return
    user = ctx.author
    bal = await update_bank(ctx.author)

    amount = int(amount)
    
    if amount > bal[1]:
        await ctx.send('insufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    users = await get_eco_data()    
    
    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.display_name} gave {member.display_name} {amount} Primos!')




respects = 0 
reac_data= []
@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    
    i = 0
    
    if str(reaction.emoji) == '<:press_f:976042321940480030>' and user != client.user:
        print(reac_data)

        if user.name in reac_data:
            i += 1
        else:
            await channel.send(f'{user.mention} has paid respects for **{f_reason[0]}**')
            reac_data.append(user.name)
        




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Command On Cooldown!",description=f"Try again in {error.retry_after:.1f}s.")
        await ctx.reply(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('`Missing reqiured arguments!`')
    if isinstance(error, commands.NotOwner):
        await ctx.reply(f'Owner only command <:SadgePlant:964365569241534524>')
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Member not found')
    print(error)
@client.event

async def on_message(message , member: discord.Member = None ):
    ching = Image.open('images/15.png')
    ching_cheng = Image.open('images/ching.png')
    hanji = Image.open('images/sheesh.png')
    noo = Image.open('images/bruh.png')

   
    #if message.author == client.user:
        #return
  

    if 'bing chilling' in message.content.lower() :
        ching.save('images/chingcheng.png')
        await message.reply(file=discord.File('images/chingcheng.png'))

    if 'ching cheng hanji' in message.content.lower():
        ching_cheng.save('images/chingchenghanji.png')
        await message.reply(file=discord.File('images/chingchenghanji.png'))

    if 'Super Idol的笑容 都没你的甜' in message.content or 'taiwan is not a country' in message.content.lower():
        hanji.save('images/infinity.png')
        await message.reply(file=discord.File('images/infinity.png'))

    if 'taiwan is a country' in message.content.lower():
        noo.save('images/negative.png')
        await message.reply(file=discord.File('images/negative.png'))

    ##if '?afk gn' in message.content.lower():
    #    await message.reply('https://tenor.com/view/milk-and-mocha-hugs-bear-couple-love-cute-gif-17896170')
    #if 'Is it too late now ' in message.content.lower():
    #    await message.reply('<:SadgePlant:964365569241534524>')    

    await client.process_commands(message)
    


    list = [
        'bully',
        'slap',
        'kill',
        'kick',
        'hug',
        'pat',
        'cuddle',
        'cry',
        'awoo',
        'kiss', 
        'lick',
        'smug',
        'bonk',
        'yeet',
        'blush',
        'smile',
        'wave',
        'highfive',
        'handhold',
        'nom',
        'bite',
        'glomp',
        'wink',
        'poke',
        'dance',
        'cringe' ]    
    mssg = message.content.lower()
    msg = mssg[2:]
    #if message.content.startswith('l.') :
    for i in range(len(list)):
            if message.content.lower().startswith(f'l-{list[i]}') or message.content.lower().startswith(f'L-{list[i]}'):
                choice = list[i]
                link = f'https://api.waifu.pics/sfw/{choice}'
                content = get(link).text
                data = json.loads(content, )
                
                cat = discord.Embed(
                
                    
                    timestamp=message.created_at,
                #description = 'a random cat image <:neko:851307202115010600>',
                    colour = message.author.color
                )
                if not message.mentions:
    
                     cat.set_author(name = f'{str(message.author)[:-5]} {choice}-s  🤠'   , icon_url=message.author.avatar_url)
        
                    
                else:
                     member = message.mentions
                     name = str(member[0])
                  
                     cat.set_author(name = f'{str(message.author)[:-5]} {choice}-s  {name[:-5]} 🤠 '   , icon_url=message.author.avatar_url)
                    
                    
                                            
  
                #cat.set_author(name = f'{str(message.author)[:-5]} {choice}-s  {name[:-5]} '   , icon_url=message.author.avatar_url)
               
                cat.set_image(url = data['url'])
                cat.set_footer(text=f"Requested by: {message.author} ")
                await message.reply(embed=cat)

              

          
                #print(type(name))



async def open_account(user):
    users = await get_eco_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 100
    with open('bank.json',"w") as f:
        json.dump(users, f,indent=4)
    return True

async def get_eco_data():
    with open("bank.json","r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change = 0,mode = 'wallet'):
    users =  await get_eco_data()
    users[str(user.id)][mode] += change

    with open("bank.json" ,"w") as f:
        json.dump(users, f,indent=4)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal
        



@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send('?afk gn')
    await ctx.bot.logout() 

client.run("OTQ0MjM1NDEzNDk5OTQ1MDAw.Yg-pwQ.k_t-pD6PPQpuPcKbzpcuLfNbt-8")
