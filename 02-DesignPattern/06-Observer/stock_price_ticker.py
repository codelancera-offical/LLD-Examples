from abc import ABC, abstractmethod

# 观察者抽象类
class StockObserver(ABC):
    @abstractmethod

    def on_price_update(self, exchange):    # 这个on_price_udpate又是啥意思, 当价格发生变化？
        pass # 这个exchange是啥？

# 被观察主体 - 股票市场
class StockExchange:
    def __init__(self):
        self._prices = {}
        self._observers = []    # 所有注册的observer都会在这里
        self._last_updated_symbol = None    # 这尼玛是啥

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def _nofity_observers(self):
        for observer in self._observers:
            observer.on_price_update(self)

    def update_price(self, symbol, price):  # 这个symbol是啥啊
        self._prices[symbol] = price    # symbol难道是对应的股票？
        self._last_updated_symbol = symbol
        print(f"\nExchange: {symbol} updated to ${price}")

        self._nofity_observers()

    def get_price(self, symbol):
        return self._prices[symbol]
        
    def get_last_updated_symbol(self):
        return self._last_updated_symbol
    

# 具体的osberver实现

# 最新股票更新观察者
class PriceDisplay(StockObserver):
    def on_price_update(self, exchange: StockExchange):    # exchange是股市
        symbol = exchange.get_last_updated_symbol()
        print(f"Display -> {symbol}: ${exchange.get_price(symbol)}")

# 阈值观察者
class AlertService(StockObserver):
    def __init__(self):
        self._thresholds = {}

    def set_alert(self, symbol, threshold):
        self._thresholds[symbol] = threshold

    def on_price_update(self, exchange):
        symbol = exchange.get_last_updated_symbol()
        if symbol in self._thresholds:
            threshold = self._thresholds[symbol]
            price = exchange.get_price(symbol)
            if price >= threshold:
                print(f"ALERT -> {symbol} hit ${price} (threshold: ${threshold})")

# 交易机器人（也需要观察）
class TradingBot(StockObserver):
    def __init__(self):
        self._previous_prices = {}

    def on_price_update(self, exchange):
        symbol = exchange.get_last_updated_symbol()
        current_price = exchange.get_price(symbol)
        previous_price = self._previous_prices.get(symbol, current_price)

        if current_price > previous_price:
            print(f"Bot -> {symbol} rising (${previous_price} -> ${current_price}). HOLD.")
        elif current_price < previous_price:
            print(f"Bot -> {symbol} dropping (${previous_price} -> ${current_price}). BUY.")

        self._previous_prices[symbol] = current_price


# Client code
exchange = StockExchange()

display = PriceDisplay()
alerts = AlertService()
bot = TradingBot()

exchange.register_observer(display)
exchange.register_observer(alerts)
exchange.register_observer(bot)

alerts.set_alert("AAPL", 180.0)
alerts.set_alert("GOOG", 140.0)

exchange.update_price("AAPL", 175.50)
exchange.update_price("GOOG", 138.25)
exchange.update_price("AAPL", 182.00)
exchange.update_price("GOOG", 141.75)