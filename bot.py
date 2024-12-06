import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("MTMxNDY4Mjg4Mzc2MzQ3MDQxNw.G1a6Du.sDDDCedQIOiJ34tq__mdPYhhA3PYiue-DoHJQo")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.slash_command(description="Spam a phrase multiple times")
async def spam(
    interaction: nextcord.Interaction,
    phrase: str,
    count: int = 5,
    delay: float = 1.0
):
    """
    Spams a phrase multiple times.
    - phrase: The text to spam.
    - count: Number of times to repeat the phrase (default: 5, max: 20).
    - delay: Delay between messages in seconds (default: 1.0).
    """

    await interaction.response.send_message("Sending...", ephemeral=True)

    if count > 20:
        await interaction.followup.send("Please keep the spam count under 20.", ephemeral=True)
        return
    if delay < 0.1:
        await interaction.followup.send("Delay must be at least 0.1 seconds.", ephemeral=True)
        return

    for _ in range(count):
        await interaction.channel.send(phrase)
        await asyncio.sleep(delay)

    await interaction.followup.send("Spam completed!", ephemeral=True)

bot.run(TOKEN)
