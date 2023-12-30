import discord
from discord.ext import commands

class ShowHelp:
    async def show_help(self,ctx,function_config):
        response = ""
        for key,item in function_config.items():
            if (item["use"]):
                for func,conf in  item["commands"].items():
                    if(conf["use"]):
                        response += "- コマンド: {}\n  - 説明: {}\n".format(func,conf["discription"])
        await ctx.send(response)
