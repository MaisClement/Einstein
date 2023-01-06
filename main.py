import discord
from discord.ext import commands
import subprocess
import sys
import os # default module
from dotenv import load_dotenv
import linecache
from random import choice

intents = discord.Intents.default()
intents.message_content = True
version = "1.1"
from selenium import webdriver
import geckodriver_autoinstaller


#geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title


 # load all the variables from the env file

bot = discord.Bot()

print ("Firefox ✔")
liste = ['Absence de conducteur', 'Régulation Trafic', 'Panne Aiguillage', 'Panne Train Ligne', 'Retard lors du Trajet Précédent', 'Travaux sur la voie je peux pas écraser les ouvriers donc bah tu patiente et TU FERME TA BOUCHE !', 'Suspension trafic', 'Attente Correspondance', 'Arrêt Voyageur Prolongé', 'Intervention Police A Bord', "Pablo Escobar est votre conducteur aujourd'hui entre Lyon et Paris profitez en ;)", "La porte arrière de votre train ne sera pas en face du quai en gare de Tarare, merci de vous dirigez vers un autre accès si vous déscendez dans cette gare", "En raison d'une régulation, votre Intercité aura un retard de 15 minutes pour laisser passer un TGV", "Le menu de la cantine est Burger Frites aujourd'hui", "Il pleut sur Clermont", "Les débats sont interdits dans nos trains", "Ouverture de la gare du Listenbourg dirigée par Adrien", 'En raison de la traversée de la rue du 1er mai par les cartons migrateur, la ligne 1 est déviée.', "En raison d'un séisme de magnitude 10 due à la faim de votre conducteur, le train à déraillé", 'Le Conducteur Alex Roule comme un crabe sur les voies, pour plus de sécurité aucun autre train ne circule', 'destruction du train devant', 'divagation de chèvres', 'Retard à la préparation de la boîte repas', 'Les plats de la cantine sont froids', 'Tout est fermé','La pizza du conducteur est arrivée en retard']
listealex = ['https://media.tenor.com/ye189ndlDpkAAAAM/patrick-sebastien-bravo.gif','https://media.tenor.com/UAGeMI4qk54AAAAM/sardinha.gif','https://media.tenor.com/mxJCaasEDcQAAAAM/pokemon-chammal.gif','https://media.tenor.com/nCCiMfXAAssAAAAM/tpmp-touche-pas-a-mon-poste.gif','https://tenor.com/view/car-fail-mechanic-ouch-alarm-gif-12178274','https://tenor.com/view/viralhog-fire-towing-hot-ride-flaming-gif-12840432']

@bot.slash_command(name="spot")
async def spot(ctx):
    try:
        embed = discord.Embed(
            description = '📷',
            color = discord.Color.from_rgb(16, 108, 138)
        )
        await ctx.respond("Spot en cours de chargement", ephemeral=True, delete_after=3)
        message = await ctx.channel.send(embed=embed)
        
        #if os.path.exists('spot.png'):
        #    os.remove("spot.png")
        
        driver.set_window_size(1200, 484) # set the window size that you need 
        driver.get('https://mylines.fr/luca/spot')
        driver.save_screenshot('spot.png')

        with open('spot.png', "rb") as fh:
            f = discord.File(fh, filename='spot.png')
        await ctx.send(file=f)

        await message.delete()
    #    os.remove("spot.png")
    except Exception as e:
        await printerror(e, ctx)
        
#en cas d'erreur
async def printerror(e, ctx):

    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

    embed = discord.Embed(
        description = ':red_circle: Quelque chose s\'est mal passé',
        color = discord.Color.from_rgb(215, 2, 2)
    )    
    #await ctx.channel.send(embed=embed)

@bot.listen() # Le listener comprend que tu vas écouter sur le on_message, et va executer la fonction à chaque message du tchat
async def on_message(message):
    if message.content == "quoi":
        await message.channel.respond("feur")
# démarrage
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="la version " + version))

@bot.slash_command(name="ping")
async def ping(ctx):
  await ctx.respond("Pong! 🏓")

# Fun
@bot.slash_command(name="pecresse", description = "Présidente de la Région Ile-de-France")
async def pecresse(ctx):
    embed = discord.Embed(
        title="Coucou tout le monde ! 👋",
        description="Vive le bleu, vive le camembert et vive la France ! Ah et bonne journée ;)",
        color=0x56B3E5, 
    )
    embed.set_author(name="Valérie Pécresse", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://img.20mn.fr/xBs4WR7oSAOc9bkYvGhEkyk/1200x768_valerie-pecresse-president-de-l-ile-de-france-aux-manettes-d-un-flambant-neuf-rer-ng")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name="gulag")
async def gulag(ctx, message: discord.Option(str)):
    embed = discord.Embed(
        title=message,
        description="Le gulag express, EN VOITUUUUURE !",
        color=0x56B3E5, 
    )
    embed.set_author(name="SNCF InfoTrafic", icon_url="https://cdn.discordapp.com/attachments/1044705168534556755/1046465897201672302/Design_sans_titre.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1034492018346446848/1043975164016209990/D1E_qGuXgAA0SQH.png")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name="bellebite")
