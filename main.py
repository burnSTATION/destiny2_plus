# stdlib
import os.path
import json

# 3rd party
import discord
import asyncio
import requests

# should put the "openapi-2.json" file in the same folder and then
# use that filename as the first cmdline argument to load the data
# from the api doc
with open(sys.argv[1]) as api:
    bungie = json.load(api)

client = discord.Client()
api_key = {'X-API-Key':'a46292e41c284dfbb9065b5864ec7ff0'}
api_root = 'https://www.bungie.net/Platform'

@client.event
async def on_ready():
    print('Authenticating...')
    print('Authenticated with Discord ID:' + ' ' + client.user.id)

@client.event
async def on_message(message):
    '''
    here we format the path based on arguments. the path definition is over when we use `--`
    everything that comes after `--` will be arguments for the function

    example:
    .dsr destiny2 clan weeklyrewardstate -- groupId=2809604
    we can also set defaults for some arguments using a config file in the app,
    but for now it's just `argument = value`
    '''

    cmd, top, args = message.content.split(' ', 3)

    if message.content.startswith('.milestone'):
        await client.send_message(message.channel, daily_milestone())

    elif message.content.startswith('.clan'):
        await client.send_message(message.channel, clan_milestones())

    elif message.content.startswith('.stats'):
        await client.send_message(message.channel, stats_request(message.content[7:]))

    elif cmd.strip == '.d2p':
        raise "not implemented yet"
        path_names, values = args.strip.split('--', 2)
        path = os.path.join('/', *path)

        top = top.lower()
        if top == 'user':
            url = user()
        elif top == 'forum':
            url = forum()
        elif top == 'groupv2':
            url = groupv2()
        elif top == 'destiny2':
            url = destiny2()
        elif top == 'community':
            url = community()
        elif top == 'trending':
            url = trending()

def daily_milestone():
    r = requests.get(api_root + '/Destiny2/Milestones/', headers = api_key)
    return(str(r.json()))

def clan_milestones():
    r = requests.get(api_root + '/Destiny2/Clan/2809604/WeeklyRewardState/', headers = api_key).json()
    return(r['Response']['endDate'])

def stats_request(user):
    r = requests.get(api_root + '/Destiny2/SearchDestinyPlayer/-1/' + user + '/', headers = api_key).json()
    return (r)

# user, forum, groupv2, destiny2, community and trending will
# all come w/ a way of searching the endpoints found in openapi-2.json
# so that you don't have to iterate over the whole list - partial input
# from the user narrows it down really quickly so every request doesn't
# take forever. it's a hack, but it will work and not be slow AF :)
def user(substr, **kw):
    path = path_search('user', )
    pass

def forum(substr, **kw):
    path = path_search('forum', substr, bungie['paths'].keys).format(**kw)
    pass

def groupv2(substr, **kw):
    path = path_search('groupv2', substr, bungie['paths'].keys).format(**kw)
    pass

def destiny2(substr, **kw):
    path = path_search('destiny2', substr, bungie['paths'].keys).format(**kw)
    pass

def community(substr, **kw):
    path = path_search('community', substr, bungie['paths'].keys).format(**kw)
    pass

def trending(substr, **kw):
    path = path_search('trending', substr, bungie['paths'].keys).format(**kw)
    pass


def fetch(ep, **kw):
    endpoint[ep](**kw)

# this is absolutely the wrong way to do this but it only takes a few lines to implement
# and it should work so we can just fix it to something non-retarded later
# worth noting that w/ this technique we don't actually have to type the whole
# url, we just have to get close and it will still work
# e.g. `.d2p user netuser id=1234` will use `/User/GetBungieNetUserById/1234/` as its url
def path_search(prefix, substr, paths, length = 1):
    if len(substr) < length
        raise "no matching path found"

    matching = [s for s in paths if prefix in s.lower() and substr[0:length] in s.lower()]

    if matching == paths
        raise "found '{these}', but can't decide between them. try something more specific".format(these=matching.join(", "))

    if len(matching) == 1
        matching[0]
    else
        path_search(prefix, substr, matching, length + 1)

client.run('MzczOTg0ODcxMjQ2MzMxOTA2.DNauaA.7949_eWFqXqx1Dfsaj0TzbaO7WI')
