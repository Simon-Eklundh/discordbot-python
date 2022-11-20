

import mysql.connector

mydb = mysql.connector.connect(
  host="mysql",
  user="discordbot",
  password="discordbotpw",
  database="discordbot"
)
cursor = mydb.cursor()



def prepare():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS helpchannels (person BIGINT NOT NULL PRIMARY KEY, server BIGINT NOT NULL, channel BIGINT NOT NULL)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS helpcategories (server BIGINT NOT NULL PRIMARY KEY, category BIGINT NOT NULL)")
    mydb.commit()



def set_help_category(guild_id, category_id):
    remove_category = f"DELETE FROM helpcategories " \
                      f"Where server={guild_id}"
    execute_statement(remove_category)
    add_category = f"INSERT INTO helpcategories (server,category) VALUES ({guild_id},{category_id})"
    execute_statement(add_category)


def get_help_channel(user_id, guild_id):
    help_statement = f"SELECT channel FROM helpchannels WHERE person={user_id} AND server={guild_id}"
    channel = execute_statement_with_fetch(help_statement)
    if channel is None:
        return -1
    else:
        return channel[0]


# Executes the statement and returns the result if applicable
def execute_statement(help_statement):
    global cursor
    cursor.execute(help_statement)
    mydb.commit()

def execute_statement_with_fetch(help_statement):
    global cursor
    cursor.execute(help_statement)
    channel = cursor.fetchone()
    mydb.commit()
    return channel


def get_help_category(guild_id):
    category_statement = f"SELECT category FROM helpcategories WHERE server={guild_id}"
    output: str = execute_statement_with_fetch(category_statement)
    if output == None:
        return -1
    else:
        return output[0]


def set_help_channel(user_id, guild_id, channel_id):
    set_help_channel_statement = f"INSERT INTO helpchannels (person, server, channel) VALUES ({user_id},{guild_id},{channel_id})"
    execute_statement(set_help_channel_statement)


def delete_help_channel(user_id, guild_id):
    channel_delete_statement = f"DELETE FROM helpchannels WHERE person={user_id} and server={guild_id}"
    execute_statement(channel_delete_statement)
