
# Setup Ranknir (ranknir-manual v1.2.3)
Would be nice if you credit this repository or me in any way :D
1. Go to [this page](https://discord.com/developers/applications) and create a discord bot (Would be cool if you credit Ranknir in the bot name or image :D)
2. Enable these 3 Intents for your bot
![image](https://github.com/user-attachments/assets/db0f8433-65d1-4fbe-a66f-82dbe4a4e2fd)
4. Add the bot to your server and make sure to give it the following permissions
![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/aa3afa90-f8d1-4f00-82ed-dabba8c7d0c8)

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/f7789492-e48c-439c-93d1-93ba8538fabf)
3. Click "Copy" to copy the url and paste it in browser to add the bot to your discord server

![image](https://github.com/CrossyChainsaw/Ranknir/assets/74303221/4049bb52-8d08-46eb-856a-400a2d8a25aa)

4. Download latest version of ranknir-manual [here](https://github.com/CrossyChainsaw/Ranknir/releases/download/manual-v1.1.1/ranknir.zip)
5. Unzip the zip and open `clan.json`
6. In `clan.json` change the variables to make them match your discord server and brawlhalla clan.

**💡 Note: In this example the clan is called `Eisen` and has a clan id of `833565`. Edit all the fields to match your clans'*

*clan.json*
```json
{
    "server_name": "EISEN",
    "clan_names": ["Eisen"],
    "discord_server_id": "705783420189671458",
    "id_array": ["833565"],
    "color": "0x000000",
    "image": "https://private-user-images.githubusercontent.com/74303221/383203281-4f4b49d1-9478-4ffd-adb0-8e4d6a16a5d8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYyOTA0MjQsIm5iZiI6MTczNjI5MDEyNCwicGF0aCI6Ii83NDMwMzIyMS8zODMyMDMyODEtNGY0YjQ5ZDEtOTQ3OC00ZmZkLWFkYjAtOGU0ZDZhMTZhNWQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTA3VDIyNDg0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM1YTY4MzRjNjk2MmZhMGRlNzMyZWJkMGIyYjQ1YmVlN2Y5N2E1YWMyMTI1ZmM2ZjM4OTgwMjNmOTU1MGQ2NWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.zan8WrmzqZDGzttpEh2w2Cob3WEqUpqUEWHvyh2NjIE",
    "channel_1v1_id": 1131552899378466887,
    "channel_2v2_id": 1131552899378466887,
    "channel_rotating_id": null,
    "sorting_method": "peak",
    "show_member_count": true,
    "show_xp": true,
    "show_no_elo_players": true,
    "show_win_loss": true,
    "show_1v1_legends": false,
    "show_2v2_legends": false,
    "show_average_elo": true,
    "account_linkers": [
        {
            "brawlhalla_id": "62051982",
            "brawlhalla_name": "Heartbleat (PC)"
        }
    ],
    "console_players": [
        {
            "brawlhalla_id": "12779207",
            "brawlhalla_name": "Heartbleat (PS4)"
        }
    ],
    "legends_for_2v2": [],
    "bot_token": "YOUR_BOT_TOKEN"
}
```

7. Run ranknir.exe
8. If this helped please leave a star on the repository ⭐
