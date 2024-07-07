import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Ajedrez'):
        await message.channel.send("Es un juegos en la que 16 piezas blancas se enfrentan a 16 piezas negras buscando ganar dando jaque mate o ganar por tiempo, pero aparte de ganar se puede empatar como con la regla de triple repeticion, rey ahogado, regla de las 50 jugadas, la regla de falta material")
    elif message.content.startswith('$Valorant'):
            await message.channel.send("Es un juego 5 contra 5 en el hay 2 bandos el atacante y el defensor, los atacantes buscan plantar una bomba y esperar que explote o matar a todos los defensores y los defensores buscan desactivar la bomba, matar a todos los atacantes sin plantar la bomba o que se acabe el tiempo ")
    elif message.content.startswith('$PokemonUnite'):
        await message.channel.send("Es un juego 5 contra 5 en la que ambos bandos buscan anotar la mayor cantidad de puntos posibles para ganar. En este juego existen 5 roles tecnicamente 6 pero el juego no lo dice son los siguientes: Ofensivo: fragil pero es el que es capaz de hacer más daño, Equilibrado: hace buen daño y es el que se mete en medio de la pelea ya que aguanta buenos golpes y puede proteger al ofensivo, Tanques: Son los que resisten los golpes y protege al ofensivo, Agil: entra hace daño y se va, puede cazar al ofensivo por su capacidad de saltar ")
    elif message.content.startswith('$PokemonShowdown'):
        await message.channel.send("Bye")
    elif message.content.startswith('$Roblox'):
        await message.channel.send("Bye")
    elif message.content.startswith('$DigimonRumble'):
        await message.channel.send("Bye")
    elif message.content.startswith('$¿QueHaces?'):
        await message.channel.send("Doy una reseña de los juegos que estan aqui: Ajedrez,Valorant,PokemonUnite,PokemonShowdown, Roblox, DigimonRumble")
    else:
        await message.channel.send(message.content)

client.run("MTI1MTkzMDM0NTcwODcxNjE1Mg.GcR-sz.LI_oI_8FToI6CviaGidKH3O1fR1fZeHuEvKN0Y")
