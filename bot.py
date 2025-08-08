import os
import discord
from discord import app_commands
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def parse_time(time_str: str) -> int:
    """Converts a time string (e.g., 10s, 5m, 1h) into seconds."""
    unit = time_str[-1].lower()
    value_str = time_str[:-1]

    try:
        value = int(value_str)
    except ValueError:
        raise ValueError("The time value must be a number.")

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
        await interaction.response.send_message(f"Error in time format: {e}", ephemeral=True)
        return
    
    await interaction.response.send_message(f"Alright! I will remind you about '{message}' in {time}.")

    await asyncio.sleep(seconds)

    try:
        await interaction.user.send(f"🔔 **Reminder:** {message}")
    except discord.Forbidden:
        print(f"Could not send a DM to user {interaction.user.name}")
        await interaction.followup.send(
            "I couldn't send you a DM with your reminder. Please check your privacy settings or allow DMs from server members.",
            ephemeral=True
        )
if TOKEN is None:
    print("ERROR: The DISCORD_TOKEN environment variable is not set.")
else:
    client.run(TOKEN)
