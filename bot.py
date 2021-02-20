import discord
import os
import io
import requests
from discord.ext import commands
from dotenv import load_dotenv  # для загрузки .env


load_dotenv('.env')  # загрузка .env файла
TOKEN = os.getenv('TOKEN')  # обьявление токен из .env файла
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('Зарегестрировался, имя - {0.user}'.format(bot))  # если вкл, то пишет в консоль


@bot.event
async def on_message(message):
    if message.author == bot.user:  # если сообщение от юзера, то
        return

    if message.content.startswith('Привет'):  # если сообщение привет, то в ответ получаешь привет
        await message.channel.send('Приветствую!')


@bot.command()
async def reg(ctx): 
    await ctx.author.send('Для регистраци введите свое имя и пароль')



if __name__ == "__main__":
    bot.run(TOKEN)
