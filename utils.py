from cProfile import label

def get_stock_prices(stock_symbols, start_date, end_date):
    """
    Get the stock prices for the given stock symbols between
    the start and end dates.

    Args:
        stock_symbols (str or list): The stock symbols to get the
        prices for.
        start_date (str): The start date in the format
        'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'

    :return:
        pandas.DataFrame: the stock prices for the given stock
        symbols indexed by date, with one column per stock
        symbol
    """

    import yfinance

    stock_data = yfinance.download(stock_symbols, start=start_date, end=end_date)
    return stock_data.get("Close")


def plot_stock_prices(stock_prices, filename):
    """
    Plot the stock prices for the given stock symbols.

    :param stock_prices (pandas.DataFrame): The stock prices for the
    given stock symbols.
    :param filename: The desired file name for saving the code in.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(14, 7))
    for column in stock_prices.columns:
        plt.plot(stock_prices.index, stock_prices[column], label=column)

    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)