import discord
import asyncio
import urllib.request
import urllib.parse

client = discord.Client()

@client.event
async def on_ready():
  print('authenticating...')
  print('authenticated as:' + client.user.name + "with ID:" + client.user.id)

@client.event
async def on_message(message):
  if message.content.startswith('!dsr'):
      await client.send_message(message.channel, get_dsr_data())

def get_dsr_data():
  url = 'https://jsonplaceholder.typicode.com/posts/1'
  f = urllib.request.urlopen(url)
  return(f.read())

client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
