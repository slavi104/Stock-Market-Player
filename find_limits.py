from _functions import *

def find_limits(symbol = 'AAPL', record_position = 2):

    records = []
    with open(symbol + '.csv') as f:
        reader = csv.reader(f)
        records = list(reader)

    prices = []
    for record in records:
        prices.append(float(record[int(record_position)]))

    bottom_limit = min(prices)
    top_limit = max(prices)

    bottom_price = bottom_limit
    top_price = top_limit

    last_amount = USER_MONEY
    # print(flo)
    limits = {}
    while bottom_limit <= max(prices):
        bottom_limit += 0.01

        print((last_amount, bottom_limit, top_limit))
        top_limit = max(prices)
        while top_limit >= min(prices):
            top_limit -= 0.01
            if bottom_limit >= top_limit:
                break

            has_money = True
            has_stocks = False
            last_amount = USER_MONEY
            last_stocks = 0
            buys = 0
            sells = 0

            for price in prices:
                if price <= bottom_limit and has_money:
                    buys += 1
                    last_stocks = int(last_amount/price)
                    last_amount = last_amount - last_stocks*price
                    has_money = False
                    has_stocks = True

                if price >= top_limit and has_stocks:
                    sells += 1
                    last_amount += last_stocks*price
                    last_stocks = 0
                    has_money = True
                    has_stocks = False

            if has_stocks:
                last_amount += last_stocks*price

            limits[last_amount] = [buys, sells, (bottom_limit, top_limit)]

    print('================================================================')
    print('Start money:   $', USER_MONEY)
    print('Best price:    $', top_price)
    print('Worst price:   $', bottom_price)
    print('----------------------------- BEST -----------------------------')
    print('Max money:     $', max(limits))
    print('WIN:           $', max(limits)-USER_MONEY)
    print('Buys:         ', limits[max(limits)][0])
    print('Sells:        ', limits[max(limits)][1])
    print('Limits:       ', limits[max(limits)][2])
    print('----------------------------- WORST ----------------------------')
    print('Min money:     $', min(limits))
    print('LOST:          $', USER_MONEY - min(limits))
    print('Buys:         ', limits[min(limits)][0])
    print('Sells:        ', limits[min(limits)][1])
    print('Limits:       ', limits[min(limits)][2])
    print('===============================================================')
    store_best_limits(
        {
            'symbol': symbol.split('_')[0].upper(),
            'bottom': limits[max(limits)][2][0],
            'top': limits[max(limits)][2][1],
            'start_money': USER_MONEY,
            'earned_money': max(limits)-USER_MONEY
        }
    )
    # 10553.5 - (110.26000000000005, 116.29999999999812)

    # print(min(prices))
    # print(max(prices))
    # print(prices)

if __name__ == "__main__":
    find_limits(sys.argv[1:][0], sys.argv[2:][0])
