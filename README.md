# Setup Ranknir (ranknir-manual)
There are a few steps you need to take to setup Ranknir in your server
1. Go to [this page](https://discord.com/developers/applications) and create a discord bot
2. Add the bot to your server and make sure to give it the following commands
![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/aa3afa90-f8d1-4f00-82ed-dabba8c7d0c8)

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/f7789492-e48c-439c-93d1-93ba8538fabf)
3. Click "Copy" to copy the url and paste it in browser to add the bot to your discord server

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/4049bb52-8d08-46eb-856a-400a2d8a25aa)

4. Download latest version of ranknir-manual [here](https://github.com/CrossyChainsaw/Ranknir/archive/refs/heads/ranknir-manual.zip)
5. Unzip the zip and open `main.py`
6. In `main.py`, replace all the variables mentioned below `# Fill in with your own clan data!`
```py
# Fill in with your own clan data!
discord_server_name = "YOUR_DISCORD_SERVER_NAME"
discord_server_id = 'YOUR_DISCORD_SERVER_ID' # Yes this has to be a string
clan_name = ["YOUR_CLAN_NAME, YOUR_CLAN_NAME_2, YOUR_CLAN_NAME_3"]
channel_1v1_id=0 # Replace with your 1v1 elo channel id
channel_2v2_id=0 # Replace with your 2v2 elo channel id
clan_id = ["YOUR_CLAN_ID, YOUR_CLAN_ID_2, YOUR_CLAN_ID_3"]
clan_image = 'YOUR_CLAN_IMAGE_SOURCE_LINK'
discord_bot_token = "YOUR_BOT_TOKEN" # DON'T SHARE THIS TOKEN WITH ANYONE!!!!!!!!!!!!!!!!!!!!!!
```

7. Run main.py
8. run the `r!1`, `r!2` or `r12` command anywhere
