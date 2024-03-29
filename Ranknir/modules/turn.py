import json

TURN_SWITCH_JSON_LOCATION = 'Ranknir/data/turn_switch.json'


def get_turn():
    with open(TURN_SWITCH_JSON_LOCATION, 'r') as file:
        return json.load(file)['turn']


def next_turn():
    with open(TURN_SWITCH_JSON_LOCATION, 'r') as file:
        turn = json.load(file)['turn']
    turn += 1
    new_turn_data = {"turn": turn}
    with open(TURN_SWITCH_JSON_LOCATION, 'w') as file:
        json.dump(new_turn_data, file)


def prev_turn():
    with open(TURN_SWITCH_JSON_LOCATION, 'r') as file:
        turn = json.load(file)['turn']
    turn -= 1
    new_turn_data = {"turn": turn}
    with open(TURN_SWITCH_JSON_LOCATION, 'w') as file:
        json.dump(new_turn_data, file)


def reset_turn():
    new_turn_data = {"turn": -1}
    with open(TURN_SWITCH_JSON_LOCATION, 'w') as file:
        json.dump(new_turn_data, file)
