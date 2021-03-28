import discord
import asyncio 
import datetime
import random
from discord.ext import commands





class User(commands.Cog):

	def __init__(self,client):
		self.client = client

	
	#ping
	@commands.command(aliases = ["pin"])
	@commands.cooldown(1, 60, commands.BucketType.user)
	async def ping(self, ctx):
		await ctx.message.delete()
		emb = discord.Embed (title = 'Пинг: {0} ms'.format(self.client.latency * 1000), colour = discord.Color.gold())
		await ctx.send(embed = emb,delete_after=30) 


#на лс ссылка
#ссылка на дс
	@commands.command(aliases = ["d"])
	@commands.cooldown(1, 60, commands.BucketType.user)
	async def ds(self, ctx):
		await ctx.message.delete()
		emb = discord.Embed (title = 'Ссылка на наш дискорд сервер :clipboard:', description='https://discord.gg/bWqMJSUy3z',colour = discord.Color.gold())
		await ctx.send(embed = emb,delete_after=30)

#об авторе бота
	@commands.command(aliases = ["avto"])
	@commands.cooldown(1, 60, commands.BucketType.user)
	async def avtor (self, ctx):
		await ctx.message.delete()
		emb = discord.Embed (title = f"Peach Bot created by **@LOONEY ROJERS#3966** ", description = f"[Ссылка на мой VK](https://vk.com/rojers228) \n Peach Bot Main, 2021", colour = discord.Color.gold())
		emb.set_thumbnail(url=ctx.bot.user.avatar_url)
		await ctx.send (embed = emb,delete_after=30)

# @client.command()
# @commands.cooldown(1, 60, commands.BucketType.user)  # Один раз в 60 секунд на пользователя (глобально)
# async def cmd(ctx, ...):


# @client.listen("on_command_error")
# async def cooldown_message(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         await ctx.send(f"{ctx.command.qualified_name} можно использовать только {error.cooldown.rate} раз в {error.cooldown.per} секунд. Попробуйте через {error.retry_after} секунд.")

# clear mess
	@commands.command(aliases = ["clea"])
	@commands.has_any_role(819292703589269514,817408828500213860,817408830240456754,817643991331766283)
	async def clear (self, ctx, amount : int):
		if amount > 100:
			await ctx.message.delete()
			emb = discord.Embed (title = ':x: Ошибка', description='{0.author.mention} Укажите число от 1 до 100'.format(ctx.message), colour = discord.Color.gold())
			await ctx.send(embed = emb, delete_after=30)
			return  
		if amount < 0:
			await ctx.channel.purge(limit = 1)
			emb = discord.Embed (title = ':x: Ошибка', description='{0.author.mention} Укажите число от 1 до 100'.format(ctx.message), colour = discord.Color.gold())
			await ctx.send(embed = emb, delete_after=30)
			return
		await ctx.channel.purge(limit = amount + 1)
		emb = discord.Embed (title = 'Удалено {} сообщений!'.format(amount), colour = discord.Color.gold())
		await ctx.send(embed = emb, delete_after=30)

