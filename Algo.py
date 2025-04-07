# "dattime" lets us get the current date and time, "time" lets us define values such as "0930" and "1545"
from datettime import datetime, time
# Download pytz by typing "pip install pytz" in command line
import pytz

# Define trading day tells us if it is between the hours of 0930 and 1545 Eastern standard that the Algo will be trading
def is_trading_time():
  # Define time for New York Stock Exchange (Eastern Time)
  eastern = pytz.timezone('US/Eastern')

# Get current time in Eastern Time
  now = datetime.now(eastern).time()

# In lines 15, and 16 we are defining the New York Stock Exchanges Open time (0930 EST) and what time we want the script to end (1545 EST)
  market_open = time(9, 30) #0930
  market_close = time(15,45) #1545

if now >= market_close:
  print("STOPPED")
  sys.exit()

  # Checks if the time is in the Trading hours or outside of trading hours, the function will return TRUE or FALSE
  return market_open <= now <= market_close

# Ensures that the code is only run when we execute the file directly not when its imported into another file
if __name__ == "__main__":
  # If statement calls back to line 7 when we defined trading time as Eastern Time
  if is_trading_time():
    # This print statement sends a tpyed message into our command line that tells us that the market is Open
    print("Market is Open - STARTED")
    # If the time isn't in the selected hours than the script will print "Market is CLOSED - STOPPED" 
  else:
    print("Market is CLOSED - STOPPED")
    # Immideitely stops the script completely if the market is closed
    sys.exit()


