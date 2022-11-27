import os

from disnake.ext import commands

import admin_commands
import database
import user_commands

bot = commands.InteractionBot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


def start():
    database.prepare()
    token: str = os.environ.get("BOT_TOKEN")
    bot.add_cog(admin_commands.Admin(bot))
    bot.add_cog(user_commands.User(bot))
    bot.run(token)


if __name__ == "__main__":
    start()
