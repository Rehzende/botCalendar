from discord.ext import tasks, commands
from utils import config as cfg
from utils.google_calendar import list_events
from datetime import date, datetime
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


async def notify(channel):

    eventos = list_events.getEvents()
    data = date.today().strftime("%d %b %Y")

    if not eventos:
        embed = discord.Embed(
            title="📚 Agenda de Estudos :loudspeaker: ", description=data)
        embed.add_field(name=f"**:cold_sweat: Sem Agenda**",
                        value=f"Use ```>criar_agenda```  e agende um estudo, bora aprender!! ", inline=False)
        embed.set_footer(
            text="Se você está afim de aprender algo, agende um momento de estudo, para que os demais possam saber do seu interesse.")
        await channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title="📚 Agenda de Estudos :loudspeaker: ", description=data)
        for event in eventos:
            embed.add_field(
                name=f"**:white_check_mark: {event['summary']}**", value=f" Local:  {event['location']} ", inline=False)
            embed.set_footer(
                text="Agenda: ✅ - Ativa - 🟥 - Cancelada(provavelmente já passou do horário)")
        await channel.send(embed=embed)


class Monitor(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.calendar_cron.start()

    def cog_unload(self):
        self.calendar_cron.cancel()

    @tasks.loop(minutes=60.0)
    async def calendar_cron(self):
        if datetime.now().hour == 9:
            await self.bot.wait_until_ready()
            channel = self.bot.get_channel(
                cfg.config[0]['notification_channel'])
            await notify(channel)


def setup(bot):
    bot.add_cog(Monitor(bot))
