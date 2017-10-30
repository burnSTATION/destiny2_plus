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
        await client.send_message(message.channel, embed=stats_request(message.content[7:]))

def daily_milestone():
    r = requests.get(api_root + '/Destiny2/Milestones/', headers = api_key)
    return(str(r.json()))

def clan_milestones():
    r = requests.get(api_root + '/Destiny2/Clan/2809604/WeeklyRewardState/', headers = api_key).json()
    start_date = r['Response']['startDate']
    end_date = r['Response']['endDate']
    milestoneTime = 'The current clan milestone timer started at ' + start_date + ' and will end at ' + end_date + '. Unfortuneately this is all the data we are able to pull reliably at this time.'
    return(milestoneTime)

def stats_request(user):
    if user == 'synapse':
        name = 'SYNAPSE#11498'
        char = 'Titan'
        emblem = '<:titan:374636049910988801>'
        network = '<:bnet:374636065509736458>'
        accountType = '4'
        destinyId = '4611686018467291248'
    elif user == 'musclehamstr':
        name = 'MuscleHamstr#11639'
        char = 'Hunter'
        emblem = '<:hunter:374574917594644480>'
        network = '<:bnet:374636065509736458>'
        accountType = '4'
        destinyId = '4611686018467293944'
    elif user == 'burnstation':
        name = 'burnSTATION#1999'
        char = 'Warlock'
        emblem = '<:warlock:374575358327914498>'
        network = '<:bnet:374636065509736458>'
        accountType = '4'
        destinyId = '4611686018470929530'

    r = requests.get(api_root + '/Destiny2/' + str(accountType) + '/Account/' + str(destinyId) +'/Stats/', headers = api_key).json()
    characterId = (r['Response']['characters'][0]['characterId'])

    highestCharacterLevel = r['Response']['characters'][0]['results']['allPvP']['allTime']['highestCharacterLevel']['basic']['displayValue']
    highestLightLevel = r['Response']['characters'][0]['results']['allPvP']['allTime']['highestLightLevel']['basic']['displayValue']
    combatRating = r['Response']['characters'][0]['results']['allPvP']['allTime']['combatRating']['basic']['displayValue']

    embed=discord.Embed(title = str(network) + name, description = emblem + char + " Level " + highestCharacterLevel + ' |' + '<:light:374575358596612106>' + str(highestLightLevel))
    return (embed)



client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
