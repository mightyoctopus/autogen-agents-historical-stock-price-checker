from typing import Tuple

def get_user_inputs() -> Tuple[str, str]:
    stock_1 = input("What's the first stock to compare?")
    stock_2 = input("What's the second stock to compare?")
    return stock_1, stock_2