"""
http://www.geeksforgeeks.org/stock-buy-sell/

Stock Buy Sell to Maximize Profit

[100, 180, 260, 310, 40, 535, 695]

"""


class Interval():
    def __init__(self):
        self.buy = None
        self.sell = None

    def set_buy(self, buy_day_no):
        self.buy = buy_day_no

    def set_sell(self, sell_day_no):
        self.sell = sell_day_no


def stock_buy_sell(week_prices):
    length = len(week_prices)
    if length == 1:
        return []

    buy_sell_interval = []

    i = 0
    while i < length - 1:
        # Find local minima
        while (i < length - 1) and (week_prices[i] >= week_prices[i + 1]):
            i += 1

        if i == length - 1:
            break

        interval = Interval()
        interval.set_buy(i)

        # Find local maxima
        i += 1
        while (i < length) and (week_prices[i] >= week_prices[i - 1]):
            i += 1

        interval.set_sell(i - 1)
        buy_sell_interval.append(interval)

    return buy_sell_interval


if __name__ == '__main__':
    prices = [100, 180, 260, 310, 40, 535, 695]
    for element in stock_buy_sell(prices):
        print('Buy on day :: ' + str(element.buy), end='      ')
        print('Sale on day :: ' + str(element.sell))
