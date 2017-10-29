import discord
import asyncio
import requests

client = discord.Client()
api_key = {'X-API-Key':'a46292e41c284dfbb9065b5864ec7ff0'}
api_root = 'https://www.bungie.net/Platform'

@client.event
async def on_ready():
    print('Authenticating...')
    print('Authenticated with Discord ID:' + ' ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('.dsr'):
        await client.send_message(message.channel, milestone_request())

    elif message.content.startswith('.stats'):
        await client.send_message(message.channel, stats_request(message.content[7:]))


def milestone_request():
    r = requests.get(api_root + '/Destiny2/Clan/2809604/WeeklyRewardState/', headers = api_key)
    return(r.json())

def stats_request(user):
    r = requests.get(api_root + '/Destiny2/SearchDestinyPlayer/-1/' + user + '/', headers = api_key)
    return (r.json())

client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
