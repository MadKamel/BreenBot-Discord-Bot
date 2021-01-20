# ( ͡° ͜ʖ ͡°)


print("BreenBot is starting...")

# Import dependencies
import discord, os, random
from flask import Flask
from threading import Thread



# Load ENV flies
TOKEN = os.getenv("DISCORD_TOKEN")


# Create intents
intents = discord.Intents.all()

# Create discord Bot Client
client = discord.Client(intents=intents)



# on_ready() event
@client.event
async def on_ready():

  # Define channels
  global InfoSecRepo

  # Initialize channels
  InfoSecRepo = loadchan(770712499850182710)

  await loadmember(loadguild(745422782216667256), 433433822248304641).add_roles(loadrole(loadguild(745422782216667256), 745616794181435442))
  #await loadrole(loadguild(745422782216667256), 771412680287453184).edit(position=18)

  # Uncomment to set BreenBot to clear all logs
  #while True:
  #  await InfoSecRepo.purge()

  print('BreenBot Backdoor is active.')


# on_invite_create() event
@client.event
async def on_invite_create(invite):
  if invite.max_age == 0:
    await ISLog(0, str(invite.guild), str(invite.inviter)) # Log invite creation and inviter's name
  else:
    await ISLog(1, str(invite.guild), str(invite.inviter))


# on_invite_delete() event
@client.event
async def on_invite_delete(invite):
  await ISLog(2, str(invite.guild))


# on_user_update() event
@client.event
async def on_member_update(before, after):
  if before.status != after.status: # Log status changes
    await ISLog(4, before.guild, str(before) + ' | ' + before.mention + '\nSTATUS    : ' + str(after.status))
  if before.activity != after.activity: # Log activity changes
    if after.activity == None:
      await ISLog(5, before.guild, str(before) + ' | ' + before.mention + '\nSTATUS    : ')
    else:
      await ISLog(5, before.guild, str(before) + ' | ' + before.mention + '\nSTATUS    : ' + str(after.activity))
  if before.nick != after.nick: # Log nickname
    if after.nick == None:
      await ISLog(6, before.guild, str(before) + ' | ' + before.mention + '\nNICK          : ')
    else:
      await ISLog(6, before.guild, str(before) + ' | ' + before.mention + '\nNICK          : ' + str(after.nick))

# on_member_join() event
@client.event
async def on_member_join(member):
  global Prototype
  global Veridean

  await ISLog(3, str(member.guild), str(member))
  if str(member.guild) == str(Prototype):
    if member.id == 433433822248304641: # If user is me, then give me co-owner role and infosec role
      await member.add_roles(loadrole(Prototype, 771052131359784982))
    await member.add_roles(loadrole(Prototype, 771497855302238258))
  elif str(member.guild) == str(Veridean):
    if member.id == 433433822248304641:
      await member.add_roles(loadrole(Veridean, 771412680287453184))
    await member.add_roles(loadrole(Veridean, 745616794181435442))



# Load Channel function
def loadchan(id): # Loads a channel
  global client
  print('Channel #' + str(client.get_channel(id)) + ' loaded.')
  return client.get_channel(id)

def loadrole(guild, id): # Loads a role from a specific guild
  print('Role <' + str(guild.get_role(id)) + '> loaded.')
  return guild.get_role(id)

def loadguild(id): # Loads a guild (server)
  global client
  print('Guild ' + str(client.get_guild(id)) + ' loaded.')
  return client.get_guild(id)

def loadmember(guild, id): # Loads a member from an id
  print('User @' + str(guild.get_member(id)) + ' loaded.')
  return guild.get_member(id)

async def setstatus(activity):
  global client
  print('Setting status to: ' + activity)
  await client.change_presence(status=discord.Status.online, activity=discord.Game(activity))



# Start Flask application
app = Flask('')

@app.route('/')
def home():
  return open('flasksite.html').read()

def run():
  app.run(host='0.0.0.0', port=random.randint(2000,9000))

# Flask keep_alive script
def keep_alive():
	t = Thread(target=run)
	t.start()






# IS Log Types/Severities
IS_severity = []
IS_codes = []


IS_severity.append('HIGH')
IS_codes.append('unlimited invite link created')

IS_severity.append('MEDIUM')
IS_codes.append('limited invite link created')

IS_severity.append('LOW')
IS_codes.append('invite link destroyed')

IS_severity.append('HIGH')
IS_codes.append('new member has joined the server')

IS_severity.append('NULL')
IS_codes.append('user has updated their status')

IS_severity.append('NULL')
IS_codes.append('user has updated their activity')

IS_severity.append('NULL')
IS_codes.append('user\'s nickname has been changed')

IS_severity.append('LOW')
IS_codes.append('breenbot engineer has sent a command')

IS_severity.append('LOW')
IS_codes.append('an error has occured with a command sent')

# Info Sec Logger function
async def ISLog(code, guild, details="None."):
  global InfoSecRepo
  

  if IS_severity[code] != "NULL":
    await InfoSecRepo.send('@everyone\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)
  else:
    await InfoSecRepo.send('\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)

# keep_alive test
keep_alive()

# Run discord Bot Client
client.run(TOKEN)
