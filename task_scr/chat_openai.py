import datetime 
import discord
from discord.ext import commands

import os
import openai
import json

openai_conf_obj = open("./config/openai_conf.json","r")
openai_config = json.load(openai_conf_obj)

openai.api_key = openai_config["OPENAI_API_KEY"]
log_num = 5

message_dic = {}
"""
messages = [
    {"role": "system", "content": "あなたは親切なアシスタントです。"},
    {"role": "user", "content": "春の季語を絡めた冗談を教えてください。"},
    {"role": "assistant", "content": "「春眠（しゅんみん）暁（ぎょう）を覚（さ）えず」という言葉がありますが、「春は眠くても、アシスタントは覚えてるよ！」と言って、ツッコミを入れるのはいかがでしょうか？笑"},
    {"role": "user", "content": "面白くない。もう一度。"},
]
"""

def add_assistant_chat_log(thread_id,text):
    """
    chatログを追加するための関数
    """
    message_dic[thread_id]["prompt"].append({"role": "assistant", "content": text})

def check_chatgpt_thread(thread_id):
    """
    すでにchatのスレッドが立っているか確認するための
    """
    if (thread_id in message_dic):
        return True
    else:
        return False

async def make_prompt(thread_id,text):
    """
    chat-gptに問い合わせるためのpromptを作る関数
    """
    #threadに１投稿目の時
    prompt = None
    if (thread_id not in message_dic):
        prompt = [
            {"role": "system", "content": "あなたは親切なアシスタントです。"},
            {"role": "user", "content": text},
        ]
        message_dic[thread_id] = {}
        message_dic[thread_id]["prompt"] = prompt
        date = datetime.datetime.now()
        message_dic[thread_id]["start_time"] = date.strftime('%Y-%m-%d')
    else:
        message_dic[thread_id]["prompt"].append({"role": "user", "content": text})
    #上限を超えたときの処理を入れる
    while(len(message_dic[thread_id]) >= log_num + 1):
        del message_dic[thread_id]["prompt"][1]
    return message_dic[thread_id]["prompt"]

async def call_openai(messages):
    """
    chat gptに問い合わせるための関数
    """
    # APIリクエストの設定
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",  # GPTのエンジン名を指定します
        messages=messages,
        max_tokens=500,  # 生成するトークンの最大数
        n=1,  # 生成するレスポンスの数
        stop=None,  # 停止トークンの設定
        temperature=0.7,  # 生成時のランダム性の制御
        top_p=1,  # トークン選択時の確率閾値
    )
    return response.choices[0].message.content.strip()

async def response_chatgpt(thread,text):
    """
    discordにchat-gptのレスポンスを返すための関数
    """
    prompt = await make_prompt(thread.id,text)
    response = await call_openai(prompt)
    #ログを追加
    add_assistant_chat_log(thread.id,response)
    await thread.send(response)

async def new_chat(ctx,text):
    """
    /chatコマンドが呼ばれた時の処理。新たにスレッドを立てて、chat-gptのレスポンスを返す関数
    """
    channel = ctx.channel #メッセージがあったチャンネルの取得
    #スレッド名の定義
    date = datetime.datetime.now()
    date_str = date.strftime('%Y-%m-%d')
    thread_name = '{}'.format(date_str)
    #スレッドの作成
    thread = await channel.create_thread(name=thread_name,reason="make chat",type=discord.ChannelType.public_thread)#スレッドを作る
    # メッセージを送信してスレッドを開始します。
    await thread.send("/chat\n入力："+text)
    await response_chatgpt(thread,text)