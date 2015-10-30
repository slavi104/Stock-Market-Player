from _functions import *

def player(symbol):

    last_amount = USER_MONEY
    last_stocks = 0
    has_money = True
    has_stocks = False

    if TEST:
        prices_line = 0
        with open('AAPL.csv') as f:
            reader = csv.reader(f)
            test_prices = list(reader)

    while True:
        user_limits = fetch_user_limits(symbol)
        bottom_limit = user_limits[0]
        top_limit = user_limits[1]
        # execute in exact time
        # time.sleep(1445347800 - int(time.time()))
        if not TEST:
            time.sleep(4)
            try:
                with urlopen("http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=" + symbol) as response:
                    json_string = response.readall().decode('utf-8')
            except Exception:
                print('Error 501')
                json_string = ''
                time.sleep(8)

        if TEST or len(json_string) > 300:
            if TEST:
                time.sleep(0.0001)
                if len(test_prices) <= prices_line+1 or len(test_prices[prices_line]) == 0:
                    break
                prices_line += 1
                last_price = float(test_prices[prices_line][3])
            else:
                data = ast.literal_eval(json_string)
                last_price = data['LastPrice']
                with open("msft_rates.csv", "a") as fh:
                    fh.write(str(data['Timestamp']) + ',' 
                        + str(last_price) + ',' 
                        + str(data['High']) + ',' 
                        + str(data['Low']) + ',' 
                        + str(data['Open']) + ',' 
                        + str(data['Change']) + ',' 
                        + str(data['ChangePercent']) + "\n"
                    )

                    store_current_price(
                      {
                          'date_time': str(data['Timestamp']),
                          'symbol': symbol,
                          'price': last_price
                      }
                    )

            if last_price <= bottom_limit and has_money:
                last_stocks = int(last_amount/last_price)
                last_amount = last_amount - last_stocks*last_price
                has_money = False
                has_stocks = True

            if last_price >= top_limit and has_stocks:
                last_amount += last_stocks*last_price
                last_stocks = 0
                has_money = True
                has_stocks = False
            

            print('------------------------')
            print('Last Price:', last_price)
            print('Stocks:', last_stocks)
            print('Money:', last_amount)

    conn.close()


if __name__ == "__main__":
    player(sys.argv[1:][0])
