from datetime import datetime
import discord
from discord.ext import commands
from discord import Member
from discord.utils import get
import asyncio

client = commands.Bot(command_prefix = "/")


@client.event
async def on_ready():
    print('Time to Ban.')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def selfban(ctx, member: Member):
    role_get = get(discord.guild.Role, name = 'Banall')
    await member.remove_roles(role_get)
    
@client.command()
async def count(ctx, number:int):
    try:
        if number < 0:
            await ctx.send('number cant be a negative')
        elif number > 300:
            await ctx.send('number must be under 300')
        else:
            message = await ctx.send(number)
            while number != 0:
                number -= 1
                await message.edit(content=number)
                await asyncio.sleep(1)
            await message.edit(content='Ended!')
datetime.now
    except ValueError:
        await ctx.send('time was not a number')


@client.command(pass_context=True, name='status')
async def status(ctx, member: Member):
    await ctx.send(str(member.status))
    

client.run('BanAllBot')
