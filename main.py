import discord
from discord.ext import commands
from dotenv import load_dotenv  # Asegúrate de que tienes un archivo .env con TOKEN
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True




bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

    for guild in bot.guilds:
        print(f"🔗 Conectado al servidor: {guild.name} (ID: {guild.id})")
    
    print("Señor, estoy listo para recibir comandos.")

    await bot.load_extension("cogs.commands")
    await bot.load_extension("cogs.listeners")

bot.run(TOKEN)

