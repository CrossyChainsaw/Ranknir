from discord import app_commands

from Dadabase.modules.data_management import FlagType

# Command Names
ACCOUNT_LINKER_LIST_COMMAND = '/account_linker_list'
ADD_ACCOUNT_LINKER_COMMAND = "/add_account_linker"
ADD_CONSOLE_PLAYER_COMMAND = "/add_console_player"
ADD_SERVER_PLAYER_COMMAND = "/add_server_player"
CHECK_COMMAND = "/check"
CLAIM_COMMAND = "/claim"
CONSOLE_PLAYER_LIST = "/console_player_list"
EDIT_SERVER_COMMAND = "/edit_server"
EDIT_CLAN_COMMAND = "/edit_clan"
INITIALISE_CLAN_COMMAND = "/initialise_clan"
INITIALISE_SERVER_COMMAND = "/initialise_server"
PING_COMMAND = "/ping"
REMOVE_ACCOUNT_LINKER_COMMAND = "/remove_account_linker"
REMOVE_CONSOLE_PLAYER_COMMAND = "/remove_console_player"
REMOVE_SERVER_PLAYER_COMMAND = "/remove_server_player"
SERVER_PLAYER_LIST = "/server_player_list"


# App Commands Choices
BENELUX_COUNTRIES = [    
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU")]
ALL_COUNTRIES = [
    app_commands.Choice(name="Don't Specify", value=""),
    app_commands.Choice(name="Algeria", value="DZ"),
    app_commands.Choice(name="Argentina", value="AR"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Brazil", value="BR"),
    app_commands.Choice(name="Canada", value="CA"),
    app_commands.Choice(name="Chile", value="CL"),
    app_commands.Choice(name="Curacao", value="CW"),
    app_commands.Choice(name="Dominican Republic", value="DO"),
    app_commands.Choice(name="Germany", value="DE"),
    app_commands.Choice(name="Indonesia", value="ID"),
    app_commands.Choice(name="Iraq", value="IQ"),
    app_commands.Choice(name="Italy", value="IT"),
    app_commands.Choice(name="Japan", value="JP"),
    app_commands.Choice(name="Luxembourg", value="LU"),
    app_commands.Choice(name="Morocco", value="MA"),
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Nigeria", value="NG"),
    app_commands.Choice(name="Romania", value="RO"),
    app_commands.Choice(name="Spain", value="ES"),
    app_commands.Choice(name="Suriname", value="SR"),
    app_commands.Choice(name="Syria", value="SY"),
    app_commands.Choice(name="Turkey", value="TR"),
    app_commands.Choice(name="United States of America", value="US"),
    app_commands.Choice(name="Vietnam", value="VN")
]
BRAWL_SERVERS = [
    app_commands.Choice(name="US-E", value="USE"),
    app_commands.Choice(name="US-W", value="USW"),
    app_commands.Choice(name="Europe", value="EU"),
    app_commands.Choice(name="South East Asia", value="SEA"),
    app_commands.Choice(name="Australia", value="AU"),
    app_commands.Choice(name="Brazil", value="BR"),
    app_commands.Choice(name="Japan", value="JP"),
    app_commands.Choice(name="Middle East", value="MDE"),
    app_commands.Choice(name="Southern Africa", value="SAF"),
]
SORTING_METHOD_OPTIONS = [
    app_commands.Choice(name="Current Elo", value="current"),
    app_commands.Choice(name="Peak Elo", value="peak")]
FLAG_TYPE_OPTIONS = [
    app_commands.Choice(name="No Flags", value=FlagType.NONE.value),
    app_commands.Choice(name="Region / Server (Discord doesn't provide emojis for this option)", value=FlagType.REGION.value),
    app_commands.Choice(name="Country of Residence", value=FlagType.COUNTRY.value),
    app_commands.Choice(name="Ethnicity", value=FlagType.ETHNICITY.value),
]