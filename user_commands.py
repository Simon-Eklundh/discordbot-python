import disnake.ext.commands
import database

from disnake.ext import commands
from Links import Link



class User(disnake.ext.commands.Cog,disnake.BotIntegration):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def help(self,inter: disnake.CommandInteraction):
        user = inter.user
        guild = self.bot.get_guild(inter.guild_id)
        channel_id = database.get_help_channel(user.id, guild.id)

        if channel_id == -1:
            category_id = database.get_help_category(guild.id)
            if category_id == -1:
                return "no helpcategory has been set, please tell admin to set one"
            category = guild.get_channel(category_id)
            the_channel = await category.create_text_channel(user.name + "-helpchannel")
            database.set_help_channel(user.id, guild.id, the_channel.id)
            channel_id = the_channel.id
        channel = guild.get_channel(channel_id)
        await inter.response.send_message("please go to " + channel.mention + " to get help :joy:")

    @commands.slash_command()
    async def thanks(self, inter: disnake.CommandInteraction):
        user = inter.user
        guild = self.bot.get_guild(inter.guild_id)
        channel_id = database.get_help_channel(user.id, guild.id)
        if channel_id == -1:
            await inter.response.send_message("We found no channel for you, glad you're happy however! :joy:")
            return
        channel = guild.get_channel(channel_id)
        await channel.delete()
        database.delete_help_channel(user.id, guild.id)
        await inter.response.send_message(channel.name + " has been removed, glad we could help!")

    # these links are for the link slash command

    @commands.slash_command()
    async def link(self,inter: disnake.ApplicationCommandInteraction, link_name: Link):
        await inter.response.send_message(link_name)
