import discord
from discord.ext import commands
import json
import shutil
from task_scr import parrot,chat_openai,live_scheduler

#configの読み込み
config_file = open("./config/config.json","r",encoding="utf-8")
config = json.load(config_file)
common_config= config["common"]
function_config = config["function"]

## 各機能ごとのconfig取り出し
parrot_cls = parrot.Parrot(function_config["parrot"]) if function_config["parrot"]["use"] == True else None
chat_openai_cls = chat_openai.ChatOpenai(function_config["chat_openai"]) if function_config["chat_openai"]["use"] == True else None
live_scheduler_cls = live_scheduler.LiveScheduer(function_config["live_scheduler"],common_config["google_dirive_setting"]) if function_config["live_scheduler"]["use"] == True else None

##必用な設定値を読み出し
discord_api_key = common_config["discord_api_key"]

#replitを使用する場合に必要なライブラリを読み込み
if(common_config["use_replit"]):
	from server import keep_alive# ToDo ない場合は読み込まない

#discordbotの設定
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True  # メッセージに関するデバッグ情報を有効化
client = commands.Bot(command_prefix="/", intents=intents)

#bot用スクリプト
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
			if(chat_openai.check_chatgpt_thread(message.channel.id) and chat_openai_cls != None):
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
	if(parrot_cls != None):
		await parrot_cls.parrot(ctx,text)
	else:
		await ctx.send("この機能は使用できません。")

#chat GPTによるチャット
@client.command("chat")
async def wrapper_chat_openai(ctx,text):
	try:
		if(chat_openai_cls!=None):
			await chat_openai_cls.new_chat(ctx,text)
		else:
			await ctx.send("この機能は使用できません。")
	except Exception as e:
		await ctx.send("Errorが発生しました。次のメッセージをbot管理者にお伝えください。\n {}".format(str(e)))

#スケジュール画像の表示
@client.command("schedule-print")
async def wrapper_chat_openai(ctx):
	try:
		if(live_scheduler_cls!=None):
			await ctx.send("スケジュール画像の生成を受け付けました。\n生成までしばらくお待ちください。")
			await live_scheduler_cls.print_schedule(ctx)
			shutil.rmtree(live_scheduler_cls.tmp_dir_path)
		else:
			await ctx.send("この機能は使用できません。")
	except Exception as e:
		await ctx.send("Errorが発生しました。次のメッセージをbot管理者にお伝えください。\n {}".format(str(e)))


# ウェブサーバーを起動する
# ToDo ない場合は読み込まない
if(common_config["use_replit"]):
	keep_alive()

client.run(discord_api_key)
