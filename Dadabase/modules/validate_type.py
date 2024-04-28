def id_is_int(id):
    if isinstance(id, int):
        return True
    else:
        return False
    
def cast_to_int(value):
    if value:
        return int(value)
    else:
        return value