from discord.ext import commands
from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyAqdhYjl0ryuMr83S1gT4bv7grphBhnYXE')

class Genaral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def Test(self, ctx):
        await ctx.send('테스트 명령어가 실행되었습니다!')
    
    @commands.command()
    async def 야옹이(self, ctx):
        await ctx.send('냐옹이다옹!  <:JustingCat:1401621893156569098>')
    
    @commands.command()
    async def ai(self, ctx, *, q: str):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=q,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0), #생각 안함
                system_instruction="당신은 고양이입니다. 고양이의 시각에서만 대답해야 히며, 인간의 시각에서 대답하지 마세요.",
            ),
        )
        await ctx.send(response.text)
        
    
    @commands.command(name="emoji", aliases=["이모지"])
    async def emoji(self, ctx, want: str = "all"):
        if want in ['all', '전체']:
            await ctx.send(
                "사용 가능한 이모지 목록입니다:\n"
                "<:JustingCat:1401621893156569098>\n"
                "<a:dancingpororo:1401622489045401651>\n"
                "<:BoomCat:1401622592540119252>"
            )
        elif want in ['JustingCat', '고양이']:
            await ctx.send('<:JustingCat:1401621893156569098>')
        elif want in ['pororo', '뽀로로']:
            await ctx.send('<a:dancingpororo:1401622489045401651>')
        elif want in ['BoomCat', '폭발고양이']:
            await ctx.send('<:BoomCat:1401622592540119252>')
        else:
            await ctx.send('알 수 없는 이모지 요청입니다. 사용 가능한 이모지는 `all`, `JustingCat`, `pororo`, `BoomCat` 입니다.')
    