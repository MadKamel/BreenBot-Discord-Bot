# ( ͡° ͜ʖ ͡°)


# Import dependencies
import discord, os, dotenv

# Load ENV flies
dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


# Create intents
intents = discord.Intents.all()

# Create discord Bot Client
client = discord.Client(intents=intents)



# on_ready() event
@client.event
async def on_ready():
  
  # Define channels
  global InfoSecLogs
  global SelfRoles

  
  # Initialize channels
  InfoSecLogs = loadchan(768628551091748884)
  SelfRoles = loadchan(768901512130199552)

  # Send selfrole messages
  await SelfRoles.purge()
  SelfRolesMSG = await SelfRoles.send('Welcome to The Nexus! React to these messages to choose your roles.\nWhat is your gender?')
  await SelfRolesMSG.add_reaction('👩')
  await SelfRolesMSG.add_reaction('👨')

  SelfRolesMSG2 = await SelfRoles.send('Do you want to join the information security team?')
  await SelfRolesMSG2.add_reaction('✔️')

  SelfRolesMSG3 = await SelfRoles.send('What is your relationship status?\n💑 = Taken\n🧑 = Single')
  await SelfRolesMSG3.add_reaction('💑')
  await SelfRolesMSG3.add_reaction('🧑')

  SelfRolesMSG4 = await SelfRoles.send('How would you describe your personality?\n🙃 = goofy/crazy\n🗡 = criminally insane\n🐕‍🦺 = loyal\n😠 = edgy/angry\n🙂 = chill')
  await SelfRolesMSG4.add_reaction('🙃')
  await SelfRolesMSG4.add_reaction('🗡')
  await SelfRolesMSG4.add_reaction('🐕‍🦺')
  await SelfRolesMSG4.add_reaction('😠')
  await SelfRolesMSG4.add_reaction('🙂')

  SelfRolesMSG5 = await SelfRoles.send('What are your interests?\n🎧 = music\n🏌️ = golfing\n🎨 = art\n💻 = computers')
  await SelfRolesMSG5.add_reaction('🎧')
  await SelfRolesMSG5.add_reaction('🏌️')
  await SelfRolesMSG5.add_reaction('🎨')
  await SelfRolesMSG5.add_reaction('💻')

  # Define selfrole data
  global SelfRoleEmojis
  global SelfRoleRoles

  # An array of emojis and their corresponding role
  SelfRoleEmojis = ['👩', '👨', '✔️', '💑', '🧑', '🙃', '🗡', '🐕‍🦺', '🎧', '🏌️', '🎨', '💻', '😠', '🙂']
  SelfRoleRoles = [768899694033764462, 768899841580728340, 768632488842100737, 768689359461154827, 768938126516682833, 769077333452783616, 769223941473697792, 769078138582859816, 769077092036902962, 769077211742994443, 769077009577934858, 769286509508952074, 769287800272191518, 769287556352835615]

  # Snippet of code from back when it was called MAIM
  print('MAIM is active.')



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


# on_reaction_add() event
@client.event
async def on_reaction_add(reaction, member):
  if member.id != 766781586125357087: # If the user reacting is not BreenBot
    if reaction.message.channel.id == SelfRoles.id: # Makes sure the channel handled is the selfroles channel
      for i in range(len(SelfRoleEmojis)):
        if reaction.emoji == SelfRoleEmojis[i]:
          await member.add_roles(loadrole(loadguild(767517834812194816), SelfRoleRoles[i])) # Add role


# on_reaction_remove() event
@client.event
async def on_reaction_remove(reaction, member):
  if member.id != 766781586125357087: # Makes sure the user reacting is NOT BreenBot.
    if reaction.message.channel.id == SelfRoles.id: # Makes sure the channel handled is the selfroles channel
      for i in range(len(SelfRoleEmojis)):
        if reaction.emoji == SelfRoleEmojis[i]:
          await member.remove_roles(loadrole(loadguild(767517834812194816), SelfRoleRoles[i])) # Remove role


# on_user_update() event
@client.event
async def on_member_update(before, after):
  if before.status != after.status: # Log status changes
    await ISLog(4, before.guild, str(before) + '\nSTATUS    : ' + str(after.status))
  if before.activity != after.activity: # Log activity changes
    if after.activity == None:
      await ISLog(5, before.guild, str(before) + '\nSTATUS    : ')
    else:
      await ISLog(5, before.guild, str(before) + '\nSTATUS    : ' + str(after.activity))
  if before.nick != after.nick: # Log nickname
    if after.nick == None:
      await ISLog(6, before.guild, str(before) + '\nNICK          : ')
    else:
      await ISLog(6, before.guild, str(before) + '\nNICK          : ' + str(after.nick))

# on_member_join() event
@client.event
async def on_member_join(member):
  await ISLog(3, str(member.guild), str(member))
  if str(member.guild) == "The Nexus":
    if member.id == 433433822248304641: # If user is me, then give me co-owner role and infosec role
      await member.add_roles(loadrole(loadguild(767517834812194816), 767518645114110012))
      await member.add_roles(loadrole(loadguild(767517834812194816), 768632488842100737))
      await member.add_roles(loadrole(loadguild(767517834812194816), 768917831600308234))
    await member.add_roles(loadrole(loadguild(767517834812194816), 767518743949213696))



# Load Channel function
def loadchan(id): # Loads a channel
  global client
  print('Channel #' + client.get_channel(id).name + ' loaded.')
  return client.get_channel(id)

def loadrole(guild, id): # Loads a role from a specific guild
  print('Role <' + guild.get_role(id).name + '> loaded.')
  return guild.get_role(id)

def loadguild(id): # Loads a guild (server)
  global client
  print('Guild ' + client.get_guild(id).name + ' loaded.')
  return client.get_guild(id)

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

# Info Sec Logger function
async def ISLog(code, guild, details="None."):
  global InfoSecLogs

  if IS_severity[code] != "NULL":
    await InfoSecLogs.send('<@&768632488842100737>\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)
  else:
    await InfoSecLogs.send('\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)


# Run discord Bot Client
client.run(TOKEN)
