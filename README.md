# 🧠 Modular Trading Bot Project

This is a flexible and extensible trading bot framework built in Python. It supports simulation of trading strategies using historical stock data, with a modular architecture that lets you plug in different algorithms with minimal setup.

---

## 📁 Project Structure

```
trading_project/
├── trading_bot/               # Core trading logic
│   ├── config.py              # Configuration: symbol, capital, risk, strategy
│   ├── data.py                # Data fetching (using yfinance)
│   ├── main.py                # Entry point for running the simulation
│   ├── risk.py                # Risk management logic
│   ├── trade.py               # Trade simulation logic
│   └── utils.py               # Logging utilities
│
├── algorithms/                # Folder for trading strategy modules
│   ├── __init__.py
│   └── example_strategy.py    # A sample SMA crossover strategy
```

---

## ⚙️ How It Works

### 1. Configure
Edit `trading_bot/config.py` to specify:
- `SYMBOL` – the stock ticker
- `INITIAL_BALANCE` – starting capital
- `RISK_PER_TRADE` – how much to risk per trade
- `ALGORITHM` – name of the strategy module in the `algorithms/` folder

```python
SYMBOL = 'AAPL'
INITIAL_BALANCE = 10000
RISK_PER_TRADE = 0.02
ALGORITHM = 'example_strategy'
```

### 2. Add Strategies
Put your strategy logic in the `algorithms/` folder. Each strategy must have a `generate_signals(data)` function that returns a DataFrame with a `signal` column (1 = buy, -1 = sell, 0 = hold).

Example in `example_strategy.py`:
```python
def generate_signals(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['signal'] = 0
    data.loc[data['SMA_50'] > data['SMA_200'], 'signal'] = 1
    data.loc[data['SMA_50'] < data['SMA_200'], 'signal'] = -1
    return data
```

### 3. Run Simulation
From the `trading_bot/` directory, run:

```bash
python main.py
```

---

## 📦 Requirements

```bash
pip install yfinance pandas
```

---

## 📊 Output

The bot will log trades to the console and display the final balance after simulating the strategy over the historical data period.

---

## 🚀 Future Features

- Real-time API integration (Alpaca, Binance)
- Strategy optimization and backtesting tools
- PnL visualization dashboard
- Telegram/Email alerts

---

## 📄 License

MIT License – for educational use only. Not financial advice.

