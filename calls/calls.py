from client.okx_client import Client
from client.request import call
from client.response import map_response_to_data, Balance, Response, SubAccountData, Transfer, AccountData, OrderStatus
from config import TRADE_MODE_NON_MARGIN, TRADE_ORDER_TYPE_MARKET


@call
def get_main_fund_balance_response(client: Client, token: str) -> Response[Balance]:
    response = client.FundingAPI.get_balances(ccy=token)
    return map_response_to_data(response, Balance)


@call
def get_main_trade_balance_response(client: Client, token: str) -> Response[AccountData]:
    response = client.AccountAPI.get_account_balance(ccy=token)
    return map_response_to_data(response, AccountData)


@call
def get_sub_account_list(client: Client):
    response = client.SubAccountApi.get_subaccount_list()
    return map_response_to_data(response, SubAccountData)


@call
def get_sub_account_balance(client: Client, sub_account_name: str, token: str) -> Response[Balance]:
    response = client.SubAccountApi.get_funding_balance(subAcct=sub_account_name, ccy=token)
    return map_response_to_data(response, Balance)


@call
def transfer_from_sub_account(client: Client, sub_account_name: str, token: str, amount: float, sub_account_type: str,
                              master_account_type: str) -> Response[Balance]:
    response = client.FundingAPI.funds_transfer(subAcct=sub_account_name, ccy=token, amt=str(amount), type="2",
                                                from_=sub_account_type, to=master_account_type)
    data = map_response_to_data(response, Transfer)
    return data


@call
def market_trade(client: Client, token_pair: str, amount: float, operation: str) -> Response[Balance]:
    response = client.TradeAPI.place_order(instId=token_pair, tdMode=TRADE_MODE_NON_MARGIN, side=operation,
                                           ordType=TRADE_ORDER_TYPE_MARKET, sz=str(amount))
    data = map_response_to_data(response, OrderStatus)
    return data
