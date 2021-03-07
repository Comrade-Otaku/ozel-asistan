import discord
import time
from discord.ext import commands

TOKEN = "bruh"

client = commands.Bot(command_prefix = "lx.")
client.remove_command("help")

@client.event
async def on_ready():
      print("Özel Asistan uyandı.")
      channel = client.get_channel(817726201514164236)
      await channel.send('Günaydın ev ahalisi, asistanınız uyandı. Ne isterdiniz? @here')
      
@client.command()
async def help(ctx, arg = "1"):
    if(arg=="1"):
        await ctx.send("```lx.help {Sayfa Numarası} - Komutları listeler\nlx.ping - Botun pingini aktarır.\nlx.ban - Kullanıcıyı yasaklar.\nlx.kick - Kullanıcıyı atar.\nlx.unban - Kullanıcının yasağını kaldırır.\nlx.avatar - Kullanıcının profil fotoğrafını gösterir.```")
      
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


client.run(TOKEN)
