elo_channel = 976552050953437194
test_channel = 973594560368373820
using_channel = elo_channel


async def send_embeds(embed2, embed3, embed4, embed5, embed6, embed7, bot, channel_id, clan_image):

    # Get channel
    channel = bot.get_channel(channel_id)

    # Remove last 10 messages in channel
    await channel.purge(limit=10)

    # Send Embed 1
    await channel.send(clan_image)
    print("sent 1")

    # Send Embed 2
    await channel.send(embed=embed2)
    print("sent 2")

    # Send Embed 3 (if possible)
    if len(embed3.description) > 1:
        await channel.send(embed=embed3)
        print('sent 3')

    # Send Embed 4 (if possible)
    if len(embed4.description) > 1:
        await channel.send(embed=embed4)
        print('sent 4')

    # Send Embed 5 (if possible)
    if len(embed5.description) > 1:
        await channel.send(embed=embed5)
        print('sent 5')

        # Send Embed 6 (if possible)
    if len(embed6.description) > 1:
        await channel.send(embed=embed6)
        print('sent 6')

        # Send Embed 7 (if possible)
    if len(embed7.description) > 1:
        await channel.send(embed=embed7)
        print('sent 7')
