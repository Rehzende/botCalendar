from discord.ext import commands
import discord, datetime
from dateutil.parser import parse
from datetime import  date
from utils.google_calendar import list_events 
import logging

class Calendar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Retorna os agendamento de estudo da semana atual")
    async def agenda_semana(self, ctx):
        """
        usage: >agenda_semana
        """
        dt = datetime.datetime.now()
        week_number = dt.isocalendar()[1]
        firstdayofweek = datetime.datetime.strptime(f'{dt.year}-W{int(week_number)}-1', "%Y-W%W-%w").date()
        lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)



        eventos = list_events.getEventsWeek()
        data = date.today().strftime("%d %b %Y")

        if not eventos:
            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker: ", description=f"Semana: {week_number} -  {firstdayofweek} Até {lastdayofweek}")
            embed.add_field(name=f"**:cold_sweat: Sem Agenda**",
                            value=f"Use ```>criar_agenda```  e agende um estudo, bora aprender!! ", inline=False)
            embed.set_footer(
                text="Se você está afim de aprender algo, agende um momento de estudo, para que os demais possam saber do seu interesse.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker: ", description=f"Semana: {week_number} -  {firstdayofweek} Até {lastdayofweek}")
            for event in eventos:
                data = parse(event['start']['dateTime'])
                embed.add_field(
                name=f"**:white_check_mark: {event['summary']}**", value=f" **Local:**  {event['location']} - **Horário:** {data.time()} ", inline=True)
                embed.add_field(
                name=f"Descrição:", value=f"```{event['description']}``` ", inline=False)
                embed.set_footer(
                    text="Agenda: ✅ - Ativa")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Calendar(bot))
