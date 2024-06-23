import schedule
import time
import asyncio
import discord
from discord.ext import commands


class AutoPostArrangeSchedule:
    def __init__(self, config):
        self.send_message = config["post_content"]
        self.send_day = config["post_day"]
        self.send_time = config["post_time"]
        self.send_channel = config["channel_id"]
        self.day_map = {"日": 6, "月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5}

    async def scheduled_message(self, ctx):
        # 現在の曜日を取得
        current_time = time.localtime()
        if current_time.tm_wday == self.day_map[self.send_day]:  # 木曜日はtm_wdayが3
            await ctx.send(self.send_message)
        else:
            await ctx.send(self.send_message + "※テスト")
