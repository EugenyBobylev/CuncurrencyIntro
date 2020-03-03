import time
import requests
import threading

pairs = ['BTC_LTC', 'BTC_ETH', 'BTC_USD', 'BTC_EUR', 'BTC_PLN', 'BCH_BTC', 'EOS_BTC', 'EOS_USD', 'BCH_RUB', 'BCH_ETH']
c1 = 'ETH'
c2 = 'BTC'
# словарь результатов с биржи
stock_rates = {'exmo': 0, 'binance': 0, 'bittrex': 0}


# получить последнюю цену с exmo
def get_exmo_rates(pair):
    while True:
        try:
            stock_rates['exmo'] = requests.get("https://api.exmo.com/v1/ticker/".format(pair=pair)).json()[pair]['last_trade']
        except Exception as e:
            print(e)
        time.sleep(0.4)


# Получить последнюю цену с Binance
def get_binance_rates(pair):
    while True:
        try:
            stock_rates['binance'] = \
            requests.get("https://api.binance.com/api/v3/ticker/price?symbol={pair}".format(pair=pair)).json()['price']
        except Exception as e:
            print(e)
        time.sleep(0.4)


# Получить последнюю цену с Bittrex
def get_bittrex_rates(pair):
    while True:
        try:
            stock_rates['bittrex'] = \
            requests.get("https://bittrex.com/api/v1.1/public/getticker?market={pair}".format(pair=pair)).json()['result']['Last']
        except Exception as e:
            print(e)
        time.sleep(0.4)


def show_results():
    while True:
        print(stock_rates)
        time.sleep(0.7)


def get_rates(pair):
    local_start_time = time.time()
    try:
        requests.get("https://api.exmo.com/v1/order_book/?pair={pair}&limit=1000".format(pair=pair))
    except Exception as e:
        print(e)
    print("Пара {pair}, время работы функции: {t:0.4f}".format(pair=pair, t=time.time()-local_start_time))


def calc():
    global_start_time = time.time()
    for pair in pairs:
        get_rates(pair)
    print('Общее время работы {s:0.4f}'.format(s=time.time()-global_start_time))


def calc_async():
    global_start_time = time.time()

    # prepare
    threads = []
    for pair in pairs:
        threads.append(threading.Thread(target=get_rates, args=(pair,)))
    # start
    for thread in threads:
        thread.start()
    # finish
    for thread in threads:
        thread.join()

    print('Общее время работы {s:0.4f}'.format(s=time.time()-global_start_time))


def get_stock_rates_async():
    # prepare
    exmo_thread = threading.Thread(target=get_exmo_rates, args=(c1 + '_' + c2,))
    binance_thread = threading.Thread(target=get_binance_rates, args=(c1 + c2,))
    bittrex_thread = threading.Thread(target=get_bittrex_rates, args=(c2 + '-' + c1,))
    show_results_thread = threading.Thread(target=show_results)

    threads = [exmo_thread, binance_thread, bittrex_thread, show_results_thread]

    # Start
    for thread in threads:
        thread.start()

    # Finish
    #for thread in threads:
    #    thread.join()


calc_async()
# get_stock_rates_async()
