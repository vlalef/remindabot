import os
import discord
from discord import app_commands
import asyncio
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the bot's intents (default is sufficient for slash commands)
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def parse_time(time_str: str) -> int:
    """Converts a time string (e.g., 10s, 5m, 1h) into seconds."""
    unit = time_str[-1].lower()
    value_str = time_str[:-1]

    if not value_str.isdigit():
        raise ValueError("The time value must be a number.")
    
    value = int(value_str)

    if unit == 's':
        return value
    elif unit == 'm':
        return value * 60
    elif unit == 'h':
        return value * 3600
    else:
        raise ValueError("Invalid time unit. Please use 's' for seconds, 'm' for minutes, or 'h' for hours.")

@client.event
async def on_ready():
    """Event that runs when the bot is connected and ready."""
    await tree.sync()
    print(f'Logged in as {client.user}')
    print('ReminderBot is ready and commands have been synced.')

@tree.command(name="remind", description="Sets a quick reminder. Ex: /remind time:10m message:Call the client")
async def remind(interaction: discord.Interaction, time: str, message: str):
    """The main command to set a reminder."""
    try:
        seconds = parse_time(time)
    except ValueError as e:
        # Send an error message visible only to the user if the time format is invalid
        await interaction.response.send_message(f"Error in time format: {e}", ephemeral=True)
        return
    
    # Immediately confirm to the user that the command was received
    await interaction.response.send_message(f"Alright! I will remind you about '{message}' in {time}.")

    # Wait for the specified duration asynchronously (doesn't block the bot)
    await asyncio.sleep(seconds)

    # Send the reminder via Direct Message (DM)
    try:
        await interaction.user.send(f"🔔 **Reminder:** {message}")
    except discord.Forbidden:
        # This happens if the user has DMs disabled for server members
        print(f"Could not send a DM to user {interaction.user.name}")

# Start the bot
if TOKEN is None:
    print("ERROR: The DISCORD_TOKEN environment variable is not set.")
else:
    client.run(TOKEN)
