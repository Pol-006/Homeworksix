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
        await message.channel.send("Es un juego 5 contra 5 en la que ambos bandos buscan anotar la mayor cantidad de puntos posibles para ganar. En este juego existen 5 roles tecnicamente 6 pero el juego no lo dice son los siguientes: Ofensivo: fragil pero es el que es capaz de hacer más daño, Equilibrado: hace buen daño y es el que se mete en medio de la pelea ya que aguanta buenos golpes y puede proteger al ofensivo, Tanques: Son los que resisten los golpes y protege al ofensivo, Agil: entra hace daño y se va, puede cazar al ofensivo por su capacidad de saltar, Auxiliar de curación: cura a su equipo, Auxiliar de control: Controla stuneando al equipo enemigo ")
    elif message.content.startswith('$PokemonShowdown'):
        await message.channel.send("Un equpipo de 6 pokemons se enfrentaran a otro equipo de 6 en una batalla por turnos donde la tabla de tipos, habilidades, objetos, ataques fisicos ataques especiales y de estado, estadisticas del pokemon, naturalezas que potencian estadisticas, seran los datos que debes de considerar para crear un equipo ")
    elif message.content.startswith('$Roblox'):
        await message.channel.send("Juego que almacena juegos y minijuegos de todo tipo que comparten tu personaje creado y bailes ")
    elif message.content.startswith('$GTASanAndreas'):
        await message.channel.send("Eres un criminal que regresa a su barrio y se rencuentra con sus amigos pero 2 de estos lo traicionan. Tendras misiones como delincuente que ya tiene una banda muy grande como robar una casa, pelea de bandas, robarle al ejercito, perseguir a un tren con miembros de una banda enemiga para matarlos, huir en bicicleta de una carro con miembros de una banda enemiga")
    elif message.content.startswith('$¿QueHaces?'):
        await message.channel.send("Doy una reseña de los juegos que estan aqui: Ajedrez,Valorant,PokemonUnite,PokemonShowdown,Roblox,$GTASanAndreas")
    else:
        await message.channel.send(message.content)

client.run("MTI1MTkzMDM0NTcwODcxNjE1Mg.GcR-sz.LI_oI_8FToI6CviaGidKH3O1fR1fZeHuEvKN0Y")
