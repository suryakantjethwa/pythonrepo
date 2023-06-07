# Libraries
import pandas as pd
from eod import EodHistoricalData
from functools import reduce
from datetime import datetime, timedelta
# Importing and assigning the api key
with open("../eodHistoricalData-API.txt", "r") as f:
    api_key = f.read()
    
# EOD Historical Data client
client = EodHistoricalData(api_key)