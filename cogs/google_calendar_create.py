from typing import Pattern
from discord.ext import commands
import discord
import datetime
import re
import asyncio
from utils import calendy as call
from utils.google_calendar import create_event as event
from datetime import date, datetime
import logging

# logging.basicConfig(level=logging.DEBUG)
date_pattern = re.compile(
    "^data:[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$")
hour_pattern = re.compile("^hora:([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")


class Calendar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Criar um evento no google calendar")
    async def criar_agenda(self, ctx, evento=None, data=None, hora=None):
        """
        usage: >criar_agenda

        """
        if not evento:
            embed = discord.Embed(title="Crie um momento de estudo aqui", colour=discord.Colour(
                0xacb4ce), description="Crie um momento de estudo, a agenda será enviada no canal de agenda no dia do evento!!")
            embed.add_field(name=":blue_book:  - ESTUDO  - ANSIBLE",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:ansible data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":closed_book:  - ESTUDO  - TERRAFORM",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:terraform data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":green_book:  - ESTUDO  - PACKER",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:packer data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":orange_book:  - ESTUDO  - GIT",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:git data:dd/mm/yyyy hora:HH:mm  ```",  inline=False)
            embed.add_field(name=":beers:  - BOTECO",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda boteco data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            await ctx.send(embed=embed, delete_after=60)
        else:
            await ctx.message.delete()
            embed = discord.Embed(
                title="Qual a descrição do evento?",
                description="||Responda em  60 segundos!!||"
            )
            sent = await ctx.send(embed=embed, delete_after=60)

            try:
                msg = await self.bot.wait_for(
                    "message",
                    timeout=30,
                    check=lambda message: message.author == ctx.author
                    and message.channel == ctx.channel
                )
                if msg:
                    await sent.delete()
                    await msg.delete()

                    date_time_str = data[-10:] + " " + hora[-5:]
                    date_time_obj = datetime.strptime(
                        date_time_str, '%d/%m/%Y %H:%M')
                    if date_pattern.match(data) and hour_pattern.match(hora):
                        if evento == "estudo:ansible":
                            res = event.createEvent(
                                "📚 ESTUDO - ANSIBLE", date_time_obj, "🎙️ CANAL DE VOZ - ANSIBLE", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            embed.add_field(
                                name="Criado por:", value=f"{ ctx.message.author}",  inline=False)
                            embed.set_footer(
                                text="Reaja com: ✅ - Para ser notificado desse envento!")
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                        if evento == "estudo:terraform":
                            res = event.createEvent(
                                "📚 ESTUDO - TERRAFORM", date_time_obj, "🎙️ CANAL DE VOZ - TERRAFORM", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                        if evento == "estudo:packer":
                            res = event.createEvent(
                                "📚 ESTUDO - PACKER", date_time_obj, "🎙️ CANAL DE VOZ - PACKER", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                        if evento == "estudo:git":
                            res = event.createEvent(
                                "📚 ESTUDO - GIT", date_time_obj, "🎙️ CANAL DE VOZ - GIT", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            embed.set_footer(
                                text="Reaja com: ✅ - Para ser notificado desse envento!")
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                        if evento == "estudo:nomad":
                            res = event.createEvent(
                                "📚 ESTUDO - NOMAD", date_time_obj, "🎙️ CANAL DE VOZ - NOMAD", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                        if evento == "boteco":
                            res = event.createEvent(
                                "🍻 BOTECO", date_time_obj, "🎙️ CANAL DE VOZ - 42", msg.content)
                            embed = discord.Embed(
                                title="Evento criado!!", colour=discord.Colour(0x7ed321))
                            embed.add_field(name="Evento: ",
                                            value=f"{res['summary']}",  inline=False)
                            embed.add_field(
                                name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                            embed.add_field(
                                name="Local:", value=f"{res['location']} ",  inline=False)
                            embed.add_field(
                                name="Descrição:", value=f"```{res['description']}``` ",  inline=False)
                            message_sent =  await ctx.send(embed=embed)
                            await self.bot.pg_con.execute("INSERT INTO events (message_id, calendar_id, date_time, event_name, event_link ) VALUES ($1, $2, $3, $4, $5)", message_sent.id, res['id'], date_time_obj, res['summary'], res['htmlLink'])
                    else:
                        await ctx.reply('Ajuste a data ou a hora!')
            except asyncio.TimeoutError:
                await sent.delete()
                await ctx.send("Agendamento cancelado!", delete_after=10)


def setup(bot):
    bot.add_cog(Calendar(bot))
