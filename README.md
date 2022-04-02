# Bloxflip-rain-notifier

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will notify you about the rain with some information about it
- Virustotal for exe: https://www.virustotal.com/gui/file/5c9708bb6130c3b2d190fb96e9a9bcce95bf900882fc0d675b6cdec9d414fe18
- If you dont trust it, its literally open source

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program, either the exe or the python version.
2) Extract the files to a foler of your choice
3) Find your current chrome version by 
going here: **chrome://settings/help** and it should upon up shwoing your current chrome version like this:

![image](https://user-images.githubusercontent.com/79641603/161394661-f7d055ab-e5b7-4f83-b096-6956f39a3728.png)


4) Get your current chrome version of chromedriver by clicking [here](https://chromedriver.chromium.org/downloads) and download the chromedriver version that corresponds with your current chrome version and download the **"chromedriver_win32.zip"** file
5) Next extract the chromedriver folder and you should be left with a chromedriver.exe file. Copy and paste this file into the folder where you extraced the other files earlier in step 2
6) Now run the **"installer.bat"** file and it should start running, now you can minimise the chrome browser and the program and do some work while waiting for a notification. 
- Any problems open up a new issue on this github respitory!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Latest config.json file:
```json
{
  "windows_notification": "True",
  "webhook_enabled": "False",
  "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx"
}
```

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
- Chromedriver headless mode currently does not work with this program
- Currently cannot use requests due to cloudflare being a pain
