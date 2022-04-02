# Bloxflip-rain-notifier

## Information:
- When there is a rain at [bloxflip](https://bloxflip.com) this program will notify you about the rain with some information about it

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Installation:
- First download the latest version of the program, either the exe or the python version.
- Extract the files
- Find your current chrome version by clicking [here](chrome://settings/help) and it should upon up shwoing your current chrome version
- Get the latest version of chromedriver by clicking [here](https://chromedriver.chromium.org/downloads) and download the "chromedriver_win32.zip" file
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
- Headless mode currently does not work with this program :(
