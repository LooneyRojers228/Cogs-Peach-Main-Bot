import discord
import asyncio 
import datetime
import random
import pandas as pd
from discord.ext import commands
from typing import Optional
from discord import Embed, Member
from datetime import datetime
from discord import utils
from discord.utils import get




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
		emb = discord.Embed (title = f"Peach Bot created by **@LOONEY ROJERS#3966** ", description = f"[Ссылка на мой VK](https://vk.com/rojers228) \n \n Peach Bot Main, 2021", colour = discord.Color.gold())
		emb.set_thumbnail(url=ctx.bot.user.avatar_url)
		await ctx.send (embed = emb,delete_after=30)



	@commands.command(aliases = ["меропртиятие1"])
	@commands.has_permissions(administrator=True)
	async def mp(self, ctx):
		emb = discord.Embed(title=f'Праздник вазелина', description='Нажми на реакцию что бы получить роль', colour=discord.Color.purple())

		message = await ctx.send(embed=emb)  # Send embed
		await message.add_reaction('✅') # Add reaction
		roles = discord.utils.get(message.guild.roles, id = 839599224000610344) # Replace it with the role ID
		check = lambda reaction, user: client.user != user # Excludes the bot reaction

		while True:
			reaction, user = await client.wait_for('reaction_add', check=check) # Wait for reaction
			if str(reaction.emoji) == "✅":
				await user.add_roles(roles) # Add role
				print('[SUCCESS] Пользователь {0.display_name} получил новую роль {1.name}'.format(check, roles)) # Print

				await user.send('TEST') # Send message to member



