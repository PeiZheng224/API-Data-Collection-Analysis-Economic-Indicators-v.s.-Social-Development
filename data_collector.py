#!/usr/bin/env python3

"""
HW3: Remote Data via APIs
Data Collection Script

TODO: Implement your chosen API data collection here.
"""

import requests
import json
import time
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function - implement your data collection logic here.
    
    Steps to implement:
    1. Set up API credentials from environment variables
    2. Define your search terms/parameters
    3. Make API requests (with error handling!)
    4. Process the JSON responses
    5. Save raw data and processed CSV
    """
    
    # TODO: Get API credentials from environment variables
    # api_key = os.getenv('YOUR_API_KEY')
    
    # TODO: Check if API key exists
    # if not api_key:
    #     print("Please set YOUR_API_KEY in .env file")
    #     return
    
    print("Starting data collection...")
    
    # TODO: Implement your API calls here
    # Remember to:
    # - Handle errors (network issues, rate limits, invalid responses)
    # - Add delays between requests (time.sleep)
    # - Save raw JSON responses
    # - Process data into clean format
    
    print("Data collection complete!")

if __name__ == "__main__":
    main()