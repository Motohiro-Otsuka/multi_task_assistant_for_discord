import discord
from discord.ext import commands
import json
from task_scr import parrot,chat_openai

conf_file = open("./config/assistant_function_conf.json","r")
allow_function = json.load(conf_file)
if(allow_function["use_replit"]):
	from server import keep_alive# ToDo ない場合は読み込まない

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True  # メッセージに関するデバッグ情報を有効化
client = commands.Bot(command_prefix="/", intents=intents)

conf_file = open("./config/discord_conf.json","r")
config = json.load(conf_file)
discord_api_key = config["flare_assistant"]["discord_api_key"]

@client.event
async def on_ready():
	print('ログインしました')


@client.event
async def on_message(message):  #メッセージをなにかしら受け取ったときの処理
	if type(message.channel) is discord.Thread:  #スレッドでメッセージを受け取った時
		if message.author == client.user or message.author.bot:  #メッセージの送り主がbotの時は処理しない
			pass
		elif False:#message.channel.id not in allow_recoed_thread_id:  #録画を許可しないスレッドは処理しない
			pass
		else:  #ここに保存コマンドを書く
			#chatgptへの問い合わせ場合
			if(chat_openai.check_chatgpt_thread(message.channel.id) and allow_function["chat"]):
				await chat_openai.response_chatgpt(message.channel,message.content)

	#それ以外はコマンド実行
	if message.author == client.user or message.author.bot:
		pass
	else:
		pass
		#await message.channel.send('メッセージを受信しました。')
	await client.process_commands(message)


#オウム返し
@client.command("parrot")
async def wrapper_parrot(ctx,text):
	if(allow_function["parrot"]):
		await parrot.parrot(ctx,text)
	else:
		await ctx.send("この機能は使用できません。")

@client.command("chat")
async def wrapper_parrot(ctx,text):
	try:
		if(allow_function["chat"]):
			await chat_openai.new_chat(ctx,text)
		else:
			await ctx.send("この機能は使用できません。")
	except Exception as e:
		await ctx.send("Errorが発生しました。次のメッセージをbot管理者にお伝えください。\n {}".format(str(e)))

# ウェブサーバーを起動する
# ToDo ない場合は読み込まない
if(allow_function["use_replit"]):
	keep_alive()

client.run(discord_api_key)
