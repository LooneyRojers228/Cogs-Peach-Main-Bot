import discord
from discord.ext import commands



	
class Event(commands.Cog):

	def __init__(self,client):
		self.client = client



	@commands.Cog.listener()
	async def on_ready(self):
		print('Запущен бот!')
		await self.client.change_presence (status = discord.Status.online, activity = discord.Game('!tiktok | !help'))


	async def on_raw_reaction_add(self, payload):
		if payload.message_id == config.POST_ID:
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id) 
			member = utils.get(message.guild.members, id=payload.user_id) 

			try:
				emoji = str(payload.emoji) 
				role = utils.get(message.guild.roles, id=config.ROLE[emoji],) 
			
				
				await member.add_roles(role)
					

				print('[SUCCESS] Пользователь {0.display_name} получил роль мероприятия {1.name}'.format(member, role))

				user = await Client.fetch_user(user_id=member)
				await user.send('test')





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

