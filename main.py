import json

import time

import requests

from win10toast import ToastNotifier

from discord_webhook import DiscordWebhook, DiscordEmbed

import ctypes

import sched

ctypes.windll.kernel32.SetConsoleTitleW("Bloxflip Rain Notifier")

class BloxflipRainNotifier:

    def __init__(self, config_file):

        self.load_config(config_file)

        self.setup_webhook()

    def load_config(self, config_file):

        with open(config_file, "r") as config:

            config_data = json.load(config)

        

        self.webhook_enable = config_data['webhook_enabled']

        self.webhookurl = config_data['webhook']

        self.winnotif = config_data['windows_notification']

        self.minimum = config_data['minimum_amount']

        self.ping = config_data['webhook_ping']

        self.refresh = config_data['refresh_rate']

    def setup_webhook(self):

        if self.webhook_enable:

            self.webhook = DiscordWebhook(url=self.webhookurl, content=self.ping)

    def run(self):

        self.scheduler = sched.scheduler(time.time, time.sleep)

        self.scheduler.enter(0, 1, self.check_rain)

        self.scheduler.run()

    def check_rain(self):

        try:

            response = requests.get('https://rest-bf.blox.land/chat/history')

            r = response.json()

            check = r['rain']

            if check['active']:

                if check['prize'] >= self.minimum:

                    prize = str(check['prize'])[:-2]

                    host = check['host']

                    getduration = check['duration']

                    created = check['created']

                    umduration = getduration + created

                    eduration = umduration / 1000

                    duration = round(eduration)

                    convert = (getduration / (1000 * 60)) % 60

                    waiting = (convert * 60 + 10)

                    sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))

                    print(f"Bloxflip Rain!\nRain amount: {prize} R$\nExpiration: {duration} minutes\nHost: {host}\nTimestamp: {sent}\n\n")

                    userid = requests.post(f"https://users.roblox.com/v1/usernames/users", json={"usernames": [host]}).json()['data'][0]['id']

                    thumburl = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userid}&size=50x50&format=Png&isCircular=false").json()['data'][0]['imageUrl']

                    if self.webhook_enable:

                        embed = DiscordEmbed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)

                        embed.add_embed_field(name="Rain Amount", value=f"{prize} R$")

                        embed.add_embed_field(name="Expiration", value=f"<t:{duration}:R>")

                        embed.add_embed_field(name="Host", value=f"[{host}](https://www.roblox.com/users/{userid}/profile)")

                        embed.set_timestamp()

                        embed.set_thumbnail(url=thumburl)

                        self.webhook.add_embed(embed)

                        self.webhook.execute()

                        self.webhook.remove_embed(0)

                else:

                    time.sleep(130)

                if self.winnotif:

                    toast = ToastNotifier()

                    toast.show_toast("Bloxflip Rain!", f"Rain amount: {prize} R$\nExpiration: {convert} minutes\nHost: {host}\n\n", icon_path="logo.ico", duration=10)

                    time.sleep(waiting)

            elif not check['active']:

                time.sleep(self.refresh)

        except Exception as e:

            print(e)

            time.sleep(self.refresh)

if __name__ == '__main__':

    notifier = BloxflipRainNotifier("config.json")

    notifier.run()
