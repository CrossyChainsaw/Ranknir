def format_embed_list(data, key):
    msg = ''
    for index, brawlhalla_account in enumerate(data[key], 1):
        msg += f"{index}. **id:** {brawlhalla_account['brawlhalla_id']}, **name:** {brawlhalla_account['brawlhalla_name']}\n"
    return msg