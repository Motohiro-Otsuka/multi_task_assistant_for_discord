import datetime 
import discord
from discord.ext import commands
import os
import openai
import json


class ChatOpenai:

    def __init__(self,config):
        self.config = config
        #openai_conf_obj = open("./config/openai_conf.json","r")
        #openai_config = json.load(openai_conf_obj)
        openai.api_key = config["OPENAI_API_KEY"]
        self.log_num = config["max_log"]
        self.message_dic = {}
        """
        messages = [
            {"role": "system", "content": "あなたは親切なアシスタントです。"},
            {"role": "user", "content": "春の季語を絡めた冗談を教えてください。"},
            {"role": "assistant", "content": "「春眠（しゅんみん）暁（ぎょう）を覚（さ）えず」という言葉がありますが、「春は眠くても、アシスタントは覚えてるよ！」と言って、ツッコミを入れるのはいかがでしょうか？笑"},
            {"role": "user", "content": "面白くない。もう一度。"},
        ]
        """

    def add_assistant_chat_log(self,thread_id,text):
        """
        chatログを追加するための関数
        """
        self.message_dic[thread_id]["prompt"].append({"role": "assistant", "content": text})

    def check_chatgpt_thread(self,thread_id):
        """
        すでにchatのスレッドが立っているか確認するための
        """
        if (thread_id in self.message_dic):
            return True
        else:
            return False

    async def make_prompt(self,thread_id,text):
        """
        chat-gptに問い合わせるためのpromptを作る関数
        """
        #threadに１投稿目の時
        prompt = None
        if (thread_id not in self.message_dic):
            prompt = [
                {"role": "system", "content": self.config["system_prompt"]},
                {"role": "user", "content": text},
            ]
            self.message_dic[thread_id] = {}
            self.message_dic[thread_id]["prompt"] = prompt
            date = datetime.datetime.now()
            self.message_dic[thread_id]["start_time"] = date.strftime('%Y-%m-%d')
        else:
            self.message_dic[thread_id]["prompt"].append({"role": "user", "content": text})
        #上限を超えたときの処理を入れる
        while(len(self.message_dic[thread_id]) >= int(self.log_num) + 1):
            del self.message_dic[thread_id]["prompt"][1]
        return self.message_dic[thread_id]["prompt"]

    async def call_openai(self,messages):
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

    async def response_chatgpt(self,thread,text):
        """
        discordにchat-gptのレスポンスを返すための関数
        """
        prompt = await self.make_prompt(thread.id,text)
        response = await self.call_openai(prompt)
        #ログを追加
        self.add_assistant_chat_log(thread.id,response)
        await thread.send(response)

    async def new_chat(self,ctx,text):
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
        #await thread.send("/chat\n入力："+text+"\n解答作成中です\n")
        await self.response_chatgpt(thread,text)