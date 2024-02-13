import datetime
from zoneinfo import ZoneInfo
import discord
from discord.ext import commands
import os
import openai
import json
from threading import Thread
import time
import pytz


class ChatOpenai:
    def __init__(self, config):
        self.config = config
        # openai_conf_obj = open("./config/openai_conf.json","r")
        # openai_config = json.load(openai_conf_obj)
        openai.api_key = config["OPENAI_API_KEY"]
        self.log_num = config["max_log"]
        self.message_dic = {}

    def delete_chat_log(self):
        for thread_id in list(self.message_dic.keys()):
            create_time = datetime.datetime.strptime(
                self.message_dic[thread_id]["start_time"], "%Y-%m-%d %H:%M"
            ).replace(tzinfo=pytz.timezone("Asia/Tokyo"))
            now_time = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
            delta = now_time - create_time
            if delta.days >= 1:
                del self.message_dic[thread_id]

    def add_assistant_chat_log(self, thread_id, text):
        """
        chatログを追加するための関数
        """
        self.message_dic[thread_id]["prompt"].append(
            {"role": "assistant", "content": text}
        )

    def check_chatgpt_thread(self, thread_id):
        """
        すでにchatのスレッドが立っているか確認するための
        """
        if thread_id in self.message_dic:
            return True
        else:
            return False

    async def make_prompt(self, thread_id, text):
        """
        chat-gptに問い合わせるためのpromptを作る関数
        """
        # threadに１投稿目の時
        self.message_dic[thread_id]["prompt"].append(
            {"role": "user", "content": text}
        )
        # 上限を超えたときの処理を入れる
        while len(self.message_dic[thread_id]) >= int(self.log_num) + 1:
            del self.message_dic[thread_id]["prompt"][1]
        return self.message_dic[thread_id]["prompt"]

    async def call_openai(self, messages):
        """
        chat gptに問い合わせるための関数
        """
        # APIリクエストの設定
        response = openai.ChatCompletion.create(
            model=self.config["model"],  # GPTのエンジン名を指定します
            messages=messages,
            max_tokens=int(self.config["max_tokens"]),  # 生成するトークンの最大数
            n=1,  # 生成するレスポンスの数
            stop=None,  # 停止トークンの設定
            temperature=float(self.config["temperature"]),  # 生成時のランダム性の制御
            top_p=1,  # トークン選択時の確率閾値
        )
        return response.choices[0].message.content.strip()

    async def response_chatgpt(self, thread, text):
        """
        discordにchat-gptのレスポンスを返すための関数
        """
        prompt = await self.make_prompt(thread.id, text)
        response = await self.call_openai(prompt)
        # ログを追加
        self.add_assistant_chat_log(thread.id, response)
        await thread.send(response)

    async def new_chat(self, ctx):
        """
        /chatコマンドが呼ばれた時の処理。新たにスレッドを立てsystemプロンプトを返す
        """
        channel = ctx.channel  # メッセージがあったチャンネルの取得
        # スレッド名の定義
        date = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
        date_str = date.strftime("%Y-%m-%d %H:%M")
        thread_name = "{}".format(date_str)
        # スレッドの作成
        thread = await channel.create_thread(
            name=thread_name,
            reason="make chat",
            type=discord.ChannelType.public_thread,
            auto_archive_duration=60,
        )  # スレッドを作る
        # メッセージを送信してスレッドを開始します。
        prompt = [
                {"role": "system", "content": self.config["system_prompt"]},
            ]
        self.message_dic[thread.id] = {}
        self.message_dic[thread.id]["prompt"] = prompt
        date = datetime.datetime.now()
        self.message_dic[thread.id]["start_time"] = date.strftime("%Y-%m-%d %H:%M")
        await thread.send("現在のGPTの役割を示す文章：{}\nこのスレッドで会話を続けてください".format(self.config["system_prompt"]))
        #await self.response_chatgpt(thread, text)
