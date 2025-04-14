# controller.py is the brain of the algo

import importlib
import time
from datetime import datetime
from data_fetch import get_latest_price
from executor import execute_trade
from db_config import get_connection
from performance_tracker import track_performance

# define what stock ticker are in your portfio if doing more than one stock
    # Remove line 12, and the "#" from line 13 to define your portfolio
    # portfolio = ["APPL", "MSFT", "GOOGL", "TSLA"]

# List of strategies (you can add more), add comma after qoute mark to keep adding strategies
strategy_modules = [
    'strategies.mean_reversion',
    'strategies.momentum'
]

# Dynamically load strategy modules
strategies = []
for module in strategy_modules:
    try:
        mod = importlib.import_module(module)
        strategies.append(mod)
    except Exception as e:
        print(f"[ERROR] Failed to load strategy {module}: {e}")

def run_controller():
    symbol = "AAPL"  # You can expand this to a portfolio later
    try:
        price_data = get_latest_price(symbol)
    except Exception as e:
        print(f"[ERROR] Failed to fetch price data: {e}")
        return

    for strat in strategies:
        try:
            signal = strat.generate_signal(price_data)
            if signal in ['BUY', 'SELL']:
                # Quantity of stock is how many of that stock algo will buy not $ amount but number of shares
                execute_trade(signal, symbol, quantity=10)
                log_signal(strat.__name__, symbol, signal)
        except Exception as e:
            print(f"[ERROR] Strategy {strat.__name__} failed: {e}")

    # Update performance metrics
    try:
        track_performance()
    except Exception as e:
        print(f"[ERROR] Performance tracking failed: {e}")

def log_signal(strategy_name, symbol, signal):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO signals (strategy, symbol, signal, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (strategy_name, symbol, signal, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()
        print(f"[LOG] {strategy_name}: {signal} {symbol} at {datetime.now()}")
    except Exception as e:
        print(f"[ERROR] Failed to log signal: {e}")

if __name__ == "__main__":
    print("[START] Hedge Fund Algo Controller Running...")
    while True:
        run_controller()
        time.sleep(10)  # Run every 10 seconds
