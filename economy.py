from discord.ext import commands
import csv
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ecowrite', aliases=['경제등록'])
    async def ecotest(self, ctx):
        user = ctx.message.author.name
        # 기존 사용자 기록 확인
        with open('test.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"{user}님은 이미 등록되어 있습니다.")
                    return
        # 사용자의 기록이 없을 경우 새로 작성
        with open('test.csv', 'a', encoding='utf-8', newline='') as file:
            csv_writter = csv.writer(file)
            csv_writter.writerow([user, 0])
        await ctx.send(f"test.csv에 '{user}', '0' 헤더를 작성했습니다.")

    @commands.command(name='bagwrite', aliases=['가방등록'])
    async def bag(self, ctx):
        user = ctx.message.author.name
        with open('bag.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"{user}님의 가방이 이미 등록되어 있습니다.")
                    return
        with open('bag.csv', 'a', encoding='utf-8', newline='') as file:
            csv_writter = csv.writer(file)
            csv_writter.writerow([user, 0, 0, 0, 0])
        await ctx.send(f"bag.csv에 '{user}','0','0','0','0' 헤더를 작성했습니다.")

    @commands.command(name='bag', aliases=['가방','ㄱㅂ','rq'])
    async def b_info(self, ctx):
        user = ctx.message.author.name
        with open('bag.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"🎒{user}님의 가방\n\n```ansi\n[0;31m឵⛏️하급 곡괭이 : {row[1]}\n[0;33m឵⛏️일반 곡괭이 : {row[2]}\n[0;32m឵⛏️고급 곡괭이 : {row[3]}\n[0;40;37m឵🪛'드릴' : {row[4]}```")
                    return
        await ctx.send(f"{user}님은 가방이 없다냥! 가방부터 만들라냥!")

    @commands.command(name='money', aliases=['돈','ㄷ', 'e'])
    async def money(self, ctx):
        user = ctx.message.author.name
        with open('test.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"🪙{user}님의 통장\n\n```ansi\n[0;32m឵보유중인 돈 : {row[1]}원```")
                    return  

    @commands.command(name='dobak', aliases=['도박','ㄷㅂ'])
    async def dobak(self, ctx, amount: str = None):  # 기본값을 None으로 설정
        if amount is None:
            await ctx.send("도박 금액을 입력해야 한다냥! 예: `.도박 1000`")
            return
        try:
            amount = int(amount)
        except ValueError:
            await ctx.send("금액은 숫자로 입력해야 한다냥! 예: `.도박 1000`")
            return
        if amount < 500:
            await ctx.send("도박은 최소 500원 이상부터 가능하다냥!")
            return
        user = ctx.message.author.name
        # 'test.csv' 파일을 읽기/쓰기(r+) 모드로 엽니다.
        with open('test.csv', 'r+', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)  # 모든 행을 리스트로 저장
            for i, row in enumerate(rows):
                if len(row) < 2:
                    continue
                if row[0] == user:  # 사용자의 이름이 있는 행을 찾음
                    current_money = int(row[1])  # 현재 금액을 정수로 변환
                    if current_money >= amount:  # 도박할 금액이 충분한지 확인
                        r = random.random()
                        if r <= 0.5:  # 50% 확률로 성공
                            new_money = amount * 2 + current_money  # 금액을 두 배로 증가
                            rows[i][1] = str(new_money)  # 증가된 금액을 문자열로 저장
                            await ctx.send(f"{user}님이 50% 확률로 도박에 성공했다냥! {amount}원이 두배가 되었다냥!\n{user}의 돈은 {new_money}원 있다냥!")
                        else:  # 실패
                            new_money = current_money - amount  # 금액 차감
                            rows[i][1] = str(new_money)  # 차감된 금액을 문자열로 저장
                            await ctx.send(f"{user}님이 50% 확률로 도박에 실패했다냥... {amount}원이 증발했다냥...\n{user}의 돈은 {new_money}원 있다냥...")
                        file.seek(0)  # 파일 포인터를 처음으로 이동
                        csv_writter = csv.writer(file)
                        # 전체를 새로 쓰기 모드로 저장
                        with open('test.csv', 'w', encoding='utf-8', newline='') as file:
                            csv_writer = csv.writer(file)
                            csv_writer.writerows(rows)# 변경된 내용을 파일에 씀  
                    else:
                        await ctx.send(f"{user}님은 도박할 돈이 부족합니다.")  # 금액 부족 안내
                    return
            await ctx.send(f"{user}님은 기록이 없다냥.")  # 사용자 기록이 없을 때

    