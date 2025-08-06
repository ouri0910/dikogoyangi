from discord.ext import commands
import csv
import random
import asyncio

mineral = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

class mineing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='minewrite', aliases=['채광등록'])
    async def minecraft(self, ctx):
        user = ctx.message.author.name
        with open('mine.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"{user}님의 채광 기록이 이미 등록되어 있습니다.")
                    return
        with open('mine.csv', 'a', encoding='utf-8', newline='') as file:
            csv_writter = csv.writer(file)
            csv_writter.writerow([user, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        await ctx.send(f"mine.csv에 '{user}', '0'..., '0' 헤더를 작성했습니다.")

    @commands.command(name='mineral', aliases=['광물','ㄱㅁ', 'ra'])
    async def mineral(self, ctx):
        user = ctx.message.author.name
        with open('mine.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    await ctx.send(f"⛏️{user}님의 광물 정보\n\n```ansi\n[0;30m឵돌 : {row[1]}\n[0;30m឵석탄 : {row[2]}\n[0;37m឵철 : {row[3]}\n[0;37m឵은 : {row[4]}\n[0;33m឵금 : {row[5]}\n[0;35m឵크리스탈 : {row[6]}\n[0;31m឵루비 : {row[7]}\n[0;32m឵에메랄드 : {row[8]}\n[0;34m사파이어 : {row[9]}\n[0;36m឵다이아몬드 : {row[10]}\n[0;30m឵네더라이트 : {row[11]}\n[0;37;45m឵??? : {row[12]}```")
                    return
        await ctx.send(f"{user}님은 채광 기록이 없다냥!")

    @commands.command(name='shop', aliases=['상점', 'ㅅㅈ', 'sh'])
    async def sell(self, ctx, item: str = None):
        if item is None or item not in ['광물', '도구', 'mineral', 'tool', 'ㄱㅁ', 'ㄷㄱ', 'm', 't']:
            await ctx.send("팔거나 살 물건의 종류를 입력해야 한다냥! 예: `.상점 광물`")
            return
        if item in ['광물', 'mineral', 'ㄱㅁ', 'm']:
            await ctx.send(f"```ansi\n[1;37;40m឵이번주 광물 가격\n\n[0;30m឵돌 : {mineral[1]}원\n[0;30m឵석탄 : {mineral[2]}원\n[0;37m឵철 : {mineral[3]}원\n[0;37m឵은 : {mineral[4]}원\n[0;33m឵금 : {mineral[5]}원\n[0;35m឵크리스탈 : {mineral[6]}원\n[0;31m឵루비 : {mineral[7]}원\n[0;32m឵에메랄드 : {mineral[8]}원\n[0;34m사파이어 : {mineral[9]}원\n[0;36m឵다이아몬드 : {mineral[10]}원\n[0;30m឵네더라이트 : {mineral[11]}원\n[0;37;45m឵??? : {mineral[12]}원```")
            return
    
    @commands.command(name='buy', aliases=['구매','ㄱㅇ', 'b'])
    async def buy(self, ctx, item: str = None, amount: int = 1):
        user = ctx.message.author.name
        if item is None or item not in ['하급', '일반', '고급', '드릴', 'ㅎㄱ', 'ㅇㅂ', 'ㄱㄱ', 'ㄷㄹ', 'l', 'n', 'h', 'd']:
            await ctx.send("구매할 도구의 종류와 개수를 입력해야 한다냥! 예: `.구매 하급 1`")
            return
        if amount <= 0:
            await ctx.send("구매할 개수는 1개 이상이어야 한다냥!")
            return
        with open('test.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if len(row) < 2:
                    continue
                if row[0] == user:
                    money = int(row[1])
                    if item in ['하급', 'ㅎㄱ', 'l']:
                        cost = 25000 * amount
                        if money < cost:
                            await ctx.send(f"{user}님이 하급 곡괭이 {amount}개를 구매하려면 {cost}원이 필요하다냥! 돈을 벌어오라냥!")
                            return
                        if money >= cost:
                            await ctx.send(f"{user}님이 하급 곡괭이 {amount}개를 구매했다냥! {cost}원을 지불했다냥!")
                            row[1] = str(money - cost)
                            with open('test.csv', 'w', encoding='utf-8', newline='') as file:
                                csv_writer = csv.writer(file)
                                csv_writer.writerows(rows)
                            with open('bag.csv', 'r', encoding='utf-8') as bag_file:
                                bag_reader = csv.reader(bag_file)
                                bag_rows = list(bag_reader)
                                for bag_row in bag_rows:
                                    if len(bag_row) < 2:
                                        continue
                                    if bag_row[0] == user:
                                        bag_row[1] = str(int(bag_row[1]) + amount)
                                        break
                            with open('bag.csv', 'w', encoding='utf-8', newline='') as bag_file:
                                bag_writer = csv.writer(bag_file)
                                bag_writer.writerows(bag_rows)
                            break
                    if item in ['일반', 'ㅇㅂ', 'n']:
                        cost = 100000 * amount
                        if money < cost:
                            await ctx.send(f"{user}님이 일반 곡괭이 {amount}개를 구매하려면 {cost}원이 필요하다냥! 돈을 벌어오라냥!")
                            return
                        if money >= cost:
                            await ctx.send(f"{user}님이 일반 곡괭이 {amount}개를 구매했다냥! {cost}원을 지불했다냥!")
                            row[1] = str(money - cost)
                            with open('test.csv', 'w', encoding='utf-8', newline='') as file:
                                csv_writer = csv.writer(file)
                                csv_writer.writerows(rows)
                            with open('bag.csv', 'r', encoding='utf-8') as bag_file:
                                bag_reader = csv.reader(bag_file)
                                bag_rows = list(bag_reader)
                                for bag_row in bag_rows:
                                    if len(bag_row) < 3:
                                        continue
                                    if bag_row[0] == user:
                                        bag_row[2] = str(int(bag_row[2]) + amount)
                                        break
                            with open('bag.csv', 'w', encoding='utf-8', newline='') as bag_file:
                                bag_writer = csv.writer(bag_file)
                                bag_writer.writerows(bag_rows)
                            break
                    if item in ['고급', 'ㄱㄱ', 'h']:
                        cost = 250000 * amount
                        if money < cost:
                            await ctx.send(f"{user}님이 고급 곡괭이 {amount}개를 구매하려면 {cost}원이 필요하다냥! 돈을 벌어오라냥!")
                            return
                        if money >= cost:
                            await ctx.send(f"{user}님이 고급 곡괭이 {amount}개를 구매했다냥! {cost}원을 지불했다냥!")
                            row[1] = str(money - cost)
                            with open('test.csv', 'w', encoding='utf-8', newline='') as file:
                                csv_writer = csv.writer(file)
                                csv_writer.writerows(rows)
                            with open('bag.csv', 'r', encoding='utf-8') as bag_file:
                                bag_reader = csv.reader(bag_file)
                                bag_rows = list(bag_reader)
                                for bag_row in bag_rows:
                                    if len(bag_row) < 4:
                                        continue
                                    if bag_row[0] == user:
                                        bag_row[3] = str(int(bag_row[3]) + amount)
                                        break
                            with open('bag.csv', 'w', encoding='utf-8', newline='') as bag_file:
                                bag_writer = csv.writer(bag_file)
                                bag_writer.writerows(bag_rows)
                            break
                    if item in ['드릴', 'ㄷㄹ', 'd']:
                        cost = 1000000 * amount
                        if money < cost:
                            await ctx.send(f"{user}님이 드릴 {amount}개를 구매하려면 {cost}원이 필요하다냥! 돈을 벌어오라냥!")
                            return
                        if money >= cost:
                            await ctx.send(f"{user}님이 드릴 {amount}개를 구매했다냥! {cost}원을 지불했다냥!")
                            row[1] = str(money - cost)
                            with open('test.csv', 'w', encoding='utf-8', newline='') as file:
                                csv_writer = csv.writer(file)
                                csv_writer.writerows(rows)
                            with open('bag.csv', 'r', encoding='utf-8') as bag_file:
                                bag_reader = csv.reader(bag_file)
                                bag_rows = list(bag_reader)
                                for bag_row in bag_rows:
                                    if len(bag_row) < 5:
                                        continue
                                    if bag_row[0] == user:
                                        bag_row[4] = str(int(bag_row[4]) + amount)
                                        break
                            with open('bag.csv', 'w', encoding='utf-8', newline='') as bag_file:
                                bag_writer = csv.writer(bag_file)
                                bag_writer.writerows(bag_rows)
                            break

    @commands.command(name='mining', aliases=['채광','광질','ㄱㅈ','m'])
    async def mining(self, ctx, mine: str = None):
        user = ctx.message.author.name
        msg = await ctx.send(f"{user}님이 채광을 시작했다냥! 잠시 기다려라냥...")
        msg
        if mine is None or mine not in ['하급', '일반', '고급', '드릴', 'ㅎㄱ', 'ㅇㅂ', 'ㄱㄱ', 'ㄷㄹ', 'l', 'n', 'h', 'd']:
            await msg.edit(content="채광 도구를 선택해야 한다냥! 예: `.채광 하급`")
            return
        await asyncio.sleep(1)  # n초 대기
        with open('bag.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            for row in rows:
                if row[0] == user:
                    if mine == '하급' and int(row[1]) <= 0:
                        await msg.edit(f"{user}님은 하급 곡괭이가 없다냥!")
                        return
                    elif mine == '일반' and int(row[2]) <= 0:
                        await msg.edit(f"{user}님은 일반 곡괭이가 없다냥!")
                        return
                    elif mine == '고급' and int(row[3]) <= 0:
                        await msg.edit(f"{user}님은 고급 곡괭이가 없다냥!")
                        return
                    elif mine == '드릴' and int(row[4]) <= 0:
                        await msg.edit(f"{user}님은 드릴이 없다냥!")
                        return
                    break
        r = random.random()
        if mine in ['하급', 'ㅎㄱ', 'l']:
            if r <= 0.45:
                await msg.edit(content = f"{user}님이 하급 곡괭이로 채광에 성공했다냥! 돌을 얻었다냥!")
                # 돌을 얻었을 때
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 2:
                        continue
                    if row[0] == user:
                        row[1] = str(int(row[1]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.75 and r > 0.45:
                await msg.edit(content = f"{user}님이 하급 곡괭이로 채광에 성공했다냥! 석탄을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 3:
                        continue
                    if row[0] == user:
                        row[2] = str(int(row[2]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.9 and r > 0.75:
                await msg.edit(content = f"{user}님이 하급 곡괭이로 채광에 성공했다냥! 철을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 4:
                        continue
                    if row[0] == user:
                        row[3] = str(int(row[3]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.975 and r > 0.9:
                await msg.edit(content = f"{user}님이 하급 곡괭이로 채광에 성공했다냥! 은을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 5:
                        continue
                    if row[0] == user:
                        row[4] = str(int(row[4]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 1 and r > 0.975:
                await msg.edit(content = f"{user}님이 하급 곡괭이로 채광에 성공했다냥! 금을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 6:
                        continue
                    if row[0] == user:
                        row[5] = str(int(row[5]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            # 곡괭이 개수 1 감소 (성공/실패와 무관)
            with open('bag.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            for row in rows:
                if len(row) < 2:
                    continue
                if row[0] == user:
                    row[1] = str(max(0, int(row[1]) - 1))
                    break
            with open('bag.csv', 'w', encoding='utf-8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
            return
        if mine in ['일반', 'ㅇㅂ', 'n']:
            if r <= 0.30:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 석탄을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 3:
                        continue
                    if row[0] == user:
                        row[2] = str(int(row[2]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.60 and r > 0.30:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 철을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 4:
                        continue
                    if row[0] == user:
                        row[3] = str(int(row[3]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.80 and r > 0.60:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 은을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 5:
                        continue
                    if row[0] == user:
                        row[4] = str(int(row[4]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.90 and r > 0.80:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 금을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 6:
                        continue
                    if row[0] == user:
                        row[5] = str(int(row[5]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.975 and r > 0.90:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 크리스탈을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 7:
                        continue
                    if row[0] == user:
                        row[6] = str(int(row[6]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 1.00 and r > 0.975:
                await msg.edit(content = f"{user}님이 일반 곡괭이로 채광에 성공했다냥! 루비를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 8:
                        continue
                    if row[0] == user:
                        row[7] = str(int(row[7]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            # 곡괭이 개수 1 감소 (성공/실패와 무관)
            with open('bag.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            for row in rows:
                if len(row) < 3:
                    continue
                if row[0] == user:
                    row[2] = str(max(0, int(row[2]) - 1))
                    break
            with open('bag.csv', 'w', encoding='utf-8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
            return
        if mine in ['고급', 'ㄱㄱ', 'h']:
            if r <= 0.35:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 철을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 4:
                        continue
                    if row[0] == user:
                        row[3] = str(int(row[3]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.60 and r > 0.35:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 은을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 5:
                        continue
                    if row[0] == user:
                        row[4] = str(int(row[4]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.80 and r > 0.60:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 금을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 6:
                        continue
                    if row[0] == user:
                        row[5] = str(int(row[5]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.90 and r > 0.80:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 크리스탈을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 7:
                        continue
                    if row[0] == user:
                        row[6] = str(int(row[6]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.95 and r > 0.90:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 루비를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 8:
                        continue
                    if row[0] == user:
                        row[7] = str(int(row[7]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.98 and r > 0.95:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 에메랄드를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 9:
                        continue
                    if row[0] == user:
                        row[8] = str(int(row[8]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.9925 and r > 0.98:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 사파이어를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 10:
                        continue
                    if row[0] == user:
                        row[9] = str(int(row[9]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 1.00 and r > 0.9925:
                await msg.edit(content = f"{user}님이 고급 곡괭이로 채광에 성공했다냥! 다이아몬드를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 11:
                        continue
                    if row[0] == user:
                        row[10] = str(int(row[10]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            # 곡괭이 개수 1 감소 (성공/실패와 무관)
            with open('bag.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            for row in rows:
                if len(row) < 4:
                    continue
                if row[0] == user:
                    row[3] = str(max(0, int(row[3]) - 1))
                    break
            with open('bag.csv', 'w', encoding='utf-8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
        if mine in ['드릴', 'ㄷㄹ', 'd']:
            if r <= 0.45:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 크리스탈을 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 7:
                        continue
                    if row[0] == user:
                        row[6] = str(int(row[6]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.70 and r > 0.45:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 루비를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 8:
                        continue
                    if row[0] == user:
                        row[7] = str(int(row[7]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.85 and r > 0.70:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 에메랄드를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 9:
                        continue
                    if row[0] == user:
                        row[8] = str(int(row[8]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.929975 and r > 0.85:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 사파이어를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 10:
                        continue
                    if row[0] == user:
                        row[9] = str(int(row[9]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.970225 and r > 0.929975:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 다이아몬드를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 11:
                        continue
                    if row[0] == user:
                        row[10] = str(int(row[10]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 0.999975 and r > 0.970225:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! 네더라이트를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 12:
                        continue
                    if row[0] == user:
                        row[11] = str(int(row[11]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            if r <= 1.00 and r > 0.999975:
                await msg.edit(content = f"{user}님이 드릴로 채광에 성공했다냥! ???를 얻었다냥!")
                with open('mine.csv', 'r', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    rows = list(csv_reader)
                for row in rows:
                    if len(row) < 13:
                        continue
                    if row[0] == user:
                        row[12] = str(int(row[12]) + 1)
                        break
                with open('mine.csv', 'w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(rows)
            # 곡괭이 개수 1 감소 (성공/실패와 무관)
            with open('bag.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)
            for row in rows:
                if len(row) < 5:
                    continue
                if row[0] == user:
                    row[4] = str(max(0, int(row[4]) - 1))
                    break
            with open('bag.csv', 'w', encoding='utf-8', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)