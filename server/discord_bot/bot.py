"""Main bot run file"""
import json
import discord
from typing import List, Dict
from discord.ext import commands

with open("discord_bot/vars.json", "r") as f:
    vars_ = json.load(f)

app_id: str = vars_["APP-ID"]
token: str = vars_["TOKEN"]
raw_channels: Dict[str, List[int]] = vars_["CHANNELS"]
channels = []
for _, c in raw_channels.items():
    channels.extend(c)

bot = commands.Bot(command_prefix="!c ", activity=discord.Game("!c help"))
bot.load_extension("general_cogs")
bot.run(token)
