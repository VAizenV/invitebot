import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

invites = {}


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_member_join(member):
    await bot.wait_until_ready()  # Attend que le bot soit complètement prêt
    guild = member.guild
    channel = guild.get_channel(1083893168854024215)  # ID du channel
    inviter = None
    for invite in await guild.invites():
        if invite.uses > invites.get(invite.inviter.id, 0):
            inviter = invite.inviter
            invites[invite.inviter.id] = invite.uses
    message = f"Bienvenue à {member.mention}, il a été invité par {inviter.mention} qui a maintenant {invites[inviter.id]} invitations"
    await channel.send(message)


@bot.command()
async def invite(ctx, member: discord.Member):
    inviter = None
    guild = ctx.guild
    for invite in await guild.invites():
        if invite.inviter.id == member.id:
            inviter = invite.inviter
            invites[invite.inviter.id] = invite.uses
            break
    if inviter is None:
        await ctx.send(f"{member.name} n'a pas été invité sur ce serveur")
    else:
        message = f"{member.name} a été invité par {inviter.mention} et a utilisé {invites[inviter.id]} invitations"
        await ctx.send(message)


bot.run("MTA4Mzg5Mjc2NzYxMDEzMDU1Mg.GHv92R.lzDh70sKVATnQneStMxVJgJZtzlP2Rh12wy6RA")
