import schedule
import time
import asyncio
import discord
from discord.ext import commands
import re
from datetime import datetime, timedelta



class AutoPostArrangeSchedule:
    def __init__(self, settings):
        #self.send_message = config["post_content"]
        #self.send_day = config["post_day"]
        #self.send_time = config["post_time"]
        self.settings = settings
        self.day_map = {"日": 6, "月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5}

    async def scheduled_message(self, ctx,config):
        send_message = config["post_content"]
        send_day = config["post_day"]
        send_time = config["post_time"]
        # 現在の曜日を取得
        matches = re.findall(r'\{day\+(\d+)\}', send_message)
        now = datetime.now()
        # 置換用の辞書を作成
        replacements = {}
        # 各マッチに対して処理
        for match in matches:
            n = int(match)  # 抽出した n を整数に変換
            future_date = now + timedelta(days=n)
            formatted_date = future_date.strftime("%d日 ")
            replacements[f"{match}"] = formatted_date
        # 元の文字列を置換
        output_string = send_message
        for match in matches:
            output_string = output_string.replace("{day+"+str(match)+"}",replacements[match])
        current_time = time.localtime()
        if current_time.tm_wday == self.day_map[send_day]:  # 木曜日はtm_wdayが3
            now = datetime.now()
            now_time_str = now.strftime("%H:%M")
            if(now_time_str==send_time):
                await ctx.send(output_string)