async def bellebite(ctx):
    embed = discord.Embed(
        title="Belle bite 😏",
        description="",
        color=0x56B3E5, 
    )
    embed.set_author(name="prout", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://i.ibb.co/bFZXGGX/IMG-20221123-182001-HDR.jpg")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name="bonnenuit")
async def bonnenuit(ctx):
    embed = discord.Embed(
        title="Bonne nuit 💤",
        description="",
        color=0x56B3E5, 
    )
    embed.set_author(name="prout", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://media.tenor.com/s_O407o0_K0AAAAC/bonne-nuit-les-petits-good-night.gif")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name="bonappetit", description = "Citation préférée du Taupin en chef 🫡")
async def bonappetit(ctx):
    embed = discord.Embed(
        title="Qu'est-ce qu'on dit ? Bon appétit  ! 😋",
        description="",
        color=0x56B3E5, 
    )
    embed.set_author(name="prout", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://i.imgur.com/fxRfx31.gif")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name="chèvrests", description = "Nous entrons dans la zone défendue farouchement par les chèvres de la TS !")
async def chevres(ctx):
    embed = discord.Embed(
        title="Bienvenue au Paradis des Chèvres !",
        description="",
        color=0x56B3E5, 
    )
    embed.set_author(name="prout", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://i.imgur.com/PqClXEo.gif")
    await ctx.respond(embed=embed)

@bot.slash_command(name="pissepartout", description = "Oups j'ai fait pipi sur le 3ème rail 🥴")
async def chevres(ctx):
    embed = discord.Embed(
        title="",
        description="",
        color=0x56B3E5, 
    )
    embed.set_author(name="prout", icon_url="https://images-ext-1.discordapp.net/external/PMCR648tV3gBBKB_mNbEGIXj1XKIXFdYVKmJbGLzKbg/https/i.imgur.com/f8wFfNZ.png")
    embed.set_image(url="https://i.imgur.com/nrMZwCS.gif")
    await ctx.respond("J'ai trouvé le cousin de passe-partout ! Mr Pissepartout 😝",embed=embed)

@bot.slash_command(name="roue_retard", description = "Viens tirer la roue des retards")
async def retard(ctx):
    motif = choice(liste)
    embed = discord.Embed(
        title=motif,
        description="",
        color=0x56B3E5, # Pycord provides a class with default colors you can choose from
    )
    embed.set_author(name="InfoTrafic", icon_url="https://s1.qwant.com/thumbr/0x380/0/4/65d60ed76e4207f30e016b11b6997fb6b2c49cc09f2b651e65677889546dbc/CaptureII.jpg?u=https%3A%2F%2Fmalignep.transilien.com%2Fwp-content%2Fuploads%2F2014%2F10%2FCaptureII.jpg&q=0&b=1&p=0&a=0")
    embed.set_image(url="https://i.ibb.co/m4g6m7G/roueretard.gif")
    await ctx.respond(embed=embed) # respond the embed with some text

@bot.slash_command(name = "alex", description = "Hummm")
async def alex(ctx):
    embed = discord.Embed(
        title="Bah c'est pas bien toussa",
        description="",
        color=0xAB0013, # Pycord provides a class with default colors you can choose from
    )
    embed.set_author(name="Alex237", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0")
    embed.set_image(url="https://images-ext-1.discordapp.net/external/yCo1Xxhi3aGZ7Ve6_HfJyfgLSF-OIqJzbHC5_MzRZ4M/https/i.imgur.com/QzkJOVa.png")
    await ctx.respond("", embed=embed)

@bot.slash_command(name = "alex2", description = "Hummm")
async def alex2(ctx):
    embed = discord.Embed(
        title="Bah c'est pas bien toussa",
        description="",
        color=0xAB0013, # Pycord provides a class with default colors you can choose from
    )
    embed.set_author(name="Alex237", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0")
    embed.set_image(url=choice(listealex))
    await ctx.respond("", embed=embed) # Send the embed with some text

@bot.slash_command(name="say")
async def say(ctx, message: discord.Option(str)):
    await ctx.respond(message)

@bot.command(name='hello')
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.author.name}!")

@bot.slash_command(name="compliment")  # create a user command for the supplied guilds
async def compliment(ctx, nom: discord.Option(str)):  # user commands return the member
    await ctx.respond(f"{nom} tu es le meilleur ♥")

@bot.slash_command(name="accountcreationdate")  # create a user command for the supplied guilds
async def account_creation_date(ctx, member: discord.Member):
  # user commands return the member
    await ctx.respond(f"{member.name}'s account was created on {member.created_at}")

@bot.slash_command(name="add")
async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
  # you can use them as they were actual integers
  sum = first + second
  await ctx.respond(f"The sum of {first} and {second} is {sum}.")

class vertm(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Verte", 
            color = discord.Color.from_rgb(0,174,88))
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038565884404432917/1051859881319206912/Video_sans_titre_Realisee_avec_Clipchamp_1.gif")
        await bot.get_channel(int(1038565884404432917)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class jaunem(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Jaune", 
            color = discord.Color.from_rgb(233,236,107))
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038565884404432917/1051859881319206912/Video_sans_titre_Realisee_avec_Clipchamp_1.gif")
        await bot.get_channel(int(1038565884404432917)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class orangem(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Orange", 
            color = discord.Color.from_rgb(239,190,125))
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038565884404432917/1051859881319206912/Video_sans_titre_Realisee_avec_Clipchamp_1.gif")
        await bot.get_channel(int(1038565884404432917)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class rougem(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Rouge", 
            color = discord.Color.from_rgb(255,109,106))
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038565884404432917/1051859881319206912/Video_sans_titre_Realisee_avec_Clipchamp_1.gif")
        await bot.get_channel(int(1038565884404432917)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class météo(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Quel niveau d'alerte ?", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vert",
                description="Chef c'est calme ce soir !"
            ),
            discord.SelectOption(
                label="Jaune",
                description="Oh coquinou tu m'existe"
            ),
            discord.SelectOption(
                label="Orange",
                description="Sortez couvert !"
            ),
            discord.SelectOption(
                label="Rouge",
                description="Ouh Pinaise !"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        if select.values[0]=="Vert":
            modal = vertm(title="Crée le bulletin météo")
        if select.values[0]=="Jaune":
            modal = jaunem(title="Crée le bulletin météo")
        if select.values[0]=="Orange":
            modal = orangem(title="Crée le bulletin météo")
        if select.values[0]=="Rouge":
            modal = rougem(title="Crée le bulletin météo")
        await interaction.response.send_modal(modal)

class vertit(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Région concernée"))
        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Verte", 
            color = discord.Color.from_rgb(0,174,88))
        embed.add_field(name="Région(s) concernée(s)", value=self.children[0].value, inline=False)
        embed.add_field(name=self.children[1].value, value=self.children[2].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1035890029093978132/1053775889147633734/Video_sans_titre_Realisee_avec_Clipchamp_2.gif")
        await bot.get_channel(int(1035890029093978132)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class jauneit(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Région concernée"))
        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Jaune", 
            color = discord.Color.from_rgb(233,236,107))
        embed.add_field(name="Région(s) concernée(s)", value=self.children[0].value, inline=False)
        embed.add_field(name=self.children[1].value, value=self.children[2].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1035890029093978132/1053775889147633734/Video_sans_titre_Realisee_avec_Clipchamp_2.gif")
        await bot.get_channel(int(1035890029093978132)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class orangeit(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Région concernée"))
        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Orange", 
            color = discord.Color.from_rgb(239,190,125))
        embed.add_field(name="Région(s) concernée(s)", value=self.children[0].value, inline=False)
        embed.add_field(name=self.children[1].value, value=self.children[2].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1035890029093978132/1053775889147633734/Video_sans_titre_Realisee_avec_Clipchamp_2.gif")
        await bot.get_channel(int(1035890029093978132)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)

class rougeit(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Région concernée"))
        self.add_item(discord.ui.InputText(label="Titre de l'alerte"))
        self.add_item(discord.ui.InputText(label="Détail de l'alerte", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Alerte Rouge", 
            color = discord.Color.from_rgb(255,109,106))
        embed.add_field(name="Région(s) concernée(s)", value=self.children[0].value, inline=False)
        embed.add_field(name=self.children[1].value, value=self.children[2].value)
        embed.set_author(name="Alex&Amélie", icon_url="https://s2.qwant.com/thumbr/0x380/5/4/cba536a7e46cd2306fcf149f11574d79452dfcb824358fd855cacdcf0ffaf3/masque-singe-.jpg?u=https%3A%2F%2Fwww.ambiance-party.be%2Fwp-content%2Fuploads%2F2020%2F02%2Fmasque-singe-.jpg&q=0&b=1&p=0&a=0"),
        embed.set_image(url="https://cdn.discordapp.com/attachments/1035890029093978132/1053775889147633734/Video_sans_titre_Realisee_avec_Clipchamp_2.gif")
        await bot.get_channel(int(1035890029093978132)).send(embeds=[embed])
        await interaction.response.send_message("Modal envoyé ^^", ephemeral=True, delete_after=3)
        
@bot.slash_command(name="météo")
async def flavor(ctx):
    await ctx.respond("Quel niveau d'alerte ?", view=météo(), ephemeral=True, delete_after=5)

class infotrafic(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Quel niveau d'alerte ?", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vert",
                description="Chef c'est calme ce soir !"
            ),
            discord.SelectOption(
                label="Jaune",
                description="Oh coquinou tu m'existe"
            ),
            discord.SelectOption(
                label="Orange",
                description="Sortez couvert !"
            ),
            discord.SelectOption(
                label="Rouge",
                description="Ouh Pinaise !"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        if select.values[0]=="Vert":
            modal = vertit(title="Crée le bulletin Trafic")
        if select.values[0]=="Jaune":
            modal = jauneit(title="Crée le bulletin Trafic")
        if select.values[0]=="Orange":
            modal = orangeit(title="Crée le bulletin Trafic")
        if select.values[0]=="Rouge":
            modal = rougeit(title="Crée le bulletin Trafic")
        await interaction.response.send_modal(modal)

@bot.slash_command(name="infotrafic")
async def flavor(ctx):
    await ctx.respond("Quel niveau d'alerte ?", view=infotrafic(), ephemeral=True, delete_after=5)
    
@bot.slash_command(name="help")
async def help(ctx):
    embed=discord.Embed(title="Bonjour je suis Einstein, assistant de la direction du serveur ^^", description="Voici la liste des commandes disponibles")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1034442894121127978/ca3128ce8527b9ed527f5f37412a6147.png?size=256")
    embed.add_field(name="Un motif de retard ? ", value="</roue_retard:1046436215840321594>", inline=True)
    embed.add_field(name="Le comportement de ce modérateur est inadmissible", value="</alex:1046436215840321595>", inline=True)
    embed.add_field(name="En cas d'abus de gif, ici tu finira", value="</alex2:1046539059339743272>", inline=True)
    embed.add_field(name="Un joli poto", value="</bellebitte:1046436215840321589>", inline=True)
    embed.add_field(name="comme son nom l'indique, bonne nuit", value="</bonnenuit:1046436215840321590>", inline=True)
    embed.add_field(name="Qu'est'ce qu'on dit ?", value="</bonappetit:1046436215840321591>", inline=True)
    embed.add_field(name="Invasion de chèvres en cours", value="</chèvrests:1046436215840321592>", inline=True)
    embed.add_field(name="Tu sait que t'es le meilleur ? ♥", value="</compliment:1046436216066818129>", inline=True)
    embed.add_field(name="Road to the Gulag !", value="</gulag:1046436215840321588>", inline=True)
    embed.add_field(name="Oups j'ai oublié ma couche", value="</pissepartout:1046436215840321593>", inline=True)
    embed.add_field(name="Présidente de la Région Ile-de-France", value="</pecresse:1046436215840321587>", inline=True)
    embed.add_field(name="Message anonyme bonsoir", value="</say:1045103244638179351>", inline=True)
    embed.add_field(name="*ze veut voir des trains qui roulent !*", value="</spot:1046229853533388870>", inline=True)
    embed.add_field(name="oups le compteur est cassé :/ 🥴", value="</mute:1046229853814390867>", inline=True)
    embed.add_field(name="ALERTE MÉTÉO ! *A utiliser qu'en cas d'urgence, tout abus sera sanctionné*", value="</météo:1046544260222165074>", inline=True)
    await ctx.respond(embed=embed)

# Administration
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Ralph la casse 🧱🧱🧱🧱🧱🧱🧱",
                                            permissions = discord.Permissions(
                                                respond_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, respond_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Ralph la casse 🧱🧱🧱🧱🧱🧱🧱":
            return role
    
    return await createMutedRole(ctx)

@bot.slash_command(name="mute", description="Rendre muet un membre")
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.respond(f"{member.mention} a été mute pour {reason} !")

@bot.slash_command(name="unmute", description="Rendre muet un membre")
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.respond(f"{member.mention} a été unmute !")


@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.respond(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.respond(f"L'utilisateur {user} n'est pas dans la liste des bans")
@bot.event
async def on_message_delete(message):
    if message.channel.id == 1041660576180469852:
        await message.channel.send(f"Le message de {message.author} a été supprimé 🚨🚨🚨")

@bot.event
async def on_message_edit(before, after):
    if before.channel.id == 1041660576180469852:
        await before.channel.send(f"{before.author} a édité son message 🚨🚨🚨")

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.respond(f"{user} à été kick.")

@bot.slash_command(name="clear")
async def clear(ctx, nombre : int):
    messages = [msg async for msg in ctx.channel.history(limit = nombre)] 
    for message in messages:
        await message.delete()
    await ctx.respond(f'{nombre} message clear')
load_dotenv()
bot.run(os.getenv('TOKEN'))
