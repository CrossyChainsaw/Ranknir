from Ranknir.classes.Server import Server
from Dadabase.modules.data_management import SERVERS_DATA_LOCATION


BRAWLHALLA_NL_SERVER_ID = 1047987261905584128
Brawlhalla_NL = Server(["Brawlhalla Nederland Leaderboard"],
                       channel_1v1_id=1050114658566152262,
                       channel_2v2_id=1075022495142400091,
                       id=BRAWLHALLA_NL_SERVER_ID,
                       color=0xff6404,
                       sorting_method="current",
                       data_location=f"{SERVERS_DATA_LOCATION}{BRAWLHALLA_NL_SERVER_ID}.json",
                       channel_rotating_id=1165780126508797953)

BRAWLHALLA_HUNGARY_SERVER_ID = 1209624739635531857
Brawlhalla_Hungary = Server(["Brawlhalla Hungary Leaderboard"],
                       channel_1v1_id=1209633413821108274,
                       channel_2v2_id=1226931575724179628,
                       id=BRAWLHALLA_HUNGARY_SERVER_ID,
                       color=0xc1253b,
                       sorting_method="current",
                       data_location=f"{SERVERS_DATA_LOCATION}{BRAWLHALLA_HUNGARY_SERVER_ID}.json")
TEST_SERVER_ID = 1047987261905584128
Test_Server = Server(["Test"],
                     channel_1v1_id=1048162813132152833,
                     channel_2v2_id=1131552899378466887,
                     id=1047987261905584128,
                     color=0xff6404,
                     sorting_method="current",
                     data_location=f"{SERVERS_DATA_LOCATION}{TEST_SERVER_ID}.json",
                     channel_rotating_id=1131552899378466887,
                     member_count="show")

M30W_SERVER_ID = 1076670210678992936
M30W = Server(name=["M30W Elo Leaderboard"],
              channel_1v1_id=1207380613380837416,
              channel_2v2_id=1207374159882223687,
              id=M30W_SERVER_ID,
              color=0xd6307a,
              sorting_method="peak",
              data_location=f"{SERVERS_DATA_LOCATION}{M30W_SERVER_ID}.json",
              image="https://media.discordapp.net/attachments/1110725749859688648/1207376677110415411/new_pink_yellow_m30w_header.png?ex=65df6c27&is=65ccf727&hm=6b5096a4a5706c225e7c67caa3c01e2c3ac5b2fbeb7b7c1cc5a30bcb3d43144a&=&format=webp&quality=lossless&width=1440&height=480",
              channel_rotating_id=1207374136188338258,
              member_count="show")
