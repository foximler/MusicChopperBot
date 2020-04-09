import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.utils import get
bot = commands.Bot(command_prefix = ",")
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
import asyncio
import youtube_dl

@bot.event
async def on_message(message):
	if message.content.startswith('!AMAK'):

		#channel = ctx.message.author.voice.channel 
		channel = bot.get_channel(575134662285066260)
		print(channel)
		voice = await channel.connect()
		source = FFmpegPCMAudio('nam.mp3')
		player = voice.play(source)
	if message.content.startswith('!leave')
		break

bot.run(TOKEN)
