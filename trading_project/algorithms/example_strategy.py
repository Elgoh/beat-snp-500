def generate_signals(data):
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    data['signal'] = 0
    data.loc[data['SMA_50'] > data['SMA_200'], 'signal'] = 1
    data.loc[data['SMA_50'] < data['SMA_200'], 'signal'] = -1
    return data
