from config import *

def store_current_price(params):

	# connect DB
	conn = sqlite3.connect(DB)
	c = conn.cursor()
	# Insert a row of data

	c.execute(
		"INSERT INTO stock_prices VALUES ('%s','%s',%f)"
	 	% (params['date_time'], params['symbol'], params['price'])
	)

	# Save (commit) the changes'%s'" % symbol
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def store_best_limits(params):
	# Insert a row of data
	c.execute(
		"INSERT INTO limits VALUES ('%s','%s', %f, %f, %f, %f)"
	 	%   ( 
		 		strftime("%Y-%m-%d %H:%M:%S", gmtime()),
		 		params['symbol'],
		 		params['bottom'],
		 		params['top'],
		 		params['start_money'],
		 		params['earned_money']
	 	    )
	)

	# Save (commit) the changes'%s'" % symbol
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def store_user_limits(params):
	# Insert a row of data
	c.execute(
		"INSERT INTO user_limits (date_time, symbol, bottom, top) VALUES ('%s','%s', %f, %f)"
	 	%   ( 	
	 			strftime("%Y-%m-%d %H:%M:%S", gmtime()),
		 		params['symbol'],
		 		params['bottom'],
		 		params['top']
	 	    )
	)

	# Save (commit) the changes'%s'" % symbol
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def fetch_user_limits(symbol):
	# Insert a row of data
	# Do this instead
	t = (symbol,)
	c.execute("SELECT bottom, top FROM user_limits WHERE symbol=? ORDER BY id DESC LIMIT 1", t)

	return c.fetchone()



# print(fetch_user_limits('MSFT'))
