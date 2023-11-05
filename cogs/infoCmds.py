import discord
from discord.ext import commands
from discord import app_commands
from colorama import Fore

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{Fore.GREEN}[ OK ]{Fore.RESET} loaded infoCmds.py")

    
    # help command
    # For the modhelp_cmd function
    @app_commands.command(name="modhelp", description="Show a list of mod commands.")
    async def modhelp_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Mod Discord Bot Commands",
            description="Here are some useful commands for moderators:",
            color=0x27ae60,
        )

        commands = [
            ("📜 /modhelp", "Show this list of commands."),
            ("🚫 /ban", "Ban a member."),
            ("👢 /kick", "Kick a member."),
            ("⚠️ /warn", "Warn a member."),
            ("❌ /delwarn", "Delete a warning."),
            ("🚨 /warnings", "Show the warning list."),
            ("🔒 /cwarn", "Clear all warns for a member."),
            ("⏰ /timeout", "Timeout a member."),
            ("☢️ /nuke", "Nuke the selected channel."),
            ("⚖️ /unban", "Unban a member."),
            ("⏲️ /tempban", "Temporarily ban a member.")
        ]

        for name, value in commands:
            embed.add_field(name=name, value=value, inline=True)

        embed.set_footer(
            text="Melo - 'Too lazy to be detailed'",
            icon_url="https://cdn.discordapp.com/attachments/1169829968402989147/1170548603434049626/discord-avatar-512-FAD21.png?ex=65597156&is=6546fc56&hm=14f70c3f63e990e412daf52745baa3c0b3abd1713f3b3ad69c77774720f718ea&"
        )

        # Send the embed as a response
        await interaction.response.send_message(embed=embed)


    # For the help_cmd function
    @app_commands.command(name="help", description="Show a list of user commands")
    async def help_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="User Discord Bot Commands",
            description="Here are some commands tailored for users:",
            color=0xff5733,
        )

        commands = [
            ("📜 /help", "Show this list of commands."),
            ("💘 /ship", "/ship [member1] [member2]"),
            ("👨‍💻 /dev", "Learn about the developer."),
            ("🔍 /whois", "OSINT information."),
            ("🖥️ /server", "OSINT Server info."),
            ("🎱 /8ball", "Ask the magic 8-ball a question.")
        ]

        for name, value in commands:
            embed.add_field(name=name, value=value, inline=True)

        # Send the embed as a response
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="dev", description="A passionate Discord bot developer")
    async def developer(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="WaterMeloDev's Bot",
            description="A passionate Discord bot developed by WaterMeloDev",
            color=0x00ff00 
        )
        
        embed.add_field(name="Currently working on", value="[TheHive](https://github.com/WaterMeloDev/TheHive)", inline=False)
        embed.add_field(name="Ask me about", value="Python, C#, JavaScript", inline=False)
        embed.add_field(name="Contact", value="Email: watermelodev@gmail.com", inline=False)
        
        embed.add_field(name="Connect with me on Twitter", value="[@WaterMeloDev](https://twitter.com/watermelodev)", inline=False)
        
        languages_and_tools = [
            "Bash", "C#", "CSS3", "Django", "Flask", "HTML5", "JavaScript",
            "Linux", "MySQL", "Node.js", "Python", "Webpack"
        ]
        embed.add_field(name="Languages and Tools", value=", ".join(languages_and_tools), inline=False)
        
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1157488352598179880/1157488404540424241/TheHive.png?ex=6518ca94&is=65177914&hm=4cf33da5ee020ffc2586421a6648e15df4aa68cc0963861ce9583a5cafc6c5f0&")
        
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))