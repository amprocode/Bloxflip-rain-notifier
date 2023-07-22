import cloudscraper
import json
import os
import requests
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from rich.console import Console
from win10toast import ToastNotifier
os.system(f'title Bloxflip Rain Notifier ^')
console = Console()
with open("config.json", "r") as config:
  config = json.load(config)
  config_keys: set[str] = {key for key in config}
  # check if all the keys required exists otherwise notify the user of it
  required_keys: set[str] = {
  "minimum_amount",
  "refresh_rate",
  "windows_notification",
  "webhook_enabled" ,
  "webhook_ping",
  "webhook"
  }
  missing = config_keys ^ required_keys  # getting the keys that are missing
  if len(missing) > 0:
      console.bell()
      console.print("Error some required keys are missing, the following keys are missing in the config.json file",
                    style='red')
      for missing_key in missing: console.print('\t'+missing_key, style='yellow')
      exit(-1)

webhook_enable: bool = config['webhook_enabled']
webhookurl: str = config['webhook']
winnotif = config['windows_notification']
minimum = config['minimum_amount']
if minimum < 0:
    console.bell()
    console.print("Error minimum can't be negative", style='red')
    console.print("Tip: By setting minimum to 0 will catch every rain", style='yellow italic')
    exit(-1)
ping = str(config['webhook_ping'])
if not ping.startswith('<@') and ping.isnumeric():
    ping = f'<@{ping}>'  # assuming ping is an integer in case as the user's ID
refresh = config['refresh_rate']
webhook: DiscordWebhook = None
if webhook_enable:  # verify if the webhook exists by sending a test message
  webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")
  try:
      if not webhookurl.startswith("https://discord.com/api/webhooks/"):
          raise ValueError
      with requests.post(webhookurl, json={
          'content': ping,
          'embeds': [
              {
                  'title': 'Ready',
                  'color': 0x00ff11,
                  'description': f'Ready to notify {ping} for rains!'
              }
          ]
      }) as response:
          if response.status_code != 204:
              raise ValueError
  except:
      console.bell()
      console.print("Error: webhook is incorrect/invalid", style='red')
      exit(-1)


toast = ToastNotifier()
console.print("Successfully started the rain notifier! Now go ahead, hide this tab", style='green')
while True:
    try:
        scraper = cloudscraper.create_scraper()
        r = scraper.get('https://api.bloxflip.com/chat/history').json()
        check = r['rain']
        if check['active'] is True:
            if check['prize'] >= minimum:
                grabprize = str(check['prize'])[:-2]
                prize = (format(int(grabprize),","))
                host = check['host']
                getduration = check['duration']
                created = check['created']
                umduration = getduration + created
                eduration = umduration/1000
                duration = round(eduration)
                convert = (getduration/(1000*60))%60
                waiting = (convert*60+10)
                sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
                print(f"Bloxflip Rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")
                userid = requests.post(f"https://users.roblox.com/v1/usernames/users", json={"usernames": [host]}).json()['data'][0]['id']
                thumburl = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userid}&size=50x50&format=Png&isCircular=false").json()['data'][0]['imageUrl']
                if webhook_enable:
                    embed = DiscordEmbed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)
                    embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
                    embed.add_embed_field(name="Expiration", value=f"<t:{duration}:R>")
                    embed.add_embed_field(name="Host", value=f"[{host}](https://www.roblox.com/users/{userid}/profile)")
                    embed.set_timestamp()
                    embed.set_thumbnail(url=thumburl)
                    webhook.add_embed(embed)
                    webhook.execute()
                    webhook.remove_embed(0)    
            else:
                time.sleep(130)
            if winnotif:
              toast.show_toast(
                  "Bloxflip Rain!", f"Rain amount: {prize} R$\nExpiration: {convert} minutes\nHost: {host}\n\n",
                               icon_path="logo.ico",
                               duration=10)
            time.sleep(waiting)
        elif not check['active']:
          time.sleep(refresh)
    except KeyboardInterrupt:
        console.print("exiting because of KeyboardInterrupt.. Bye bye!", style='yellow')
        break
    except Exception as e:
        console.bell()
        console.print("An error occured while listening for rains: ", e)
        time.sleep(refresh)
