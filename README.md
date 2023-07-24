# Bloxflip-rain-notifier
> this branch is when you want to run the notifier 24/7 by using a hosting or for linux-based distributions (but this works perfect too for windows)

## Update v1.5.1:
- Updated API
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will notify you about the rain with some information about it
- This is ORIGINAL! It is not skidded, leaked, cracked, dumped e.t.c. (kinda sad i have to say this 😂)
- If you want to use it check license so you know your limits
- Virustotal for exe: https://www.virustotal.com/gui/file/95d94c0215df3d329533d5a27dd69f20499521a9b85838c3697301b1b8d90a55
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
  "windows_notification": true,
  "webhook_enabled": false,
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

### windows_notification:
If set to "true" then a popup on the bottom right on your screen will display showing you information about the current rain

Here is an example:

![unknown (2)](https://user-images.githubusercontent.com/79641603/161392482-74abad64-d724-466a-8c7a-2f6d87acf3c6.png)

### webhook_enabled:
Should be obvious but if you want the rain notifier to send a message to your discord webhook set it to "true"

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

![image](https://user-images.githubusercontent.com/79641603/236318484-31709ae8-0215-4c88-9e43-86d11a7f43aa.png)

## Current Issues:
- None
