# Bloxflip-rain-notifier

## Update v1.3.2:
- Fixed ping for rains 10k+ as mentioned in [issue 2](https://github.com/amprocode/Bloxflip-rain-notifier/issues/2)
- Fixed issue with pinging everyone and added some more detail to how to set pings. Thanks for bringing this up in [issue 1](https://github.com/amprocode/Bloxflip-rain-notifier/issues/1)
- Updated for exe as well :D

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will notify you about the rain with some information about it
- This is ORIGINAL! It is not skidded, leaked, cracked, dumped e.t.c. (kinda sad i have to say this 😂)
- If you want to use it check license so you know your limits
- Virustotal for exe: https://www.virustotal.com/gui/file/17076e38e472404234dae7e6db135c0b310fa216cc5f7bc5eecd5f9fa812038c
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program, either the exe or the python version.
2) Extract the files to a foler of your choice
3) Now run the **"installer.bat"** file and it should start running, now you can minimise the chrome browser and the program and do some work while waiting for a notification. 
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Default config.json file:
```json
{
  "minimum_amount": 500,
  "refresh_rate": 30,
  "headless": "False", 
  "windows_notification": "True",
  "webhook_enabled": "False",
  "webhook_ping": "<@1234567890987654>",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx"
}
```
### minimum_amount:
Minimum rain amount intended for the program required to send you a notification. If you dont want this and want to be notified of all rains leave it at 500

Example: If you set it to 1000 it will only notify you of rains that are bigger then or equal to 1000 R$

### refresh_rate:
How often you want it to check if there is a rain currently happening (in seconds)

⚠️ WARNING ⚠️
- Recommended to not go below 15 seconds because you dont want your potato PC to crash
- Experiment with this feature, see what works for you

### headless:
If set to "True" the chrome browser that the program opens will be hidden so you wont have to see it or accidentally open it.
#### However: if the program shows an error it is recommended to set this value to False

### windows_notification:
If set to "True" then a popup on the bottom right on your screen will display showing you information about the current rain

Here is an example:

![unknown (2)](https://user-images.githubusercontent.com/79641603/161392482-74abad64-d724-466a-8c7a-2f6d87acf3c6.png)

### webhook_enabled:
Should be obvious but if you want the rain notifier to send a message to your discord webhook set it to "True"

### webhook_ping:
You can now ping a role or user instead of @everyone. If you need help getting an ID im sure this will help:

https://youtu.be/KVLdpboY7bg

Setting up ping:

If you want to ping **@everyone** or **@here** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "@everyone",
```
If you want to ping a **user** make sure your webhook_ping setting looks something like this:
```
"webhook_ping": "<@747719812054253568>",
```
If you want to ping a **role** just put a **&** symbol infront of the numbers. It should look something like this:
```
"webhook_ping": "<@&690632567663575090>",
```

**Obviously these are examples, replace the numbers with your own**

### webhook:
If you set webhook_enabled to "True" input your webhook into here to it can actually send it to you

Example of webhook:

![image](https://user-images.githubusercontent.com/79641603/161392598-616dda5d-adb5-4ff4-9b60-d46ea8581128.png)

## Current Issues:
- ~~Chromedriver headless mode currently does not work with this program~~
- Currently cannot use requests due to bloxflip blocking requests