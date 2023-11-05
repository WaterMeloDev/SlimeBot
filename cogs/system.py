import discord
import random
from discord.ext import commands

class WelcomeGoodbye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = member.guild.get_channel(1163125858622509148)

        if welcome_channel:
            welcome_messages = [
                f"Goop-goop! {member.name} Welcome! I hope you have a wonderful slime!",
                f"Goop-goop! {member.name} Welcome! I can't speak for these other slimes but you can always hop on my fields.",
                f"Goop-goop! {member.name} Welcome! I hope your hoppy here.. I mean happy here.",
                f"Goop-goop! {member.name} Welcome! You new here? I'd remember a gel like yours hopping around."
            ]
            welcome_message = random.choice(welcome_messages)
            await welcome_channel.send(welcome_message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        goodbye_channel = member.guild.get_channel(1163125858622509148)

        if goodbye_channel:
            goodbye_messages = [
                f"Gooey! {member.name} just hopped away. See you later slime-o-gator!",
                f"Gooey! {member.name} just hopped away, see you next slime!",
                f"Gooey! {member.name} just hopped away. Hope you at least had a good slime.",
                f"Gooey! {member.name} just hopped away. A wise slime once slimed me.. wait what am I saying?"
            ]
            goodbye_message = random.choice(goodbye_messages)
            await goodbye_channel.send(goodbye_message)

async def setup(bot):
    await bot.add_cog(WelcomeGoodbye(bot))