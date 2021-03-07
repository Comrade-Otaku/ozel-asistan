import discord
import time
from discord.ext import commands
from tinydb import TinyDB, Query

TOKEN = "bruh"

client = commands.Bot(command_prefix = "ğ")
client.remove_command("help")

@client.event
async def on_ready():
      print("Özel Asistan uyandı.")
      
@client.command()
async def help(ctx, arg = "1"):
    if(arg=="1"):
        await ctx.send("```ğhelp {Sayfa Numarası} - Komutları listeler\nğping - Botun pingini aktarır.\nğban - Kullanıcıyı yasaklar.\nğkick - Kullanıcıyı atar.\nğunban - Kullanıcının yasağını kaldırır.\nğavatar - Kullanıcının profil fotoğrafını gösterir.```")
      
@client.command()
async def ping(ctx):
    await ctx.send("```Pingim {}ms efendim.```".format(round(client.latency, 1) * 1000))

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"```{user} başarıyla atıldı.```")
  
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"```{user} başarıyla yasaklandı.```")

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"```{user} kişisinin yasağı başarıyla kaldırıldı.```")
    return

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@commands.has_role("Duyurabilir")
@client.command()
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
async def attack(ctx, *,  imparatorluk):
    await ctx.send("```" + imparatorluk + " ülkesine ateş açıldı!\nTanklar, ileri! Yönümüz " + imparatorluk + " İmparatorluğu!```")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("```Efendim, ğ?```")
    else:
        raise error

client.run(TOKEN)
