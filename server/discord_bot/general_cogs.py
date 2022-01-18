"""General cogs for use in bot.py"""
import json
from discord import Message
from discord.ext.commands import Cog, Bot


class General_Cog(Cog):
    def __init__(self, bot: Bot):
        with open("discord_bot/vars.json", "r") as f:
            self.channels = json.load(f)["CHANNELS"]
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"Bot running with id: {self.bot.user.id}")

    @Cog.listener()
    async def on_message(self, msg: Message):
        with open("discord_bot/messages.json", "r") as f:
            messages = json.load(f)
        
        for user, channels in self.channels.items():
            if str(msg.channel.id) in channels:
                if user in messages:
                    messages[user].append(msg.content)
                else:
                    messages[user] = [msg.content]
        
        with open("discord_bot/messages.json", "w") as f:
            json.dump(messages, f)


def setup(bot: Bot):
    bot.add_cog(General_Cog(bot))
