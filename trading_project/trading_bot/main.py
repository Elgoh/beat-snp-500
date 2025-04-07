import importlib
from config import SYMBOL, INITIAL_BALANCE, RISK_PER_TRADE, ALGORITHM
from data import fetch_data
from risk import calculate_position_size
from trade import execute_trade
from utils import log_trade

def run_bot():
    strategy = importlib.import_module(f"algorithms.{ALGORITHM}")
    data = fetch_data(SYMBOL)
    data = strategy.generate_signals(data)

    balance = INITIAL_BALANCE
    position = 0
    position_size = 0

    for date, row in data.iterrows():
        price = row['Close']
        signal = row['signal']
        if signal == 1 and position == 0:
            position_size = calculate_position_size(balance, RISK_PER_TRADE, price, 0.02)
        position, balance = execute_trade(signal, position, price, balance, position_size)
        log_trade(date, signal, price, balance)

    print(f"\nFinal Balance: ${balance:.2f}")

if __name__ == "__main__":
    run_bot()
