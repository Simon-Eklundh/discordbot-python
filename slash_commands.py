import disnake
import database


def set_help_channel(channel: disnake.abc.GuildChannel):
    database.set_help_category(channel.guild.id, channel.id)
    return "set helpchannel: " + channel.name + " for server: " + channel.guild.name


async def help(user: disnake.User, guild: disnake.Guild):
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
    return channel


async def thanks(user: disnake.User, guild: disnake.Guild):
    channel_id = database.get_help_channel(user.id, guild.id)
    if channel_id == -1:
        return "We found no channel for you, glad you're happy however! :joy:"
    channel = guild.get_channel(channel_id)
    await channel.delete()
    database.delete_help_channel(user.id, guild.id)
    return channel.name + " has been removed, glad we could help!"
