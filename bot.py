import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import traceback
import sys

bot = commands.Bot(command_prefix=".voice", intents=discord.Intents.all())

bot.remove_command("help")

DISCORD_TOKEN = 'INSERT DISCORD TOKEN HERE'

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension '+extension, file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('\nBOOT INFORMATION:')
    print('Bot: ' + str(bot.user.name) + ' | ' + str(bot.user.id))
    print('------\n')
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Error: Command Not Found!")
        return
    raise error
bot.run(DISCORD_TOKEN)
