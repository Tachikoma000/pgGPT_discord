import nextcord as discord

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = discord.Bot(intents=intents)

@bot.slash_command(name="ping", description="Get the bot's latency")
async def ping(ctx):
    latency = bot.latency
    await ctx.respond(latency)

@bot.slash_command(name="echo", description="Echo back the input")
async def echo(ctx, content: discord.Option(str, "Content to echo")):
    await ctx.respond(content)

def get_bot():
    return bot
