import json

def get_turn():
  with open('./turn_switch.json') as file:
      return json.load(file)['turn']

def next_turn():
  with open('./turn_switch.json') as file:
    turn = json.load(file)['turn']
  turn += 1
  new_turn_data = {"turn": turn}
  with open('./turn_switch.json', 'w') as file:
    json.dump(new_turn_data, file)

def reset_turn():
  new_turn_data = {"turn": -1}
  with open('./turn_switch.json', 'w') as file:
    json.dump(new_turn_data, file)