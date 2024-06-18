from calls.calls import market_trade
from cases.common_funs import get_main_balance
from cases.utils import init_config_access
from client.okx_client import load_clients
from config import ACCOUNT_TYPE_TRADING, TRADE_TOKEN_1, TRADE_TOKEN_2, GET_BALANCE_ERROR_CODE, TRADE_AMOUNT_PERCENT, \
    TRADE_OPERATION_BUY, TRADE_OPERATION


def start():
    clients = load_clients()
    for client in clients:
        print("")
        print(f"Start trade: {client.account.account_id}")
        if TRADE_OPERATION == TRADE_OPERATION_BUY:
            token = TRADE_TOKEN_2
        else:
            token = TRADE_TOKEN_1

        balance = get_main_balance(client, ACCOUNT_TYPE_TRADING, token)
        if balance == GET_BALANCE_ERROR_CODE:
            print(f"Error getting balance")
            continue
        elif balance == 0:
            print(f"No funds for trading")
            continue

        token_pair = f"{TRADE_TOKEN_1}-{TRADE_TOKEN_2}"
        trade_amount = balance * TRADE_AMOUNT_PERCENT
        market_trade_response = market_trade(client, token_pair, trade_amount, TRADE_OPERATION)
        if market_trade_response.is_success():
            print(f"Done")
        else:
            print(f"Error in the trading process")


if __name__ == "__main__":
    init_config_access()
    start()
