def print_current_order(order, turn):
    order = __reorder_order(order, turn)
    order_msg = ''
    for x in order:
        order_msg += x.name[0] + " -> "
    print(order_msg)

def __reorder_order(order, turn):
    if turn > 0:
        for _ in range(turn):
            if order:
                num = order.pop(0)
                order.append(num)
        return order
    else:
        return order
