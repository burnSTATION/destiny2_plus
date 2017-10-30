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
    if message.content.startswith('.milestones'):
        await client.send_message(message.channel, milestone_request())

    elif message.content.startswith('.stats'):
        await client.send_message(message.channel, stats_request(message.content[7:]))


def milestone_request():
    r = requests.get(api_root + '/Destiny2/Clan/2809604/WeeklyRewardState/', headers = api_key).json()
    start_date = r['Response']['startDate']
    end_date = r['Response']['endDate']
    milestoneTime = 'The current clan milestone timer started at ' + start_date + ' and will end at ' + end_date + '. Unfortuneately this is all the data we are able to pull reliably at this time.'
    return(milestoneTime)

def stats_request(user):
    if user == 'synapse':
        char = 'Titan'
        accountType = '4'
        destinyId = '4611686018467291248'
    elif user == 'musclehamstr':
        char = 'Hunter'
        accountType = '4'
        destinyId = '4611686018467293944'
    elif user == 'burnstation':
        char = 'Warlock'
        accountType = '4'
        destinyId = '4611686018470929530'

    r = requests.get(api_root + '/Destiny2/' + str(accountType) + '/Account/' + str(destinyId) +'/Stats/', headers = api_key).json()
    characterId = (r['Response']['characters'][0]['characterId'])

    highestCharacterLevel = r['Response']['characters'][0]['results']['allPvP']['allTime']['highestCharacterLevel']['basic']['displayValue']
    highestLightLevel = r['Response']['characters'][0]['results']['allPvP']['allTime']['highestLightLevel']['basic']['displayValue']
    combatRating = r['Response']['characters'][0]['results']['allPvP']['allTime']['combatRating']['basic']['displayValue']

    stats = char + ' Level ' + highestCharacterLevel + '. Max light level ' +  highestLightLevel + ' with a combat rating of ' + combatRating + '.'
    return (stats)

client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
