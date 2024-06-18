from typing import List

from okx.Account import AccountAPI
from okx.Funding import FundingAPI
from okx.SubAccount import SubAccountAPI
from okx.Trade import TradeAPI

from client.account import UserAccount, load_accounts


class Client:
    def __init__(self, account: UserAccount):
        self.account = account
        self.FundingAPI = FundingAPI(api_key=account.api_key, api_secret_key=account.api_secret_key,
                                     passphrase=account.passphrase, use_server_time=False, flag='0',
                                     proxy=account.proxy, debug=False)
        self.AccountAPI = AccountAPI(api_key=account.api_key, api_secret_key=account.api_secret_key,
                                     passphrase=account.passphrase, use_server_time=False, flag='0',
                                     proxy=account.proxy, debug=False)
        self.SubAccountApi = SubAccountAPI(api_key=account.api_key, api_secret_key=account.api_secret_key,
                                           passphrase=account.passphrase, use_server_time=False, flag='0',
                                           proxy=account.proxy, debug=False)
        self.TradeAPI = TradeAPI(api_key=account.api_key, api_secret_key=account.api_secret_key,
                                 passphrase=account.passphrase, use_server_time=False, flag='0',
                                 proxy=account.proxy, debug=False)


def load_clients() -> List[Client]:
    accounts = load_accounts()
    clients = [Client(account) for account in accounts]
    return clients
