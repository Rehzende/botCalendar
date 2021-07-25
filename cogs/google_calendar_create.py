from typing import Pattern
from discord.ext import commands
import discord
import datetime, re, asyncio
from utils.google_calendar import create_event as event
from datetime import date
import logging
from dateutil.parser import parse
from dateutil import tz


date_pattern = re.compile("^data:[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$")
hour_pattern = re.compile("^hora:([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
BR = tz.gettz("America/Sao_Paulo")


class Calendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Criar um evento no google calendar")
    async def criar_agenda(self, ctx, data=None, hora=None):
        """
        usage: >criar_agenda

        """
        if not data:
            embed = discord.Embed(
                title="Crie um momento de estudo aqui",
                colour=discord.Colour(0xACB4CE),
                description="Crie um momento de estudo, a agenda será enviada no canal de agenda no dia do evento!!",
            )
            embed.add_field(
                name="Copie o comando abaixo e modifique os dados nescessarios",
                value="```>criar_agenda  data:dd/mm/yyyy hora:HH:mm ```",
                inline=False,
            )
            await ctx.send(embed=embed, delete_after=60)
        else:
            await ctx.message.delete()
            embed = discord.Embed(
                title="Qual assunto do evento?",
                description="Responda em até 2 minutos!!",
            )
            sent = await ctx.send(embed=embed, delete_after=120)
            try:
                msg = await self.bot.wait_for(
                    "message",
                    timeout=30,
                    check=lambda message: message.author == ctx.author
                    and message.channel == ctx.channel,
                )
                if msg:
                    await sent.delete()
                    await msg.delete()

                    dt_str = data[-10:] + " " + hora[-5:]
                    dt_obj = datetime.datetime.strptime(dt_str, "%d/%m/%Y %H:%M")
                    date = datetime.datetime(
                        dt_obj.year,
                        dt_obj.month,
                        dt_obj.day,
                        dt_obj.hour,
                        0,
                        00,
                        0,
                        tzinfo=BR,
                    )

                    if date_pattern.match(data) and hour_pattern.match(hora):
                        res = event.createEvent(
                            msg.content,
                            date,
                            "🎙️ CANAL DE VOZ",
                            msg.content,
                        )
                        data = parse(res["start"]["dateTime"])
                        embed = discord.Embed(
                            title="Evento criado!!", colour=discord.Colour(0x7ED321)
                        )
                        embed.add_field(
                            name="Evento: ",
                            value=f"```{res['summary']}```",
                            inline=False,
                        )
                        embed.add_field(
                            name="Data:",
                            value=f"{data.strftime('%d/%m/%Y - %H:%M')} - Hora de Brasilia",
                            inline=False,
                        )
                        embed.add_field(
                            name="Local:", value=f"{res['location']} ", inline=False
                        )
                        message_sent = await ctx.send(embed=embed)
                        dt = datetime.datetime.strptime(
                            str(res["start"]["dateTime"]), "%Y-%m-%dT%H:%M:%S%z"
                        )
                        await self.bot.pg_con.execute(
                            "INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)",
                            message_sent.id,
                            res["id"],
                            dt,
                            res["summary"],
                            res["htmlLink"],
                        )
                else:
                    await ctx.reply("Ajuste a data ou a hora!")
            except asyncio.TimeoutError:
                await sent.delete()
                await ctx.send("Agendamento cancelado!", delete_after=10)


def setup(bot):
    bot.add_cog(Calendar(bot))
