import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODQ4NTM0NDU2NTU3ODk1NzQw.YLOBSw.SAJuF3UCgl2RILnlIuaNRLmnncM')