#о сервере
	@commands.command(aliases = ["инфо о серваке"])
	async def server_info(self, ctx):
		await ctx.message.delete()
		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
		emb = discord.Embed (title = 'Информация о сервере :clipboard:', colour=discord.Color.gold(), timestamp=datetime.utcnow())
		emb.set_thumbnail(url=ctx.guild.icon_url)
		emb.add_field(name ='ID cервера', value = ctx.guild.id)
		emb.add_field(name ='Владелец сервера', value = ctx.guild.owner)
		emb.add_field(name ='Регион', value = ctx.guild.region)
		emb.add_field(name ='Людей', value = len(list(filter(lambda m: not m.bot, ctx.guild.members))))
		emb.add_field(name ='Ботов', value = len(list(filter(lambda m: m.bot, ctx.guild.members))))
		emb.add_field(name ='Статусы', value = f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}")
		emb.add_field(name ='Участников', value = len(ctx.guild.members))
		emb.add_field(name ='Текстовых каналов', value = len(ctx.guild.text_channels))
		emb.add_field(name ='Голосовых каналов', value = len(ctx.guild.voice_channels))
		emb.add_field(name ='Категорий', value = len(ctx.guild.categories))
		emb.add_field(name ='Ролей', value = len(ctx.guild.roles))
		emb.set_footer (text ='Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
		await ctx.send (embed = emb, delete_after=30)
		





				

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
		emb = discord.Embed (title = 'Навигация по командам :clipboard:', colour = discord.Color.gold(), timestamp=datetime.utcnow())
		emb.add_field(name ='Описание сервера :pencil:', value = 'Rojers Squad, правила можно прочитать в канале #правила')
		emb.add_field(name ='!clear :broom:', value = 'Очистка чата')
		emb.add_field(name ='!voteban :lock:', value = 'Бан участника')
		emb.add_field(name ='!kick :wave:', value = 'Кик с сервера')
		emb.add_field(name ='!unban :unlock:', value = 'Разбан участника')
		emb.add_field(name ='!tempmute :mute:', value = 'Мут участника')
		emb.add_field(name ='!unmute :speaker:', value = 'Размут участника')
		emb.add_field(name ='!ds :rose:', value = 'Ссылка на наш дс')
		emb.add_field(name ='!slot 🍒', value = 'Игра для развлечения')
		emb.add_field(name ='!server_info :pencil:', value = 'Информация о сервере')
		emb.add_field(name ='!infouser :pencil:', value = 'Узнать информацию о себе')
		emb.add_field(name ='!ticket :microbe:', value = 'Заявка на баг/предложение')
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

		
   #ticket 
	@commands.command(aliases = ["pin1111"])
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def ticket(self, ctx, *, bag):
		channel = self.client.get_channel(820341420132139038)
		myid = '<@375240473184305164>'
		jasonid = '<@514152570156089365>'
		await ctx.message.delete()
		emb = discord.Embed(title = ':pencil: | Заявка на баг/предложение', colour = discord.Color.purple(), timestamp=datetime.utcnow())	
		emb.add_field(name =f':rose: | Ваше Обращение: {bag} отправлено на рассмотрение', value = ':poop: **| Ожидайте ответа**')
		emb.set_footer(text =f'Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
		await ctx.send(embed=emb)
		embed = discord.Embed(title = ':pencil: | Новая заявка на предложение/баг зарегистрирована в системе ', colour = discord.Color.purple(), timestamp=datetime.utcnow())
		embed.add_field(name=f':rose: | Отправитель: {ctx.author.name}', value = f':poop: **| Суть обращения: {bag}**')
		embed.set_footer(text =f'Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
		await channel.send(content=f"{myid},{jasonid}**, Пришла новая заявка, ждёт рассмотрения!**", embed=embed) 


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
		responses = ["``Сидит мужик в роддоме, ждет, когда жена родит. Вроде бы роды закончились, по коридору идет улыбающийся врач, тащит за ногу ребенка. \n Несет и размахивает: то об косяк заденет, то об угол ударит, то по батарее проведет... \n Мужик сидит в шоке. Врач кидает в него ребенком. \n Мужик: — А-а-а блять! \n Врач усмехается — Шутка! Выкидыш``",
		"``—Беня, я гарантирую вам, шо через пять лет мы будем жить лучше, чем в Европе! \n — А шо у них случится?``", 
		"``Ебется курсант с бабой. Тут приходит муж с работы. \n Баба говорит: \n - Давай прыгай с балкона. \n Тот отвечает: \n - С ума сошла? Мы на 9 этаже. \n- Я волшебница, я тебя заколдовала. Дёрнешь хуй и станешь бабочкой и улетишь. \n Ну времени мало, курсант дергает себе хуй и превращается в бабочку. Летит себе, летит. Но тут резко пугается, как же превратиться обратно? Приземляется на лавочку и дергает себя за хуй. Дёрнул - снова стал курсантом. Дёрнул опять - превратился в бабочку. Понравилось ему это, дёргает раз - бабочка, дёргает два - человек. Дёргает,и вдруг слышит голос: \n - Товарищ курсант, мало того что вы дрочите на лекции, так еще и превращаетесь то в бабочку, то в курсанта!``",
		"``Шла девочка с дедушкой вдоль речки. Смотрят, гавно плывет. Ну, а девочка и спрашивает: \n - Откуда оно? \n А дедушка говорит: \n - Было это давно. Жил принц и принцесса. Принц уехал воевать, а принцесса, подумав, что его убьют, утопилась в этой самой речушке. \n Спрашивает вновь девочка: \n - А гавно-то откуда? \n - А я ебу? Насрал кто-то.``",
		"``Решил один мужик завести домашнее животное - жена совсем достала. \n Приходит в зоомагазин и среди прочей живности видит попугая. БЕЗ ЛАПОК. \n Мужик: \n - Надо же! попугай без лапок! \n Попугай: \n - Ну что поделаешь - таким родился... \n Мужик: \n - А ты меня понимаешь, что ли? \n Попугай: \n - Да, я вообще очень умная и образованная птица - могу поддежать \n беседу на любую тему, знаком с науками и т.д. \n Мужик: \n - Скажи, а как ты без лапок на жердочке сидишь? \n Попугай: \n - Ну... членом я хватаюсь, просто под перьями не видно. \n Короче, купил мужик попугая. \n В доме сразу весело стало - попугай всех веселит, истории рассказывает, \n поет... \n Приходит мужик как-то раз с работы домой, а попугай ему и говорит: \n - К твоей жене сосед приходил. \n Мужик: \n - 8-(, и что? \n Попугай: \n - А жена твоя в одной ночнушке его встретила! \n Мужик: \n - 8-((, а потом? \n Попугай: \n - Они начали целоваться. \n Мужик: \n - Убью гада! А потом? \n Попугай: \n - Он стал на колени и полез ТУДА. \n Мужик: \n - А потом? \n Попугай: \n - А потом у меня хуй встал и я с жердочки ебнулся...``",
		"``Встретились украинец с американцем, и зашел у них разговор о горах. \n Американец говорит: \n — У нас такие горы, что как крикнешь, то эхо пять минут длится. \n — Ну так поедем посмотрим, — отвечает украинец. \n Влезают они на вершину, американец кричит: \n — Hello!!! \n Эхо: \n — Hello-ello-llo-o… \n Украинец подождал, когда эхо прекратится, и говорит: \n — Да разве это горы? У нас в горах эхо три часа держится. \n — Ну поехали посмотрим, — отвечает американец. \n Влезают они на самую высокую украинскую гору Говерлу, и украинец как закричит: \n — В Карпатах москаль!!! \n А со всех сторон: \n — Где москаль?.. Где москаль?! Где москаль?! Где москаль?! Где москаль?! Где москаль?!``",
		"``Пришел грузин в автосалон машину покупать. Спрашивает у консультанта: \n – Слушай, я машину пришел покупать. Подскаджи какую! \n – Вот – Форд Фокус \n – А в чем фокус? \n – Садитесь, покажу. \n Едут они. Консультант говорит: \n – Вы видите дерево вон-там? \n – Да! \n – Закройте глаза. \n Грузин глаза закрыл, а консультант обьехал дерево и говорит: \n – Смотрите, мы сквозь дерево проехали! \n – Пакупаю! \n Ну на следующий день едет грузин с друзьями и говорит: \n – Вы видитэ дэрэво там? \n – Дааа!!!! \n – Глаза закройтэ! \n Разьезжается и БАБАХ в дерево! Машина в дребезги, грузин орет: \n – Какой сволоч глаза не закрыл?!``",
		"``Новый украинец едет на BMW. Вдруг прокол. Съезжает к обочине. Надо колесо менять… На домкрат поднял, колесо откручивает. \n Подъезжает хохол на «запорожце»: \n — Чего делаем? \n — Да вот, колесо снимаем. \n Хохол достает монтировку — и хрясь по стеклу: \n — О! Ништяк, тады я магнитолку сниму…``"]
		await ctx.send(f'Вот тебе анекдот: \n{random.choice(responses)}', delete_after=45)
		
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


	@commands.command(aliases = ["slooo"])
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	async def infouser(self, ctx, member:discord.Member = None, guild: discord.Guild = None):

		await ctx.message.delete()
		await ctx.send(f"Команда работает только в канале **🍔┃управление-ботом**", delete_after=10)
		

		if ctx.channel.id == 817402429100392449:
			await ctx.channel.purge(limit = 1)
			if member == None:
				emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color, timestamp=datetime.utcnow())
				emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
				emb.add_field(name="Ник:", value=ctx.message.author.name,inline=False)
				emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
				t = ctx.message.author.status
				if t == discord.Status.online:
					d = "🟢 В сети"

				t = ctx.message.author.status
				if t == discord.Status.offline:
					d = "⚪ Не в сети"

				t = ctx.message.author.status
				if t == discord.Status.idle:
					d = "🟠 Не активен"

				t = ctx.message.author.status
				if t == discord.Status.dnd:
					d = "🔴  Не беспокоить"

				emb.add_field(name="Активность:", value=d,inline=False)
				emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
				emb.add_field(name="Высшая роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
				emb.add_field(name="Роли на сервере:", value= ",".join(m.mention for m in ctx.author.roles),inline=False)
				emb.add_field(name="Аккаунт был создан:", value=ctx.message.author.created_at.strftime("%d.%m.%Y в %H:%M"),inline=False)
				emb.add_field(name ='Присоединился к серверу', value = ctx.message.author.joined_at.strftime("%d.%m.%Y в %H:%M"),inline=False)
				emb.set_thumbnail(url=ctx.message.author.avatar_url)
				emb.set_footer (text ='Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
				await ctx.send(content=f"Информация по аккаунту: {ctx.message.author.mention}" , embed = emb)
			else:
				emb = discord.Embed(title="Информация о пользователе", color=member.color, timestamp=datetime.utcnow())
				emb.add_field(name="Имя:", value=member.display_name,inline=False)
				emb.add_field(name="Ник:", value=member.name,inline=False)
				emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
				t = member.status
				if t == discord.Status.online:
					d = "🟢 В сети"

				t = member.status
				if t == discord.Status.offline:
					d = "⚪ Не в сети"

				t = member.status
				if t == discord.Status.idle:
					d = "🟠 Не активен"

				t = member.status
				if t == discord.Status.dnd:
					d = "🔴  Не беспокоить"
				emb.add_field(name="Активность:", value=d,inline=False)
				emb.add_field(name="Статус:", value=member.activity,inline=False)
				emb.add_field(name="Высшая роль на сервере:", value=f"{member.top_role.mention}",inline=False)
				emb.add_field(name="Роли на сервере:", value=",".join(m.mention for m in member.roles),inline=False)
				emb.add_field(name="Аккаунт был создан:", value=member.created_at.strftime("%d.%m.%Y в %H:%M"),inline=False)
				emb.add_field(name ='Присоединился к серверу', value = member.joined_at.strftime("%d.%m.%Y в %H:%M"),inline=False)
				emb.set_thumbnail(url=member.avatar_url)
				emb.set_footer (text ='Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
				await ctx.send(content=f"Информация по аккаунту: {member.mention}" ,embed = emb)


	@commands.command(aliases = ["onlineee"])
	async def online(self, ctx, *, fraction):
		url = f"https://arizona-rp.com/mon/fraction/8/{fraction}"
		df = pd.read_html(url)[0]
		online = df.loc[df[3] == 'Сейчас играет', 1].to_list()
		emb = discord.Embed (title = 'Онлайн огранизаций на сервере Red-Rock', colour = ctx.message.author.color, timestamp=datetime.utcnow())
		emb.add_field(name=f"Фракция: {fraction}", value=f'В сети: {len(online)}')
		emb.set_footer (text ='Peach Bot Main', icon_url=ctx.bot.user.avatar_url)
		await ctx.send(embed=emb)



    
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



	@clear.error
	async def clear_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !clear [от 1 до 100]', colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
	@kick.error
	async def kick_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !kick {0.author.mention} [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@tempmute.error
	async def tempmute_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !tempmute {0.author.mention} [время] [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@unmute.error
	async def unmute_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format (ctx.author.name), description='Пример: !unmute {0.author.mention}'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format (ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)

	@unban.error
	async def unban_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format(ctx.author.name),description='Пример: !unban namesloga13', colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format(ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)


	@voteban.error
	async def voteban_error(self, ctx,error):
		if isinstance (error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} Обязательно укажите аргумент!'.format(ctx.author.name),description='Пример: !voteban {0.author.mention} [причина]'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)
		if isinstance(error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = discord.Embed(title=':x: {} у вас нет прав модератора'.format(ctx.author.name), description='{0.author.mention} Обратитесь к модераторам'.format(ctx.message), colour = discord.Color.gold(), timestamp=datetime.utcnow())
			await ctx.send(content=ctx.author.mention, embed=embed, delete_after=30)



def setup(client):
	client.add_cog(User(client))

