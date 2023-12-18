import discord
from discord.ext import commands
import json
import os
import flet as ft

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
intents.message_content = True  # メッセージに関するデバッグ情報を有効化
client = commands.Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):#メッセージをなにかしら受け取ったときの処理
    if type(message.channel) is discord.Thread:#スレッドでメッセージを受け取った時
        if message.author == client.user or message.author.bot:#メッセージの送り主がbotの時は処理しない
            pass
        elif message.channel.id not in allow_recoed_thread_id:#録画を許可しないスレッドは処理しない
            pass
        else:#ここに保存コマンドを書く
            pass
    #それ以外はコマンド実行
    await message.channel.send('メッセージを受信しました。')


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!")
    page.add(t)
    client.run(os.environ["discord_api_key"])

ft.app(target=main)
