import discord
from discord.ext import commands, tasks
import os
import random
from dotenv import load_dotenv
from spurk_ai import SpurkAI

# Load environment variables
load_dotenv()

# Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SPURK_USER_ID = int(os.getenv('SPURK_USER_ID', '0'))
RANDOM_REPLY_CHANCE = float(os.getenv('RANDOM_REPLY_CHANCE', '0.05'))
RANDOM_MESSAGE_INTERVAL = int(os.getenv('RANDOM_MESSAGE_INTERVAL', '600'))

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!spurk ', intents=intents, help_command=None)
spurk_ai = SpurkAI()

# Store channels where the bot is active for random messages
active_channels = []

@bot.event
async def on_ready():
    """Called when the bot is ready."""
    print(f'{bot.user} has connected to Discord!')
    print(f'Monitoring user ID: {SPURK_USER_ID}')
    print(f'Random reply chance: {RANDOM_REPLY_CHANCE * 100}%')
    print(f'Random message interval: {RANDOM_MESSAGE_INTERVAL}s')
    stats = spurk_ai.get_stats()
    print(f'Loaded training data: {stats}')
    
    # Start the random message task if interval is set
    if RANDOM_MESSAGE_INTERVAL > 0:
        send_random_messages.change_interval(seconds=RANDOM_MESSAGE_INTERVAL)
        send_random_messages.start()

@bot.event
async def on_message(message):
    """Called when a message is sent in any channel the bot can see."""
    # Don't respond to bot's own messages
    if message.author == bot.user:
        return
    
    # Track channels where there's activity for random messages
    if message.channel not in active_channels and not isinstance(message.channel, discord.DMChannel):
        active_channels.append(message.channel)
        # Keep only the last 10 active channels to avoid memory issues
        if len(active_channels) > 10:
            active_channels.pop(0)
    
    # Learn from Spurk's messages
    if message.author.id == SPURK_USER_ID:
        print(f"Learning from Spurk: {message.content[:50]}...")
        spurk_ai.learn_from_message(message.content)
    
    # Process commands first
    await bot.process_commands(message)
    
    # Respond when mentioned
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        response = spurk_ai.generate_response(message.content)
        await message.channel.send(response)
        return
    
    # Randomly reply to messages (excluding command messages)
    if not message.content.startswith('!spurk ') and random.random() < RANDOM_REPLY_CHANCE:
        # Only reply if we have enough training data
        if spurk_ai.get_stats()['total_messages'] >= 5:
            response = spurk_ai.generate_response(message.content)
            await message.channel.send(response)

@bot.command(name='talk')
async def talk(ctx):
    """Generate a response in Spurk's style."""
    response = spurk_ai.generate_response()
    await ctx.send(response)

@bot.command(name='stats')
async def stats(ctx):
    """Show training statistics."""
    stats = spurk_ai.get_stats()
    embed = discord.Embed(
        title="Spurk AI Statistics",
        description="Current training data stats",
        color=discord.Color.blue()
    )
    embed.add_field(name="Total Messages", value=stats['total_messages'], inline=True)
    embed.add_field(name="Unique Word Pairs", value=stats['unique_word_pairs'], inline=True)
    embed.add_field(name="Common Phrases", value=stats['common_phrases'], inline=True)
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_command(ctx):
    """Show help information."""
    embed = discord.Embed(
        title="Spurk AI Bot - Help",
        description="A bot that learns from Spurk/Oscar and mimics their style",
        color=discord.Color.green()
    )
    embed.add_field(
        name="How it works",
        value="The bot automatically learns from Spurk's messages and can generate responses in their style.",
        inline=False
    )
    embed.add_field(
        name="Commands",
        value=(
            "**!spurk talk** - Generate a random message in Spurk's style\n"
            "**!spurk stats** - Show training statistics\n"
            "**!spurk help** - Show this help message\n"
            "**@mention** - Mention the bot to get a response"
        ),
        inline=False
    )
    await ctx.send(embed=embed)

@tasks.loop(seconds=600)  # Default interval, will be changed in on_ready
async def send_random_messages():
    """Periodically send random messages to active channels."""
    if not active_channels:
        return
    
    # Only send if we have enough training data
    if spurk_ai.get_stats()['total_messages'] < 5:
        return
    
    # Pick a random active channel
    channel = random.choice(active_channels)
    
    try:
        response = spurk_ai.generate_response()
        await channel.send(response)
        print(f"Sent random message to {channel.name}: {response[:50]}...")
    except Exception as e:
        print(f"Error sending random message: {e}")

def main():
    """Main entry point."""
    if not DISCORD_TOKEN:
        print("ERROR: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your Discord bot token.")
        return
    
    if SPURK_USER_ID == 0:
        print("WARNING: SPURK_USER_ID not set in environment variables!")
        print("The bot will not learn from any user. Set SPURK_USER_ID to enable learning.")
    
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
