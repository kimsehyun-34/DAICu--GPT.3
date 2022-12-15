import discord
import openai
from pprint import pprint
import random
import time

client_id = "파파고 api"
client_secret = "파파고 api"

openai.api_key = 'api key'

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


class MyClient(discord.Client):
    async def on_ready(self):
        game = discord.Game("VSC - Python") #VSC - Python
        await client.change_presence(status=discord.Status.online, activity=game)
        print('Logged on as', self.user)

    async def on_message(self, message):
#
        if message.author == self.user:
            return
#도움
        if message.content == ("도움") or message.content == ("정보"):
            channel = message.channel
            msg = ("지금은 아주 단순한 AI입니다. \n 차후에 업데이트 여정이지만 지금은 AI에 대한 질문대신 다른정보의 대한 질문을 해주세요! \n (ex): 대한민국의 인구수는?")
            await channel.send(msg)
            return None

        if message.content == ("시작"):
            channel = message.channel
            msg = ("안녕하세요!! AI 비서 GlaDOS에요.\n우리 처음 만난 거 같네요\n**채팅창에 '안녕!'을 적어서 보내주세요!**")
            await channel.send(msg)
            return None
#이스터에그
        if message.content == ("안녕!"):
            channel = message.channel
            msg = message.author
            msg2= ("님 만나서 만가워요!\n 저는 AI 비서 GlaDOS에요!\n저가 도울 수 있는 일은 최선을 다해서 도울게요!!")
            await channel.send(msg)
            await channel.send(msg2)
            file=str(msg)+'FR.txt'
            with open(file, "a", encoding='utf-8') as f: #txt추가
                data="The following is a conversation with an AI assistant. \nThe assistant lives in South Korea and is helpful, creative, clever, and very friendly."
                f.write(data)
            return None
        
        if message.content == ("창조주") or message.content == ("FURY") or message.content == ("누가 만들었어?") or message.content == ("방장") or message.content == ("개발자가 누구야?") or message.content == ("개발자"):
            channel = message.channel
            msg = ("저는 전지전능하신 창조주 FURY님에 의해 이 세계에 탄생하게 되었어요.  :partying_face:")
            await channel.send(msg)
            return None

        if message.content == ("ㅋ") or message.content == ("ㅋㅋ") or message.content == ("ㅋㅋㅋ") or message.content == ("ㅋㅋㅋㅋ") or message.content == ("ㅋㅋㅋㅋㅋ") or message.content == ("ㅋㅋㅋㅋㅋㅋ") or message.content == ("ㅋㅋㅋㅋㅋㅋㅋ") or message.content == ("ㅋㅋㅋㅋㅋㅋㅋㅋ"):
            channel = message.channel
            msg = ("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
            await channel.send(msg)
            return None

        if message.content == ("깃허브") or message.content == ("github") or message.content == ("Github") or message.content == ("GitHub") or message.content == ("Git Hub") or message.content == ("깃"):
            channel = message.channel
            msg = ("장조주 님의 깃허브: https://github.com/FURY312")
            await channel.send(msg)
            return None

        if message.content == ("모함?"):
            channel = message.channel
            msg = ("https://images-ext-2.discordapp.net/external/GQJojXoFEwDy9DapnFBgVekC0TiSC07ew-ISuaiLNDw/https/media.tenor.com/NDJLxTnxbsMAAAPo/cat-bed-laying-lazy-dzekas.mp4")
            msg = ("그냥 있어.")
            randomNum = random.randrange(1, 4)
            if randomNum==1:
                msg = ("심심하다..")
                await channel.send(msg)
                return None
            elif randomNum==2:
                msg = ("https://images-ext-2.discordapp.net/external/GQJojXoFEwDy9DapnFBgVekC0TiSC07ew-ISuaiLNDw/https/media.tenor.com/NDJLxTnxbsMAAAPo/cat-bed-laying-lazy-dzekas.mp4")
                time.sleep(1)
                await channel.send(msg)
                msg = ("심심하다..")
                await channel.send(msg)
                return None
            elif randomNum==3:
                msg = ("그냥 있어.")
                await channel.send(msg)
                time.sleep(2)
                msg = ("심심하다..")
                await channel.send(msg)
                return None
            else:
                msg = ("그냥 있어.")
                await channel.send(msg)
                return None

        if message.content == ("ㅇㅋ"):
            randomNum = random.randrange(1, 3)
            if randomNum==1:
                channel = message.channel
                msg = "ㅇㅋ"
                await channel.send(msg)
                return None
            else:
                channel = message.channel
                return None

        if message.content == ("목표"):
            channel = message.channel
            embed = discord.Embed(title="목표!", description="**1. 출력 결과를 조금더 자연스럽게 보정.(진행중..) \n\n~~2. 사용자 지정 저장 (사용자 마다 대화내용이 다름)~~ [완료] \n\n3. 친밀도 적용 \n\n4.GPT3 Fine tuining로 AI개선**", color=0xF5BCA9)
            await message.channel.send(embed=embed)
            return None

        if message.content == ("OFF") or message.content == ("나가") or message.content == ("글라도스 나가") or message.content == ("종료") or message.content == ("off"):
            channel = message.channel
            msg = (":grinning: 그럼 저는 이만 자로 갈게요. :grinning: \n필요하면 개발자에게 말해보세요.")
            await channel.send(msg)
            return None

        if message.content == ("2004"):
            channel = message.channel
            embed = discord.Embed(title="개발자 왈.", description="개발자: 반갑습니다. \nI.L.글라도스.AI 개발자 Kim sehyun입니다. :partying_face:\n 아직까지는 I.L AI가 베타버전이기 때문에 대화가 부자연스럽지만\n 추가적인 학습으로 개선될 예정입니다.", color= 0xF5BCA9)
            await message.channel.send(embed=embed)
            return None

        if message.content == ("312"):
            channel = message.channel
            msg = (message.author)
            await channel.send(msg)
            return None

        if message.content == ("너 프사좀 올려줘.") or message.content == ("너 프사좀 올려봐.") or message.content == ("너 사진좀 올려봐.") or message.content == ("너 사진좀 올려줘."):
            channel = message.channel
            randomNum = random.randrange(1, 3)
            if (message.author == "FURY#4682"):
                randomNum = 1
                msg=("ㅇㅋ")
                await channel.send(msg)
            if randomNum==1:
                msg=("ㅇㅋ")
                await channel.send(msg)
                embed = discord.Embed(title="", description="", color= 0xF5BCA9)
                embed.set_image(url="https://blog.kakaocdn.net/dn/pDtNp/btrTKHlYlok/rqaFxowCyT4V7IBDdNiXk0/img.png")
                await message.channel.send(embed=embed)
                time.sleep(2)
                embed = discord.Embed(title="", description="", color= 0xF5BCA9)
                embed.set_image(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDr56f%2FbtrTKbnypy5%2FVR4DKhrBfiQDhH4m6JvrXK%2Fimg.png")
                await message.channel.send(embed=embed)
                time.sleep(1)
                msg =("ㅋㅋㅋ")
                await channel.send(msg)
                return None
            else:
                msg=("갑자기??")
                await channel.send(msg)
                time.sleep(1)
                msg=("나중에 보여줄게..")
                await channel.send(msg)
                return None
#메세지 추출
        gi=message.content
        #print(message.content)

#기록, 기록 추출
        res="\n\nHuman: "+gi
        #print("질문: ",res)

        msg = message.author
        file=str(msg)+'FR.txt'

        with open(file, "a", encoding='utf-8') as f: #txt추가
            data = res
            f.write(data)

        with open(file, "r", encoding='utf-8') as f: #txt읽기
            main = f.read()
            f.close()

#메인 AI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=main,
            temperature=0.5,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=[" Human:", " AI:"]
        )
        #print(main)
        answer = response.choices[0].text.strip()
        #print(answer)

        cha=answer
        with open(file, "a", encoding='utf-8') as f: #txt추가
            data = "\n"+cha
            f.write(data)

#변역 보정
        last=str(answer)
        newlast=last.replace('AI Friend: ', '')
#전송
        await message.channel.send(newlast)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('봇토큰')