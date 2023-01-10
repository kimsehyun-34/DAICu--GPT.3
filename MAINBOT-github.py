import discord
import openai
from pprint import pprint
import urllib.request
import json
import random

client_id = "id" #파파고 api
client_secret = "secret" 

openai.api_key = 'openai api_key'

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


class MyClient(discord.Client):
    async def on_ready(self):
        game = discord.Game("VSC - Python")
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
#가입
        if message.content == ("안녕!"):
            channel = message.channel
            msg = message.author
            msg2= ("님 만나서 만가워요!\n 저는 AI 비서 GlaDOS에요!\n저가 도울 수 있는 일은 최선을 다해서 도울게요!!")
            await channel.send(msg)
            await channel.send(msg2)
            file=str(msg)+'.txt'
            with open(file, "a", encoding='utf-8') as f: #txt추가
                data="The following is a conversation with an AI assistant. \nThe assistant lives in South Korea and is helpful, creative, clever, and very friendly."
                f.write(data)
            return None
#이스터에그        
        if message.content == ("창조주") or message.content == ("FURY") or message.content == ("누가 만들었어?") or message.content == ("방장") or message.content == ("개발자가 누구야?") or message.content == ("개발자"):
            channel = message.channel
            msg = ("저는 전지전능하신 창조주 Mr.Kim 님에 의해 이 세계에 탄생하게 되었어요.  :partying_face:")
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
            msg = ("**`1. 출력 결과를 조금더 자연스럽게 보정.(진행중..) \n2. 사용자 저장 (사용자 마다 대화내용이 다름) \n3. GPT3 Fine tuining 을 사용하여 AI개선`**")
            await channel.send(msg)
            return None

        if message.content == ("OFF") or message.content == ("나가") or message.content == ("글라도스 나가") or message.content == ("종료") or message.content == ("off"):
            channel = message.channel
            msg = (":grinning: 그럼 저는 이만 자로 갈게요. :grinning: \n필요하면 개발자에게 말해보세요.")
            await channel.send(msg)
            return None

        if message.content == ("2004"):
            channel = message.channel
            msg = ("개발자: 반갑습니다. \nGLaDOS.글라도스.AI 개발자 Mr.Kim 입니다. :partying_face:\n 아직까지는 글라도스. AI가 베타버전이기 때문에 대화가 부자연스럽지만 추가적인 학습으로 개선될 예정입니다.")
            await channel.send(msg)
            return None
#메세지 추출
        gi=message.content
        print(message.content)
#변역 (한 -> 영)
        text = gi
        source = 'ko'
        target = 'en'
        
        encText = urllib.parse.quote(text)
        data = f'source={source}&target={target}&text=' + encText
        
        url = "https://openapi.naver.com/v1/papago/n2mt"
        client_id = "TsdFsYhmLDaNW1wMfqOq"
        client_secret = "NW7Dyo_iHY"
        
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        
        if rescode == 200:
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))
            result = decode['message']['result']['translatedText']
            print(result)
        else:
            print('Error Code:' + str(rescode))
#기록, 기록 추출
        res="\n\nHuman: "+result
        print("질문: ",res)

        msg = message.author
        file=str(msg)+'.txt'

        with open(file, "a", encoding='utf-8') as f: #txt추가
            data = res
            f.write(data)

        with open(file, "a", encoding='utf-8') as f: #txt읽기
            main = f.read()
            f.close()

#메인 AI
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=main,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print(main)
        print()
        answer = response.choices[0].text.strip()
        print(answer)

        cha=answer
        with open("list.txt", "a", encoding='utf-8') as f: #txt추가
            data = "\n"+cha
            f.write(data)

#변역 (영 -> 한)
        last=str(answer)
        newlast=last.replace('AI: ', '')
        print(newlast)
        text = newlast
        source = 'en'
        target = 'ko'
        
        encText = urllib.parse.quote(text)
        data = f'source={source}&target={target}&text=' + encText
        
        url = "https://openapi.naver.com/v1/papago/n2mt"
        client_id = "TsdFsYhmLDaNW1wMfqOq"
        client_secret = "NW7Dyo_iHY"
        
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        
        if rescode == 200:
            response_body = response.read()
            decode = json.loads(response_body.decode('utf-8'))
            result2 = decode['message']['result']['translatedText']
            print(result2)
        else:
            print('Error Code:' + str(rescode))
#변역 보정
        #P=str(위의 최종)
        #최종=P.replace('해요고 믿는다', '한다고 믿어요')
        
        z=str(result2)
        q=z.replace('나는', '저는')

        x=str(q)
        w=x.replace('한다', '해요')

        c=str(w)
        e=c.replace('있다', '있어요')

        v=str(e)
        r=v.replace('수 있다', '수 있어요')

        b=str(r)
        t=b.replace('입니다', '이에요')

        n=str(t)
        y=n.replace('이다', '이에요')

        m=str(y)
        u=m.replace('당신', '주인님')

        a=str(u)
        s=a.replace('아니', '아니요')

        f=str(s)
        d=f.replace('해요고 믿는다', '한다고 믿어요')

        g=str(d)
        h=g.replace('왔다', '왔어요')

        j=str(h)
        l=j.replace('아니요라', '아니라')

        k=str(l)
        i=k.replace('된다', '되요')

        o=str(i)
        p=o.replace('믿는다', '믿어요')
#전송
        await message.channel.send(u)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('디코 토큰')