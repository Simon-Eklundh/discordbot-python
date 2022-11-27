import disnake.ext.commands
from disnake import ChannelType
from disnake.ext import commands

import database



class Admin(disnake.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        pass

    @commands.slash_command()
    @commands.default_member_permissions(manage_guild=True, moderate_members=True)
    async def admin(self, _inter):
        pass

    @admin.sub_command()
    async def set_help_category(self, inter: disnake.CommandInteraction,
                                channel: disnake.abc.GuildChannel = commands.Param(
                                    channel_types=[ChannelType.category])):
        database.set_help_category(channel.guild.id, channel.id)

        await inter.response.send_message(channel.name + " is set as your new help-channel")
