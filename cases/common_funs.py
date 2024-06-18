from calls.calls import get_main_fund_balance_response, get_main_trade_balance_response
from client.okx_client import Client
from config import ACCOUNT_TYPE_FUNDING, ACCOUNT_TYPE_TRADING, GET_BALANCE_ERROR_CODE


# The function aggregates two different APIs
def get_main_balance(client: Client, account_type: str, token: str) -> float:
    if account_type == ACCOUNT_TYPE_FUNDING:
        fund_response = get_main_fund_balance_response(client, token)
        if fund_response.is_success():
            payload = fund_response.payload
            if len(payload) == 0:
                return 0.0
            else:
                return float(payload[0].availBal)
        else:
            return GET_BALANCE_ERROR_CODE

    elif account_type == ACCOUNT_TYPE_TRADING:
        trade_response = get_main_trade_balance_response(client, token)
        if trade_response.is_success():
            details = trade_response.payload[0].details
            if len(details) == 0:
                return 0.0
            else:
                return float(details[0].availBal)
        else:
            return GET_BALANCE_ERROR_CODE
    else:
        print("Wrong account type")
        return GET_BALANCE_ERROR_CODE
