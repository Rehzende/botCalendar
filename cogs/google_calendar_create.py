from typing import Pattern
from discord.ext import commands
import discord
import datetime
import re
from utils import calendy as call
from utils.google_calendar import create_event as event
from datetime import date, datetime
import logging

# logging.basicConfig(level=logging.DEBUG)
date_pattern = re.compile(
    "^data:[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$")
hour_pattern = re.compile("^hora:([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")


class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Criar um evento no google calendar")
    async def criar_agenda(self, ctx, *arg):
        """
        :param ctx:
        :return: Embed of the status of each server
        """
        if not arg:
            embed = discord.Embed(title="Crie um momento de estudo aqui", colour=discord.Colour(
                0xacb4ce), description="Crie um momento de estudo, a agenda será enviada no canal de agenda no dia do evento!!")
            embed.add_field(name=":blue_book:  - ESTUDO  - ANSIBLE",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:ansible data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":closed_book:  - ESTUDO  - TERRAFORM",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:terraform data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":green_book:  - ESTUDO  - PACKER",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:packer data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":orange_book:  - ESTUDO  - GIT",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda estudo:git data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            embed.add_field(name=":beers:  - BOTECO",
                            value="Copie o comando abaixo e modifique os dados nescessarios```\n >criar_agenda boteco data:dd/mm/yyyy hora:HH:mm ```",  inline=False)
            await ctx.send(embed=embed)
        else:
            data = arg[1]
            hora = arg[2]
            date_time_str = data[-10:] + " " + hora[-5:]
            date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
            if date_pattern.match(arg[1]) and hour_pattern.match(arg[2]):
                if arg[0] == "estudo:ansible":
                    res = event.createEvent(
                        "📚 ESTUDO - ANSIBLE", date_time_obj, "🎙️ CANAL DE VOZ - ANSIBLE")
                    embed = discord.Embed(
                        title="Evento criado!!", colour=discord.Colour(0x7ed321))
                    embed.add_field(name="Evento: ",
                                    value=f"{res['summary']}",  inline=False)
                    embed.add_field(
                        name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                    embed.add_field(
                        name="Local:", value=f"{res['location']} ",  inline=False)
                    await ctx.send(embed=embed)
                if arg[0] == "estudo:terraform":
                    res = event.createEvent(
                        "📚 ESTUDO - TERRAFORM", date_time_obj, "🎙️ CANAL DE VOZ - TERRAFORM")
                    embed = discord.Embed(
                        title="Evento criado!!", colour=discord.Colour(0x7ed321))
                    embed.add_field(name="Evento: ",
                                    value=f"{res['summary']}",  inline=False)
                    embed.add_field(
                        name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                    embed.add_field(
                        name="Local:", value=f"{res['location']} ",  inline=False)
                    await ctx.send(embed=embed)
                if arg[0] == "estudo:packer":
                    res = event.createEvent(
                        "📚 ESTUDO - PACKER", date_time_obj, "🎙️ CANAL DE VOZ - PACKER")
                    embed = discord.Embed(
                        title="Evento criado!!", colour=discord.Colour(0x7ed321))
                    embed.add_field(name="Evento: ",
                                    value=f"{res['summary']}",  inline=False)
                    embed.add_field(
                        name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                    embed.add_field(
                        name="Local:", value=f"{res['location']} ",  inline=False)
                    await ctx.send(embed=embed)
                if arg[0] == "estudo:git":
                    res = event.createEvent(
                        "📚 ESTUDO - GIT", date_time_obj, "🎙️ CANAL DE VOZ - GIT")
                    embed = discord.Embed(
                        title="Evento criado!!", colour=discord.Colour(0x7ed321))
                    embed.add_field(name="Evento: ",
                                    value=f"{res['summary']}",  inline=False)
                    embed.add_field(
                        name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                    embed.add_field(
                        name="Local:", value=f"{res['location']} ",  inline=False)
                    await ctx.send(embed=embed)
                if arg[0] == "boteco":
                    res = event.createEvent(
                        "🍻 BOTECO", date_time_obj, "🎙️ CANAL DE VOZ - 42")
                    embed = discord.Embed(
                        title="Evento criado!!", colour=discord.Colour(0x7ed321))
                    embed.add_field(name="Evento: ",
                                    value=f"{res['summary']}",  inline=False)
                    embed.add_field(
                        name="Data:", value=f"{res['start']['dateTime']} ",  inline=False)
                    embed.add_field(
                        name="Local:", value=f"{res['location']} ",  inline=False)
                    await ctx.send(embed=embed)
            else:
                await ctx.reply('Ajuste a data ou a hora!')


def setup(bot):
    bot.add_cog(Status(bot))
