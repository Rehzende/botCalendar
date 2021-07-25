from discord.ext import commands
import discord, datetime
from dateutil.parser import parse
from datetime import date
from utils.google_calendar import list_events
import logging


DIAS = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-Feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]


class Calendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Retorna os agendamento de estudo do dia atual")
    async def agenda2(self, ctx):
        """
        usage: >agenda

        """

        dt = datetime.datetime.now()
        week_number = dt.isocalendar()[1]
        firstdayofweek = datetime.datetime.strptime(
            f"{dt.year}-W{int(week_number)}-1", "%Y-W%W-%w"
        ).date()
        lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)

        eventos = list_events.getEvents()

        data = date.today().strftime("%d %b %Y")
        indice_da_semana = date.today().weekday()
        dia_da_semana = DIAS[indice_da_semana]
        if not eventos:

            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker: ",
                description=f"Data: {data} - {dia_da_semana}",
            )
            embed.add_field(
                name=f"**:cold_sweat: Sem Agenda**",
                value=f"Use ```>criar_agenda```  e agende um estudo, bora aprender!! ",
                inline=False,
            )
            embed.set_footer(
                text="Se você está afim de aprender algo, agende um momento de estudo, para que os demais possam saber do seu interesse."
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker:", description=f"Data: {data} - {dia_da_semana}")
            for event in eventos:
                data = parse(event['start']['dateTime'])
                embed.add_field(
                name=f"\u200B", value=f"```yml\nAssunto: {event['summary']}\nLocal: {event['location']}\nData: {data.strftime('%d/%m/%Y - %H:%M')} - Hora de Brasilia```", inline=False)
                embed.set_footer(
                    text="")
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Calendar(bot))
