from discord.ext import commands
import discord

intents = discord.Intents.all()

discord_token = 'MTE4ODE1NTkxODQzNzg0NzA5Mg.GwhZ8-.5CXLQZyiq2I9c5U0TwV0rnl9Xz4etIVOuorSdw'
bot = commands.Bot(command_prefix="!", intents=intents)

# Define your label mapping dictionary
label_mapping = {
    'A': '4',
    'B': '13',
    'E': '3',
    'G': '6',
    'H': '#',
    'I': '1',
    'O': '0',
    'R': '12',
    'S': '5',
    'T': '+',
}

def encoder(txt):
    # Apply label mapping to each character in the text
    encoded_txt = ''.join(label_mapping.get(char.upper(), char.upper()) for char in txt)
    return encoded_txt

@bot.command()
async def encode(ctx):
    # Get the content of the message (excluding the command prefix)
    message_content = ctx.message.content[len(bot.command_prefix) + len("encode"):].strip()
    
    # Apply the encoder function
    encoded_txt = encoder(message_content)
    
    # Send the encoded text back to the channel
    await ctx.send("Encoded text: {}".format(encoded_txt))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_disconnect():
    print('Bot disconnected')

def run():
    bot.run(discord_token)

if __name__ == '__main__':
    run()
