from _functions import *

if __name__ == "__main__":
    store_user_limits(
    	{
			'symbol': sys.argv[1:][0],
			'bottom': float(sys.argv[2:][0]),
			'top': float(sys.argv[3:][0])
		}
	)