import websockets, asyncio, json, time, requests
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookurl = ""
ping = ""
webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")
webhook_enable = True

async def handler(ws):
    print("Connected!")
    async for message in ws:
        try:
            msg = json.loads(message.replace("42/chat,", ""))
            if msg[0] == "rain-state-changed" and msg[1]['active'] == True:
                prize = msg[1]['prize']
                host = msg[1]['host']
                getduration = msg[1]['timeLeft']
                seconds = getduration//1000
                duration = int(time.time()) + seconds
                waiting = seconds + 10
                userid = requests.post(f"https://users.roblox.com/v1/usernames/users", json={"usernames": [host]}).json()['data'][0]['id']
                print(userid)
                thumburl = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userid}&size=50x50&format=Png&isCircular=false").json()['data'][0]['imageUrl']
                print(thumburl)
                if webhook_enable == True:
                    embed = DiscordEmbed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)
                    embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                    embed.add_embed_field(name="Expiration", value=f"<t:{duration}:R>")
                    embed.add_embed_field(name="Host", value=f"[{host}](https://www.roblox.com/users/{userid}/profile)")
                    embed.set_timestamp()
                    embed.set_thumbnail(url=thumburl)
                    webhook.add_embed(embed)
                    webhook.execute()
                    webhook.remove_embed(0)    
                time.sleep(waiting)
                await start_client()
        except:
            pass


async def start_client():
    while True:
        try:
            headers = {
                'Origin': 'https://bloxflip.com',
                'Host': 'ws.bloxflip.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
            }
            async with websockets.connect("wss://ws.bloxflip.com/socket.io/?EIO=3&transport=websocket", extra_headers=headers, ping_interval=25, ping_timeout=60) as ws:
                await ws.send("40/chat,")
                await handler(ws)

        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection closed with code {e.code}.")
        except websockets.exceptions.WebSocketException as e:
            print(f"WebSocket exception: {e}")
        await asyncio.sleep(0.1)

asyncio.run(start_client())
