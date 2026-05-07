import discord
from discord.ext import commands
import pyttsx3

# CONFIGURAR VOZ
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# CONFIGURAR INTENTS
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# -----------------------------
# BIENVENIDA AUTOMÁTICA
# -----------------------------
@bot.event
async def on_member_join(member):

    canal = member.guild.system_channel

    mensaje = f"👋 ¡Bienvenido {member.mention}! Disfruta el servidor y aprende a reciclar ♻️"

    if canal:
        await canal.send(mensaje)

    # Voz LOCAL
    speak(f"Bienvenido {member.name}")

# -----------------------------
# BOT LISTO
# -----------------------------
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# -----------------------------
# COMANDO START
# -----------------------------
@bot.command()
async def start(ctx):

    mensaje = (
        "♻️ ¡Hola! Soy tu bot del reciclaje.\n\n"
        "Comandos disponibles:\n"
        "📄 !papel\n"
        "📦 !carton\n"
        "🔋 !pilas"
    )

    await ctx.send(mensaje)
    speak("Bienvenido, soy tu bot del reciclaje")

# -----------------------------
# COMANDO PAPEL
# -----------------------------
@bot.command()
async def papel(ctx):

    texto1 = (
        "📄 El papel se recicla colocándolo limpio y seco "
        "en el contenedor azul. Evita reciclar papel mojado "
        "o con grasa."
    )

    await ctx.send(texto1)
    speak(texto1)

# -----------------------------
# COMANDO CARTON
# -----------------------------
@bot.command()
async def carton(ctx):

    texto2 = (
        "📦 El carton debe doblarse antes de reciclarse. "
        "Debe estar limpio y sin restos de comida."
    )

    await ctx.send(texto2)
    speak(texto2)

# -----------------------------
# COMANDO PILAS
# -----------------------------
@bot.command()
async def pilas(ctx):

    texto3 = (
        "🔋 Las pilas nunca deben tirarse a la basura normal. "
        "Deben llevarse a centros de reciclaje especializados."
    )

    await ctx.send(texto3)
    speak(texto3)

# -----------------------------
# EJECUTAR BOT
# -----------------------------
bot.run("TOKEN")