# Kick
	@commands.command(aliases = ["kic"])
	@commands.has_permissions(administrator = True)

	async def kick (self, ctx, member: discord.Member, *, reason = None):
		emb = discord.Embed (title = 'Kick :wave:', colour = discord.Color.gold())
		await ctx.message.delete()

		await member.kick(reason = reason)
		emb.set_author (name = member.name, icon_url = member.avatar_url)
		emb.add_field (name = 'Kick user', value = 'Kicked user : {}'.format(member.mention))
		emb.set_footer (text = 'Был выгнан с сервера модератором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)
		await ctx.send (embed = emb, delete_after=30)

# Ban
	@commands.command(aliases = ["voteba"])
	@commands.has_permissions(administrator = True)
	async def voteban (self, ctx, member: discord.Member, *, reason = None):
		emb = discord.Embed (title = 'Ban :lock:', colour = discord.Color.gold())
		await ctx.message.delete()
		await member.ban(reason = reason)
		emb.set_author (name = member.name, icon_url = member.avatar_url)
		emb.add_field (name = 'Ban user', value = 'Baned user : {}'.format(member.mention))
		emb.set_footer (text = 'Был заблокирован модератором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)
		await ctx.send (embed = emb, delete_after=30)

	# Unban
	@commands.command(aliases = ["unba"])
	@commands.has_permissions(administrator = True)
	async def unban(self, ctx, *, member):
		await ctx.message.delete()
		emb = discord.Embed (title = 'Unban :unlock:', colour = discord.Color.gold())
		banned_users = await ctx.guild.bans()

		for ban_entry in banned_users:
			user = ban_entry.user
			await ctx.guild.unban (user)
			emb.set_author (name = member.name, icon_url = member.avatar_url)
			emb.add_field (name = 'Unban user', value = 'Unbaned user : {}'.format(member.mention))
			emb.set_footer (text = 'Был разблокирован модератором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)
			await ctx.send (embed = emb, delete_after=30)
			return

	#help 
	@commands.command(aliases = ["помощь"])
	@commands.cooldown(1, 45, commands.BucketType.user)
	async def help(self, ctx):
		await ctx.message.delete()
		emb = discord.Embed (title = 'Навигация по командам :clipboard:', colour = discord.Color.gold())
		emb.add_field(name ='Описание сервера :pencil:', value = 'Rojers Squad, правила можно прочитать в канале #правила')
		emb.add_field(name ='!clear :broom:', value = 'Очистка чата')
		emb.add_field(name ='!voteban :lock:', value = 'Бан участника')
		emb.add_field(name ='!kick :wave:', value = 'Кик с сервера')
		emb.add_field(name ='!unban :unlock:', value = 'Разбан участника')
		emb.add_field(name ='!tempmute :mute:', value = 'Мут участника')
		emb.add_field(name ='!unmute :speaker:', value = 'Размут участника')
		emb.add_field(name ='!ds :rose:', value = 'Ссылка на наш дс')
		emb.add_field(name ='!slot 🍒', value = 'Игра для развлечения')
		emb.set_footer (text ='Peach Bot Main', icon_url=ctx.bot.user.avatar_url)

		await ctx.send (embed = emb, delete_after=30)

	#mute
	@commands.command(aliases = ["tempmut"])
	@commands.has_any_role(819292703589269514,817408830240456754,817643991331766283,817408828500213860) 
	async def tempmute(self, ctx, member:discord.Member, time:int,reason):
		mute_role = discord.utils.get(ctx.message.guild.roles,id=818519675729608706)
		await ctx.message.delete()
		emb = discord.Embed (title = 'Mute :mute:', colour = discord.Color.gold())
		emb.set_author (name = member.name, icon_url = member.avatar_url)
		emb.add_field (name = 'Замучен', value = 'Muted user : {}'.format(member.mention))
		emb.add_field(name="Причина",value=reason,inline=False)
		emb.add_field(name="Время",value=time,inline=False)
		emb.set_footer (text = 'Был помещён в мут модератором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)
		await member.add_roles (mute_role)
		await ctx.send (embed = emb, delete_after=30)
		await asyncio.sleep(time * 60)
		await member.remove_roles(mute_role)
    


	#unmute
	@commands.command(aliases = ["unmut"])
	@commands.has_any_role(819292703589269514,817408830240456754,817643991331766283,817408828500213860) 
	async def unmute(self, ctx, member:discord.Member):
		unmute_role = discord.utils.get(ctx.message.guild.roles,id=818519675729608706)
		await ctx.message.delete()
		emb = discord.Embed (title = 'Unmute :speaker:', colour = discord.Color.gold())
		emb.set_author (name = member.name, icon_url = member.avatar_url)
		emb.add_field (name = 'Размучен', value = 'Unmuted user: {}'.format(member.mention))
		emb.set_footer (text = 'Был размучен модератором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)
		await member.remove_roles(unmute_role)
		await ctx.send (embed = emb, delete_after=30)




	#tiktok
	@commands.command(aliases = ["tikto"])
	async def tiktok(self, ctx):
		await ctx.message.delete()
		emb = discord.Embed (title = 'Наши ТикТок аккаунты ', colour = discord.Color.gold())
		emb.add_field(name ='Looney Rojers', value = f"[Ссылка](https://www.tiktok.com/@looneyrojers?)")
		emb.add_field(name ='Jason Rojers ', value = f"[Ссылка](https://www.tiktok.com/@jason_redrock?)")
		await ctx.send ( embed = emb, delete_after=60)

	#anekdot
	@commands.command(aliases = ["anekdo"])
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def anekdot(self, ctx):
		await ctx.message.delete()
		responses = ["я 1", "9", "12", "6","10", "8", "13", "5", "7","3", "11"]
		await ctx.send(f'Вот тебе анекдот: {random.choice(responses)}')

	#nick
	@commands.command(aliases = ["nicknam"])
	@commands.has_permissions(administrator = True)
	async def nickname(self, ctx, member: discord.Member, *, nickname=None):
		await ctx.message.delete()
		await member.edit(nick=nickname)
		emb = discord.Embed (title = f'Ник был изменен для {member.mention}', colour = discord.Color.gold())
		await ctx.send (embed = emb, delete_after=30)

	#Roll the slot machine 
	@commands.command(aliases = ["slo"])
	@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
	async def slot(self, ctx):
		await ctx.message.delete()
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)

		slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

		if (a == b == c):
			await ctx.send(f"{slotmachine} Все слоты совпали, вы выйграли! 🎉", delete_after=15)
		elif (a == b) or (a == c) or (b == c):
			await ctx.send(f"{slotmachine} Совпало два слота, вы выйграли! 🎉", delete_after=15)
		else:
			await ctx.send(f"{slotmachine} Вы проиграли( 😢", delete_after=15)




# @commands.command()
# async def about(self,ctx):
#     ramUsage = self.process.memory_full_info().rss / 1024**2
#     avgmembers = sum(g.member_count for g in self.bot.guilds) / len(self.bot.guilds)
#     embedColour = discord.Embed.Empty
#     if hasattr(ctx, 'guild') and ctx.guild is not None:
#         embedColour = ctx.me.top_role.colour
#     embed = discord.Embed(colour=embedColour)
#     embed.set_thumbnail(url=ctx.bot.user.avatar_url)
#     embed.add_field(name="Last boot", value=default.timeago(datetime.now() - self.bot.uptime), inline=True)
#     embed.add_field(
#         name=f"Developer{'' if len(self.config['owners']) == 1 else 's'}",
#         value=', '.join([str(self.bot.get_user(x)) for x in self.config["owners"]]),
#         inline=True
#     )
#     embed.add_field(name="Library", value="discord.py", inline=True)
#     embed.add_field(name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers:,.2f} users/server )", inline=True)
#     embed.add_field(name="Commands loaded", value=len([x.name for x in self.bot.commands]), inline=True)
#     embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

#     await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{self.config['version']}**", embed=embed)

# #Press F to pay respect 
# @client.command()
# async def f(ctx, *, text: commands.clean_content = None):
#     hearts = ['❤', '💛', '💚', '💙', '💜']
#     reason = f"f **{text}** " if text else ""
#     await ctx.send(f"**{ctx.author.name}** поставил {reason}{random.choice(hearts)}")
    
    
# #userinfo
# @commands.command()
# async def userinfo(ctx,member:discord.Member):
#     emb = discord.Embed (title = 'Информация о пользователе {}'.format(ctx.author.name), colour = discord.Color.gold())
#     emb.add_field(name ='Дата создания аккаунта', value = member.created_at,inline=False)
#     emb.add_field(name ='Присоединился к серверу', value = member.joined_at,inline=False)
#     emb.add_field(name ='Айди аккаунта', value = member.id,inline=False)  
#     emb.add_field(name ='Имеет роли') 
#     emb.set_thumbnail(url=member.avatar_url) 
#     emb.set_footer(text=f"Аккаунт: {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
#     await ctx.send (content=ctx.author.mention,embed = emb)

	# @client.listen("on_command_error")
	# async def cooldown_message(ctx, error):
	# 	if isinstance(error, commands.CommandOnCooldown):
	# 		await ctx.channel.purge(limit = 1)
	# 		embed = discord.Embed(title=f"Команду можно использовать только {error.cooldown.rate} раз в {error.cooldown.per} секунд", description=f"Попробуйте через {error.retry_after} секунд.", colour = discord.Color.gold(), timestamp=ctx.message.created_at)
	# 		await ctx.send(embed=embed, delete_after=10)

	@clear.error
	async def clear_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !clear [от 1 до 100]', colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
	@kick.error
	async def kick_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !kick {0.author.mention} [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@tempmute.error
	async def tempmute_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !tempmute {0.author.mention} [время] [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@unmute.error
	async def unmute_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !unmute {0.author.mention}'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@unban.error
	async def unban_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format(ctx.author.name),description='Пример: !unban namesloga13', colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format(ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)


	@voteban.error
	async def voteban_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format(ctx.author.name),description='Пример: !voteban {0.author.mention} [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format(ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=ctx.message.created_at)
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)


def setup(client):
	client.add_cog(User(client))

