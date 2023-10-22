from classes.Clan import Clan

Skyward = Clan("Skyward",
               "NO ACCESS",
               976552050953437194, ['84648'],
               0x289fb4,
               'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png',
               '705783420189671458',
               no_elo_players='show')

lnsomnia_clan_id, Parasomnia_clan_id, Hypnosia_clan_id = '1919781', '1927502', '2022800'
lnsomnia = Clan('lsomnia',
                988484998799716423, 1006780905131614280,
                [lnsomnia_clan_id, Parasomnia_clan_id, Hypnosia_clan_id], 0x301834,
                "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png",
                '971836983951372298')

Pandation_clan_id, Pandace_clan_id, Panhalla_clan_id, PanhaIIa_clan_id = '1702413', '1868949', '1709279', '1722822'

Pandation = Clan('Pandation',
                 1164181564423426079, 1164181602243457125,
                 [Pandation_clan_id, Pandace_clan_id,
                     Panhalla_clan_id, PanhaIIa_clan_id],
                 0x212226,
                 "https://media.discordapp.net/attachments/958131738503155714/958141534455337031/standard.gif",
                 '889594104873377812', sorting_method='peak', channel_rotating_id=1164251976633159682)

Dair = Clan('Dair',
            "NO ACCESS", 1029669276363280414, ['1357965'], 0x349feb,
            'https://cdn.discordapp.com/attachments/994165604602880031/1024740143015399424/unknown.png',
            '793113149041147934')

Cybers_clan_id, Cybers_II_clan_id, Xybers_clan_id, Cybers_Academy = '1983079', '1983274', '2041304', '2072355'
Cybers = Clan('Cybers',
              1062818147608043640, 1062818053936644129,
              [Cybers_clan_id, Cybers_II_clan_id, Xybers_clan_id, Cybers_Academy],
              0xD10000, " ", '1005510941590437959')

Cherimoya = Clan('Cherimoya', 1042189651118674010, "N/A", ['2024340'], 0x19eb8f, " ",
                 '1032624646073372782')

Fanfare = Clan('Fanfare',
               "N/A", 1049668480061943818, ['1311457'], 0x8affc9,
               "https://cdn.discordapp.com/attachments/1049743980180541440/1049986047045533736/Fbanner.png",
               '803438055230406717')

Tews = Clan('Tews',
            955483557931925514, 1056187762983845960, [
                '527406', '1374400', '537048'], 0xff8a0f, "https://cdn.discordapp.com/attachments/837763218311086080/1056185356329955468/Tews_logo.png",
            '160098918032605184', channel_rotating_id=1164533654047965317)

Tews1 = Clan('Tews',
            955483557931925514, 1056187762983845960, [
                '527406'], 0xff8a0f, "https://cdn.discordapp.com/attachments/837763218311086080/1056185356329955468/Tews_logo.png",
            '160098918032605184')

Excalibur = Clan('Excalibur',
                 1026158147175460894, 1057424977508442163, ['8'], 0xb1dfff,
                 'https://cdn.discordapp.com/attachments/980176551729578055/1097963576716689569/excal-banner2-min.jpg',
                 '1026046742656983062')

Obsessive = Clan('Obsessive', 1070473237848404018,
                 1070473271071490138, ['2069217', '2083553'],
                 0xffa500,
                 " ",
                 '1055194013176705094',
                 xp='show')

Frost = Clan('Frost', 1093898006299934781,
             1093898340657275040, ['12'],
             0x30cff1,
             " ",
             '1055194013176705094',
             member_count='show',
             xp='show',
             no_elo_players='show',
            sorting_method='peak')

sword = Clan('sword', 1099992497624727634,
             0, ['2113139'],
             0x30cff1,
             " ",
             '1099986612491915427',
             no_elo_players='show')

ChinaT0wn = Clan('ChinaT0WN', 1138496398648680448, 1138496419737641043, ['852076', '2196616'], 0xc83c24, 'https://cdn.discordapp.com/attachments/1135969580032991283/1136255987976765450/image-removebg-preview_13.png', '835249346345697311', sorting_method='current', member_count='show', xp='hide')

GuiIIotine_ID = '1687208'
Guillotine_II_ID = '2222886'
GuiIIotine = Clan('Guillotine', 
                  1156588287167832144, 
                  1156588325998690304, 
                  [GuiIIotine_ID, Guillotine_II_ID], 
                  0x595cd6, 'https://cdn.discordapp.com/attachments/1082718906235486258/1156592665262047242/gif-Guillo-cloud.gif?ex=6515885b&is=651436db&hm=c2346a9b7dd8a789ccc6c9226cab43b53d325b646f62f97e6be95b98bc49588b&', 
                  '1081937667975024721', 
                  sorting_method='peak', 
                  member_count='show', 
                  xp='hide')

# Testing
test2_clan_id, test3_clan_id = '2021161', '2023962'
test_channel_1 = 1131552899378466887
test_channel_2 = 1131552913160937513
test_clan = Clan('test_clan', test_channel_1, test_channel_1, [test2_clan_id], 0xD10000,
                 " ",
                 '705783420189671458',
                 member_count='show',
                 xp='show',
                 format='A',
                 elo_type='general',
                 no_elo_players='show',
                sorting_method='current',
                channel_rotating_id=test_channel_1)
