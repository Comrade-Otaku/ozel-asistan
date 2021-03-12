import discord
import time
from discord.ext import commands
from discord import utils
from oaconfig import OzelAsistan
from discord.utils import get

client = commands.Bot(command_prefix = "ğ")
client.remove_command("help")

@client.event
async def on_ready():
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} sunucu ve {members} üye.'
    ))


@client.command()
async def help(ctx, arg = "1"):
    if(arg=="1"):
        await ctx.send("```ğhelp - Komutları listeler\nğping - Botun pingini aktarır.\nğban - Kullanıcıyı yasaklar.\nğkick - Kullanıcıyı atar.\nğunban - Kullanıcının yasağını kaldırır.\nğavatar - Kullanıcının profil fotoğrafını gösterir.\nğduyur - Duyuru yapar (Duyurabilir yetkisine sahip olmalısınız.)\nğprint - Aynı kullanıcı adı ve profil fotoğrafıyla botun mesaj yazmasını sağlar.\nğmesaj - Botun mesaj yazmasını sağlar.```")
      
@client.command()
@commands.guild_only()
async def ping(ctx):
    await ctx.send("```Pingim {}ms efendim.```".format(int(client.latency * 1000)))

@client.command()
@commands.guild_only()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@commands.has_role("Duyurabilir")
@client.command()
@commands.guild_only()
async def duyur(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg
	
	response = response[1:len(response)]
	await ctx.message.delete()
	embed = discord.Embed(title=ctx.message.author.name + " diyor ki:", description=response, color=0XFF1123)
	await ctx.send("@here")
	await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def attack(ctx, ulparator, devlet):
    if(ulparator=="ülke"):
        await ctx.send("```" + devlet + " ülkesine ateş açıldı!\nTanklar, ileri! Yönümüz " + devlet + " Ülkesi!```")
    elif(ulparator=="imparator"):
        await ctx.send("```" + devlet + " imparatorluğuna ateş açıldı!\nTanklar, ileri! Yönümüz " + devlet + " İmparatorluğu!```")
    else:
        await ctx.send("```Ülke mi imparator mu?\n\nÖrnek:\nğattack ülke Ermenistan```")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("```Efendim, ğ?```")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send("```Bu komut özel mesajlarda kullanılamaz.```")
    else:
        raise error

@client.command()
@commands.guild_only()
async def print(ctx, *args):
    response = ""

    for arg in args:
        response = response + " " + arg
	
    response = response[1:len(response)]
    
    webhooks = await ctx.channel.webhooks()
    webhook = utils.get(webhooks, name = "Özel Asistan")
    if webhook is None:
        webhook = await ctx.channel.create_webhook(name = "Özel Asistan")

    await webhook.send(response, username = ctx.author.name, avatar_url = ctx.author.avatar_url)
    await ctx.message.delete()

@client.command()
@commands.guild_only()
async def duygu(ctx):
        await ctx.send("```Discord'da Ğ emojisi olmadığı için mutsuzum -.-```")

@client.command()
@commands.guild_only()
async def mesaj(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg
	
	response = response[1:len(response)]
	await ctx.message.delete()
	await ctx.send("```" + response + "```")

client.run(OzelAsistan.TOKEN)
