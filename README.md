# Bloxflip-rain-notifier

## Update v1.2:
- chromedriver.exe auto download
- Minimum rain amount
- Updated for exe as well :D

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will notify you about the rain with some information about it
- Virustotal for exe: https://www.virustotal.com/gui/file/bf231f423778368ef8ce506cdbd73292f14959a77362739b2b58017452e221a5
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program, either the exe or the python version.
2) Extract the files to a foler of your choice
3) Now run the **"installer.bat"** file and it should start running, now you can minimise the chrome browser and the program and do some work while waiting for a notification. 
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Latest config.json file:
```json
{
  "minimum_amount": 500,
  "headless": "False", 
  "windows_notification": "True",
  "webhook_enabled": "False",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx"
}
```
### minimum_amount:
Minimum rain amount intended for the program required to send you a notification. If you dont want this and want to be notified of all rains leave it at 500
Example: If you set it to 1000 it will only notify you of rains that are bigger then or equal to 1000 R$

### headless:
If set to "True" the chrome browser that the program opens will be hidden so you wont have to see it or accidentally open it.
#### However: if the program shows an error it is recommended to set this value to False

### windows_notification:
If set to "True" then a popup on the bottom right on your screen will display showing you information about the current rain

Here is an example:

![unknown (2)](https://user-images.githubusercontent.com/79641603/161392482-74abad64-d724-466a-8c7a-2f6d87acf3c6.png)

### webhook_enabled:
Should be obvious but if you want the rain notifier to send a message to your discord webhook set it to "True"

### webhook:
If you set webhook_enabled to "True" input your webhook into here to it can actually send it to you

Example of webhook:

![image](https://user-images.githubusercontent.com/79641603/161392598-616dda5d-adb5-4ff4-9b60-d46ea8581128.png)

Yes it does ping @everyone however you can change this in line 17

## Current Issues:
- ~~Chromedriver headless mode currently does not work with this program~~
- Currently cannot use requests due to bloxflip blocking requests
