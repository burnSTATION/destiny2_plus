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
      await client.send_message(message.channel, 'Oops! this function is not available yet!')

client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
