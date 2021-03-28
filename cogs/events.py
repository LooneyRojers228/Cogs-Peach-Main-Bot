import discord
from discord.ext import commands



	
class Event(commands.Cog):

	def __init__(self,client):
		self.client = client



	@commands.Cog.listener()
	async def on_ready(self):
		print('Запущен бот!')
		await self.client.change_presence (status = discord.Status.online, activity = discord.Game('!tiktok | !help'))


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		pass


	@commands.Cog.listener("on_command_error")
	async def cooldown_message(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			embed = discord.Embed(title=f"Команду можно использовать только {error.cooldown.rate} раз в {error.cooldown.per} секунд", description=f"Попробуйте через {error.retry_after} секунд.", colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(embed=embed, delete_after=10)


def setup(client):
	client.add_cog(Event(client))

