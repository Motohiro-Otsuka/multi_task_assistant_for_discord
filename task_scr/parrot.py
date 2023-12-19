import datetime 
import discord
from discord.ext import commands
async def parrot(ctx,text):
	channel = ctx.channel #メッセージがあったチャンネルの取得
    #スレッド名の定義
	date = datetime.datetime.now()
	date_str = date.strftime('%Y-%m-%d')
	thread_name = '{}'.format(date_str)
	#スレッドの作成
	thread = await channel.create_thread(name=thread_name,reason="クリップ録画API",type=discord.ChannelType.public_thread)#スレッドを作る
	#録画用のために作ったスレッド以外は許容しない
	#allow_recoed_thread_id.append(thread.id)
	#移動先のディレクトリ名はスレッドidで管理する
	#after_move_dirs[thread.id] = {}

	# メッセージを送信してスレッドを開始します。
	await thread.send(text)