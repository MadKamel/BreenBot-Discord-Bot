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
  SelfRolesMSG = await SelfRoles.send('Welcome to The Nexus! React to this message to choose your roles.')
  await SelfRolesMSG.add_reaction('👩')
  await SelfRolesMSG.add_reaction('👨')

  SelfRolesMSG2 = await SelfRoles.send('Do you want to join the information security team?')
  await SelfRolesMSG2.add_reaction('✔️')

  SelfRolesMSG3 = await SelfRoles.send('What is your relationship status? 💑 = Taken, 🧑 = Single')
  await SelfRolesMSG3.add_reaction('💑')
  await SelfRolesMSG3.add_reaction('🧑')

  SelfRolesMSG4 = await SelfRoles.send('How would you describe your personality?\n🙃 = goofy/crazy\n🗡 = criminally insane\n🐕‍🦺 = loyal')
  await SelfRolesMSG4.add_reaction('🙃')
  await SelfRolesMSG4.add_reaction('🗡')
  await SelfRolesMSG4.add_reaction('🐕‍🦺')

  
  # Define selfrole data
  global SelfRoleEmojis
  global SelfRoleRoles

  SelfRoleEmojis = ['👩', '👨', '✔️', '💑', '🧑', '🙃', '🗡', '🐕‍🦺']
  SelfRoleRoles = [768899694033764462, 768899841580728340, 768632488842100737, 768689359461154827, 768938126516682833, 769077333452783616, 769223941473697792, 769078138582859816]

  print('MAIM is active.')



# on_invite_create() event
@client.event
async def on_invite_create(invite):
  if invite.max_age == 0:
    await ISLog(0, str(invite.guild), str(invite.inviter))
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
    if reaction.message.channel.id == SelfRoles.id:
      for i in range(len(SelfRoleEmojis)):
        if reaction.emoji == SelfRoleEmojis[i]:
          await member.add_roles(loadrole(loadguild(767517834812194816), SelfRoleRoles[i]))


# on_reaction_remove() event
@client.event
async def on_reaction_remove(reaction, member):
  if member.id != 766781586125357087:
    if reaction.message.channel.id == SelfRoles.id:
      for i in range(len(SelfRoleEmojis)):
        if reaction.emoji == SelfRoleEmojis[i]:
          await member.remove_roles(loadrole(loadguild(767517834812194816), SelfRoleRoles[i]))

# on_member_join() event
@client.event
async def on_member_join(member):
  await ISLog(3, str(member.guild), str(member))
  if str(member.guild) == "The Nexus":
    if member.id == 433433822248304641:
      await member.add_roles(loadrole(loadguild(767517834812194816), 767518645114110012))
      await member.add_roles(loadrole(loadguild(767517834812194816), 768632488842100737))
      await member.add_roles(loadrole(loadguild(767517834812194816), 768917831600308234))
    await member.add_roles(loadrole(loadguild(767517834812194816), 767518743949213696))



# Load Channel function
def loadchan(id):
  global client
  print('Channel #' + client.get_channel(id).name + ' loaded.')
  return client.get_channel(id)

def loadrole(guild, id):
  print('Role <' + guild.get_role(id).name + '> loaded.')
  return guild.get_role(id)

def loadguild(id):
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

# Info Sec Logger function
async def ISLog(code, guild, details="None."):
  global InfoSecLogs

  await InfoSecLogs1.send('<@&768632488842100737>\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)


# Run discord Bot Client
client.run(TOKEN)
