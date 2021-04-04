import discord
from discord.ext import commands
import os

TOKEN = 'ODE4ODc3NTY4MTI3NDY3NTcx.YEedKg.8TyZ0PK6tmkTuA9hwP507so79P4'

intents = discord.Intents.all()

PREFIX = '!'

client = commands.Bot(command_prefix = PREFIX, intents=intents)
client.remove_command("help")




@client.command()
async def load(ctx, extension):
	if ctx.author.id == 375240473184305164:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 375240473184305164:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 375240473184305164:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")







client.run(TOKEN)
