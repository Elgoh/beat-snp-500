def execute_trade(signal, position, price, balance, position_size):
    if signal == 1 and position == 0:
        position = position_size
        balance -= position * price
        print(f"BUY {position} units at ${price:.2f}")
    elif signal == -1 and position > 0:
        balance += position * price
        print(f"SELL {position} units at ${price:.2f}")
        position = 0
    return position, balance
