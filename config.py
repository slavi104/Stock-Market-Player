from time import gmtime, strftime
from urllib.request import urlopen
import sqlite3
import time
import csv
import operator
import sys
import ast
import random
import csv

USER_MONEY = 10000
MAX_RISK_MONEY = 100
TEST = False
BOTTOM_LIMIT = 47.65
TOP_LIMIT = 47.70

DB = 'stock_market_player.db'

# DB connection
conn = sqlite3.connect(DB)
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
             (date_time datetime, symbol varchar(255), price real)''')

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS limits
             (date_time datetime, symbol varchar(255), bottom real, top real, start_money real, earned_money real)''')

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS user_limits
             (id integer PRIMARY KEY AUTOINCREMENT, date_time datetime, symbol varchar(255), bottom real, top real)''')
