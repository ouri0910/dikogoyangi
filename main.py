import csv
import discord
from discord.ext import commands
import General
import economy
import mine

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents, status=discord.Status.idle, activity=discord.Game(name='새끼 고양이 돌보기'))

@bot.event
async def on_ready():
    c = bot.get_channel(1401589532989849712)
    if c:
       await c.send("## 고양이 봇이 온라인 상태입니다! <:BoomCat:1401622592540119252>")
    print('- 다음으로 로그인되었습니다.', bot.user.name, bot.user.id, sep='\n -')
    await bot.add_cog(General.Genaral(bot))
    await bot.add_cog(economy.Economy(bot))
    await bot.add_cog(mine.mineing(bot))

@bot.command(name='stop', aliases=['종료', '정지'])
async def stop(ctx):
    await ctx.send('봇이 종료됩니다.')
    await bot.close()

bot.run('')