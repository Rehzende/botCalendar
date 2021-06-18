from discord.ext import commands
import discord
import datetime
from utils import calendy as call
from utils.google_calendar import list_events
from datetime import date


class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Retorna os agendamento de estudo do dia atual")
    async def agenda(self, ctx):
        """
        :param ctx:
        :return: Retorna os agendamento de estudo do dia atual
        """
        eventos = list_events.getEvents()
        data = date.today().strftime("%d %b %Y")

        if not eventos:
            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker: ", description=data)
            embed.add_field(name=f"**:cold_sweat: Sem Agenda**",
                            value=f"Use ```>criar_agenda```  e agende um estudo, bora aprender!! ", inline=False)
            embed.set_footer(
                text="Se você está afim de aprender algo, agende um momento de estudo, para que os demais possam saber do seu interesse.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="📚 Agenda de Estudos :loudspeaker: ", description=data)
            for event in eventos:
                embed.add_field(
                    name=f"**:white_check_mark: {event['summary']}**", value=f" Local:  {event['location']} ", inline=False)
                embed.set_footer(
                    text="Agenda: ✅ - Ativa - 🟥 - Cancelada(provavelmente já passou do horário)")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Status(bot))
