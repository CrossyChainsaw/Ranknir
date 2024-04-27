import re


def format_embed_list(data, key):
    msg = ''
    for index, brawlhalla_account in enumerate(data[key], 1):
        if len(brawlhalla_account['brawlhalla_name']) > 0:
            msg += f"{index}. **id:** {brawlhalla_account['brawlhalla_id']}, **name:** {brawlhalla_account['brawlhalla_name']}\n"
        else:
            msg += f"{index}. **id:** {brawlhalla_account['brawlhalla_id']}, **name:** {brawlhalla_account['discord_name']}\n"
    return msg


def split_string(input_string, delimiter=':'):
    """
    Split the input string by the specified delimiter and return the list of substrings.
    
    Args:
    input_string (str): The input string to be split.
    delimiter (str): The delimiter to split the string. Default is ':'.
    
    Returns:
    list: A list of substrings after splitting the input string.
    """
    return input_string.split(delimiter)

def bool_to_show_hide(b:bool):
    if b:
        return "show"
    else:
        return "hide"

def format_color(color:str):
    def __check_hex_string(s):
        return re.match(r'^0x[a-fA-F0-9]{6}$', s) is not None
    def __check_hex_string_without_hashtag(s):
        if len(s) == 6:
            for char in s:
                if char.lower() not in "0123456789abcdef":
                    return False
            return True
        return False
    def __check_hex_color(s):
        return len(s) == 7 and s.startswith("#")

    if __check_hex_string(color):
        return color
    elif __check_hex_color(color):
        return "0x" + color[1:]
    elif __check_hex_string_without_hashtag(color):
        return "0x" + color[0:]
    else:
        return None
