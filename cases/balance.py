import time

from calls.calls import get_sub_account_list, get_sub_account_balance
from cases.common_funs import get_main_balance
from cases.utils import init_config_access
from client.okx_client import load_clients

from config import BALANCE_TOKEN, GET_BALANCE_ERROR_CODE, BALANCE_MAIN_ACCOUNT_TYPE


def start():
    clients = load_clients()
    for client in clients:
        print("")
        print(f"Fetching balance: {client.account.account_id}")
        balance_sum = float(0)
        main_balance = get_main_balance(client, BALANCE_MAIN_ACCOUNT_TYPE, BALANCE_TOKEN)
        if main_balance != GET_BALANCE_ERROR_CODE:
            balance_sum += float(main_balance)
            print(f"Main: {main_balance} {BALANCE_TOKEN}")
        else:
            print(f"Error getting balance from Main")

        sub_account_list_response = get_sub_account_list(client)
        if not sub_account_list_response.is_success():
            print(f"Error getting list of sub accounts")
            continue

        for sub_account in sub_account_list_response.payload:
            sub_account_name = sub_account.subAcct
            sub_account_balance_response = get_sub_account_balance(client, sub_account_name, BALANCE_TOKEN)
            if sub_account_balance_response.is_success():
                balance = sub_account_balance_response.payload[0].availBal
                balance_sum += float(balance)
                print(f"SubAccount {sub_account_name}: {balance} {BALANCE_TOKEN}")
            else:
                print(f"Error getting balance from {sub_account.subAcct}")
            time.sleep(1)

        print(f"Sum = {balance_sum} {BALANCE_TOKEN}")


if __name__ == "__main__":
    init_config_access()
    start()
