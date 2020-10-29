# ( ͡° ͜ʖ ͡°)


print("BreenBot is starting...")

# Import dependencies
import discord, os, dotenv, random, smtplib, sys, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask
from threading import Thread



# Load ENV flies
dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
USER = os.getenv("EMAIL_ADDRESS")
PASS = os.getenv("EMAIL_PASSWORD")
MAILING_LIST = os.getenv("MAILING_LIST").split("|")
ENVLOADED = os.getenv('ENVLOADED')



# Set up breenbot mailer with SMTP
server = smtplib.SMTP("smtp.office365.com", 587)



# Create intents
intents = discord.Intents.all()

# Create discord Bot Client
client = discord.Client(intents=intents)



# on_ready() event
@client.event
async def on_ready():

  # Define channels
  global InfoSecLogs
  global InfoSecRepo
  global SelfRoles
  global InfoSecCmd


  # Initialize channels
  InfoSecLogs = loadchan(768628551091748884)
  InfoSecRepo = loadchan(770712499850182710)
  SelfRoles = loadchan(768901512130199552)
  InfoSecCmd = loadchan(771044685027344474)

  # Uncomment to set BreenBot to clear all logs
  #while True:
  #  await InfoSecLogs.purge()
  #  await InfoSecRepo.purge()


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

  SelfRolesMSG4 = await SelfRoles.send('How would you describe your personality?\n🙃 = goofy/crazy\n😠 = agressive\n🐕‍🦺 = loyal\n😊 = friendly\n🙂 = chill')
  await SelfRolesMSG4.add_reaction('🙃')
  await SelfRolesMSG4.add_reaction('😠')
  await SelfRolesMSG4.add_reaction('🐕‍🦺')
  await SelfRolesMSG4.add_reaction('😊')
  await SelfRolesMSG4.add_reaction('🙂')

  SelfRolesMSG5 = await SelfRoles.send('What are your interests?\n🎧 = music\n🏌️ = golfing\n🎨 = art\n💻 = computers')
  await SelfRolesMSG5.add_reaction('🎧')
  await SelfRolesMSG5.add_reaction('🏌️')
  await SelfRolesMSG5.add_reaction('🎨')
  await SelfRolesMSG5.add_reaction('💻')

  SelfRolesMSG6 = await SelfRoles.send('Do you want to join the <#771142908967518268> channel? (NSFW)')
  await SelfRolesMSG6.add_reaction('😳')

  # Define selfrole data
  global SelfRoleEmojis
  global SelfRoleRoles

  # An array of emojis and their corresponding role
  SelfRoleEmojis = ['👩', '👨', '✔️', '💑', '🧑', '🙃', '😠', '🐕‍🦺', '🎧', '🏌️', '🎨', '💻', '😊', '🙂', '😳']
  SelfRoleRoles = [768899694033764462, 768899841580728340, 768632488842100737, 768689359461154827, 768938126516682833, 769077333452783616, 769223941473697792, 769078138582859816, 769077092036902962, 769077211742994443, 769077009577934858, 769286509508952074, 769287800272191518, 769287556352835615, 771154548948598815]


  print('BreenBot is active.')


@client.event
async def on_message(message):
  if message.channel.id == 771044685027344474:
    if loadrole(message.guild, 770104165761417277) in message.author.roles:
      try:
        if message.content[0:4] == 'kick':
          print('kicking user ID: ' + message.content[5:] + '\n           name: ' + loadmember(message.guild, int(message.content[5:])).name)
          await ISLog(7, message.guild, message.content + " | " + loadmember(message.guild, int(message.content[5:])).mention)
          await loadmember(message.guild, int(message.content[5:])).kick()
      except:
        pass
      
      try:
        if message.content[0:4] == 'test':
          await ISLog(7, message.guild, message.content)
      except:
        pass

    await message.delete()



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
  await ISLog(3, str(member.guild), str(member))
  if str(member.guild) == "The Nexus":
    if member.id == 433433822248304641: # If user is me, then give me co-owner role and infosec role
      await member.add_roles(loadrole(loadguild(767517834812194816), 767518645114110012))
      await member.add_roles(loadrole(loadguild(767517834812194816), 768632488842100737))
      await member.add_roles(loadrole(loadguild(767517834812194816), 770104165761417277))
      await member.add_roles(loadrole(loadguild(767517834812194816), 771052131359784982))
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

def loadmember(guild, id): # Loads a member from an id
  print('User @' + guild.get_member(id).name + ' loaded.')
  return guild.get_member(id)



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

# Info Sec Logger function
async def ISLog(code, guild, details="None."):
  global InfoSecLogs
  global InfoSecRepo
  global MAILING_LIST
  global USER
  global PASS
  global server

  if IS_severity[code] != "NULL":
    await InfoSecRepo.send('@everyone\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)

    if guild != "BreenBot Logging Server": # If guild is NOT the logging server, then:
      await InfoSecLogs.send('<@&768632488842100737>\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)

      server.connect("smtp.office365.com", 587)
      server.starttls()
      outgoing_message = "<h2>Security activity detected.</h2><hr><br>Guild affected: <b>" + guild + "</b><br>Activity Type: <b>" + IS_codes[code] + "</b><br>Severity Rating: <b>" + IS_severity[code] + "</b><br>Other Details: <b>" + details + "</b><br><br>If you would like to remove your email from the mailing list, please contact the author on Discord."      
      server.login(USER, PASS)
      
      for i in range(len(MAILING_LIST)):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Security Update"
        msg['From'] = "breenbot.notifier@outlook.com"
        msg['To'] = MAILING_LIST[i]

        msg.attach(MIMEText(outgoing_message, 'plain'))
        msg.attach(MIMEText(outgoing_message, 'html'))
        server.sendmail(USER, MAILING_LIST[i], msg.as_string())
      
      server.quit()

  else:
    await InfoSecRepo.send('\nURGENCY: ' + IS_severity[code] + '\nISSUE         : ' + IS_codes[code] + '\nGUILD       : ' + str(guild) + '\nDETAILS   : ' + details)


# keep_alive test
keep_alive()

# Run discord Bot Client
client.run(TOKEN)
