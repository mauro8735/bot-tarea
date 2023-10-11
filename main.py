import discord

gato = discord.File(r'C:\Users\Usuario\Documents\MAURO\FILE\pitufo.mp4', 'pitufo.mp4')
from genpass import gen_pass
from gira_la_moneda import g_l_m
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
    #mensajes
    if message.content.startswith('-chao'):
        await message.channel.send("chao que estes bien")
    elif message.content.startswith('-me cago') or message.content.startswith('-me cago en todo'):  
        await message.delete() 
        await message.channel.send("no digas eso")
    elif message.content.startswith('-el chicle'):  
        await message.channel.send("un niño molestoso")
    elif message.content.startswith('-el papas'):  
        await message.channel.send("un niño ipercargado")
    elif message.content.startswith('-hola'):  
        await message.channel.send("hola como estas me llamo juanito")
    elif message.content.startswith('-como te llamas'):  
        await message.channel.send("juanito")
    elif message.content.startswith('-bien y tu') or message.content.startswith('-mal y tu'):  
        await message.channel.send("bien gracias")
    elif message.content.startswith('-gato pitufo'):  
        await message.channel.send(file = gato)
    #contraseña
    elif message.content.startswith('-contraseña'):
        await message.channel.send(gen_pass('password'))
    #girar la moneda
    elif message.content.startswith('-gira la moneda'):
        await message.channel.send(g_l_m())

 
client.run("")
