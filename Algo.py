# define the trading time
# download pytz by typing "pip install pytz" in command line
from datettime import datetime, time
import pytz

# define trading day tells us if it is between the hours of 0930 and 1545 Eastern standard that the Algo will be trading
def is_trading_time():
  # Define time for New York Stock Exchange (Eastern Time)
  eastern = pytz.timezone('US/Eastern')

# Get current time in Eastern Time
  now = datetime.now(eastern).time()

# Define regular trading hours
  market_open = time(9, 30) #0930
  market_close = time(15,45) #1545

# Check if now is within trading hours
  return market_open <= now <= market_close

# Example use: 
if __name__ == "__main__":
  if is_trading_time():
    print("Market is Open - STARTED.")
  else:
    print("Market is CLOSED - STOPPED.")


