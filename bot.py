import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(848558256439951450)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(848558300760375296)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(bot.larency)


bot.run('ODQ4NTM0NDU2NTU3ODk1NzQw.YLOBSw.tF4QZg7IaJp-0-fHpgJ-mDfY2y0')