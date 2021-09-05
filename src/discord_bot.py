#!/usr/bin/env python3
import discord
import threading


class DiscordNotifierClient(discord.Client):
    def __init__(self, discord_intents: discord.Intents, discord_user_id: int):
        super().__init__(intents=discord_intents)
        self.discord_user_id = discord_user_id
        self.notified_user = None

    async def on_ready(self):
        self.notified_user = self.get_user(self.discord_user_id)
        await self.notified_user.send('Online!')

    async def send_alert(self, alert_message: str) -> None:
        await self.notified_user.send(alert_message)


class DiscordNotifierBot(discord.Client):
    def __init__(self, discord_user_id: int):
        super().__init__()
        intents = discord.Intents.default()
        intents.members = True
        self.client = DiscordNotifierClient(discord_intents=intents, discord_user_id=discord_user_id)
        self.notified_user = self


def start_bot(bot_token: str, user_id: int):
    bot = DiscordNotifierBot(user_id)
    run_thread = threading.Thread(target=bot.client.run, args=(bot_token,))
    run_thread.start()
    return bot
