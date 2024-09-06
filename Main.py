import discord
from discord.ext import commands
import google.generativeai as genai

intents = discord.Intents.default()
intents.message_content = True

genai.configure(api_key="CHIAVE API")
model = genai.GenerativeModel('gemini-1.5-flash')

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Presentazione del bot
@bot.command()
async def chisei(ctx):
    await ctx.send(f'Ciao, sono il bot {bot.user}! Sono stato creato da Utente342#2732, che grazie all API dell IA Gemini, sviluppata da Google, risponde a tutte le tue domande! Chiedimi qualcosa ora usando il comando /ask [domanda] in chat, o fai un quiz veloce con il comando /quiz!')

#Lista comandi
@bot.command()
async def comandi(ctx):
    await ctx.send('I miei comandi sono: /Ask [domanda] fai una domanda al bot che ti risponderá in pochi secondi. Ricorda che in un minuto puoi fare solamente 15 domande. /quiz farai iniziare un breve quiz sul riciclo. /chisei farai fare una breve presentazione al bot.')

#Domanda al bot  
@bot.command()
async def ask(ctx, * ,arg ):
    response = model.generate_content(arg)
    await ctx.send(response.text)

#Quiz
class RicicloDropdown (discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label='Ricicli la monnezza nel bidone giusto :)', description='Tutti i giorni'),
            discord.SelectOption(label='Non la ricicli sempre :/', description='Non ho sempre tempo'),
            discord.SelectOption(label='Non la ricicli mai >:(', description='Non ho voglia')
        ]

        super().__init__(placeholder='Ricicli mai la monnezza nel bidone giusto?', options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Ricicli la monnezza nel bidone giusto :)':
            await interaction.response.send_message('Complimenti!!!!!'),
        elif self.values[0] == 'Non la ricicli sempre :/':
            await interaction.response.send_message('Puoi migliorare...'),
        elif self.values[0] == 'Non la ricicli mai >:(':
            await interaction.response.send_message('Stai piú attento! Hai un altro tentativo!',view=RicicloView2())

class RicicloView (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RicicloDropdown())

class RicicloDropdown2 (discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label='Provo ad aggiustarli e riutilizzarli :)', description='Non voglio buttarli'),
            discord.SelectOption(label='Li regalo a qualcun altro :)', description='Potrebbero servirgli'),
            discord.SelectOption(label='Li butto via >:(', description='Tanto a che servono?')
        ]

        super().__init__(placeholder='Gli oggetti quando si rompono, che fai?', options=options, min_values=1, max_values=1 )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Provo ad aggiustarli e riutilizzarli :)':
            await interaction.response.send_message('Complimenti!!!!!'),
        elif self.values[0] == 'Li regalo a qualcun altro :)':
            await interaction.response.send_message('Complimenti!'),
        elif self.values[0] == 'Li butto via >:(':
            await interaction.response.send_message('Stai piú attento! Hai un ulltimo tentativo!',view=RicicloView3() )

class RicicloView2 (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RicicloDropdown2())

class RicicloDropdown3 (discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label='Certamente, cosí la prossima volta non  lo fará! :)', description='Non é tanto corretto'),
            discord.SelectOption(label='Non sempre :/', description='Magari si arrabbia'),
            discord.SelectOption(label='Non lo faccio mai >:(', description='Tanto anche io lo faccio')
        ]

        super().__init__(placeholder='Quando un tuo amico butta per terra l immondizia, gli dici qualcosa?', options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Certamente, cosí la prossima volta non  lo fará! :)':
            await interaction.response.send_message('Complimenti!!!!!'),
        elif self.values[0] == 'Non sempre :/':
            await interaction.response.send_message('Puoi migliorare...'),
        elif self.values[0] == 'Non lo faccio mai >:(':
            await interaction.response.send_message('La prossima volta devi comportarti meglio!')

class RicicloView3 (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RicicloDropdown3())

#Comando quiz
@bot.command()
async def quiz(ctx):
    await ctx.send('Vota nel sondaggio qui sotto!', view=RicicloView())

bot.run("TOKE DISCORD BOT")
