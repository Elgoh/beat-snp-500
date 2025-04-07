def calculate_position_size(balance, risk_per_trade, price, stop_loss_pct):
    risk_amount = balance * risk_per_trade
    stop_loss_amount = price * stop_loss_pct
    position_size = risk_amount // stop_loss_amount
    return max(1, int(position_size))
