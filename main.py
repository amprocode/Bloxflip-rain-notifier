import json, os, time, requests
from selenium import webdriver
from win10toast import ToastNotifier
from zipfile import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from discord_webhook import DiscordWebhook, DiscordEmbed

os.system(f'title Bloxflip Rain Notifier ^')

with open("config.json", "r") as config:
  config = json.load(config)

headless = config['headless']    
webhook_enable = config['webhook_enabled']
webhookurl = config['webhook']
winnotif = config['windows_notification']
minimum = config['minimum_amount']

if webhook_enable == "True":
  webhook = DiscordWebhook(url=webhookurl, content='@everyone')

if not os.path.exists("chromedriver.exe"):
  version = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
  download = requests.get(f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip")
  with open("chromedriver.zip", "wb") as zip:
    zip.write(download.content)

  with ZipFile("chromedriver.zip", "r") as zip:
    zip.extract("chromedriver.exe")
    zip.close()
    os.remove("chromedriver.zip")

toast = ToastNotifier()
options = Options()
if headless == "True":
  options.headless = True
options.add_argument("window-size=200,500")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
driver.implicitly_wait(10)

while True:
    try:
      driver.get('https://rest-bf.blox.land/chat/history')
      if headless == "False":
        driver.minimize_window()
      data = driver.page_source.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', "").replace("</pre></body></html>", "")
      check = json.loads(data)['rain']
      if check['active'] == True:
          if check['prize'] >= minimum:
            prize = str(check['prize'])[:-2]
            host = check['host']
            getduration = check['duration']
            convert = (getduration/(1000*60))%60
            duration = (int(convert))
            sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
            print(f"Bloxflip Rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")
            if webhook_enable == "True":
              userid = requests.get(f"https://api.roblox.com/users/get-by-username?username={host}").json()['Id']
              thumburl = (f"https://www.roblox.com/headshot-thumbnail/image?userId={userid}&height=50&width=50&format=png")
              embed = DiscordEmbed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)
              embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")
              embed.add_embed_field(name="Expiration", value=f"{duration} minutes")
              embed.add_embed_field(name="Host", value=f"[{host}](https://www.roblox.com/users/{userid}/profile)")
              embed.set_timestamp()
              embed.set_thumbnail(url=thumburl)
              webhook.add_embed(embed)
              webhook.execute()
              webhook.remove_embed(0)
          else:
            time.sleep(130)
          if winnotif == "True":
            toast.show_toast("Bloxflip Rain!", f"Rain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\n\n", icon_path="logo.ico", duration=10)
          time.sleep(130)
      elif check['active'] == False:
        time.sleep(30)
    except Exception as e:
      print(e)
      time.sleep(30)
