import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
  print('authenticating...')
  print('authenticated as:' + client.user.name + "with ID:" + client.user.id)

@client.event
async def on_message(message):
  if message.content.startswith('!milestones'):
      await clinet.send_message(message.channel, 'Oops! this function is not available yet!')

client.run('Yj7YO5jxg4fL0UwkSqN-HWznojJZ_fas')
