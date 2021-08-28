#!/usr/bin/env python3
import discord
import threading
from project_variables import DISCORD_BOT_TOKEN, DISCORD_USER_ID, ALERT_MESSAGE

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
notified_user = None


@client.event
async def on_ready():
    global notified_user
    notified_user = client.get_user(int(DISCORD_USER_ID))
    await notified_user.send('Online!')


async def send_alert() -> None:
    await notified_user.send(ALERT_MESSAGE)


run_thread = threading.Thread(target=client.run, args=(DISCORD_BOT_TOKEN,))
run_thread.start()
