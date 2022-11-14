import os
from enum import Enum

import disnake
from disnake import ChannelType
from disnake.ext import commands

import database

import slash_commands
from Links import Link

bot = commands.InteractionBot(test_guilds=[962642268248997908], )


@bot.slash_command()
@commands.default_member_permissions(manage_guild=True, moderate_members=True)
async def admin(_inter):
    pass


@admin.sub_command()
async def set_help_category(inter: disnake.CommandInteraction,
                           channel: disnake.abc.GuildChannel = commands.Param(channel_types=[ChannelType.category])):
    result: bool = slash_commands.set_help_channel(channel)
    if result:
        await inter.response.send_message(channel.name + " is set as your new help-channel")
    else:
        await inter.response.send_message("something went wrong, please try again or open an issue at the bot github https://github.com/Simon-Eklundh/discordbot-python")


@bot.slash_command()
async def help(inter: disnake.CommandInteraction):
    result: disnake.TextChannel = await slash_commands.help(inter.user, bot.get_guild(inter.guild_id))
    await inter.response.send_message("please go to "+result.mention + " to get help :joy:")


@bot.slash_command()
async def thanks(inter: disnake.CommandInteraction):
    result: str = await slash_commands.thanks(inter.user, bot.get_guild(inter.guild_id))
    await inter.response.send_message(result)


# these links are for the link slash command

@bot.slash_command()
async def link(inter: disnake.ApplicationCommandInteraction, link_name: Link):
    await inter.response.send_message(link_name)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


if __name__ == "__main__":
    database.prepare()
    bot.run("ODU2MTczNTUxMTkxMDY0NTk3.GST-RV.bsiZmJgs6yQPT-ZqxCpGFYBf7-oH5DxbVl9L_c")
