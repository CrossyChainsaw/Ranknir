
# Setup Ranknir (ranknir-manual v1.1.1)
Would be nice if you credit this repository or me in any way :D
1. Go to [this page](https://discord.com/developers/applications) and create a discord bot
2. Add the bot to your server and make sure to give it the following permissions
![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/aa3afa90-f8d1-4f00-82ed-dabba8c7d0c8)

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/f7789492-e48c-439c-93d1-93ba8538fabf)
3. Click "Copy" to copy the url and paste it in browser to add the bot to your discord server

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/4049bb52-8d08-46eb-856a-400a2d8a25aa)

4. Download latest version of ranknir-manual [here](https://github.com/CrossyChainsaw/Ranknir/releases/download/manual-v1.1.1/ranknir.zip)
5. Unzip the zip and open `clan.json`
6. In `clan.json` change the variables to make them match your discord server and brawlhalla clan.

*clan.json*
```json
{
    "server_name": "YOUR_DISCORD_SERVER_NAME",
    "clan_names": ["YOUR_BRAWLHALLA_CLAN_CLAN"],
    "discord_server_id": "YOUR_DISCORD_SERVER_ID_YES_PUT_THE_ID_IN_A_STRING",
    "id_array": ["YOUR_BRAWLHALLA_CLAN_ID_THIS_IS_ALSO_A_STRING"],
    "color": "0x000000",
    "image": "https://i.sstatic.net/xJida.png",
    "channel_1v1_id": 1234567890123456789,
    "channel_2v2_id": 1234567890123456789,
    "channel_rotating_id": 1234567890123456789,
    "sorting_method": "peak",
    "show_member_count": true,
    "show_xp": false,
    "show_no_elo_players": false,
    "account_linkers": [],
    "console_players": [],
    "bot_token": "PUT_YOUR_BOT_TOKEN_HERE_DONT_SHARE_WITH_ANYONE"
}
```

7. Run ranknir.exe
