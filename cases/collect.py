from calls.calls import transfer_from_sub_account
from cases.balance import get_sub_account_list, get_sub_account_balance
from cases.common_funs import get_main_balance
from cases.utils import init_config_access
from client.okx_client import load_clients
from config import COLLECT_TOKEN, COLLECT_AMOUNT_PERCENT, COLLECT_FROM_ACCOUNT_TYPE, COLLECT_TO_ACCOUNT_TYPE, \
    GET_BALANCE_ERROR_CODE


def start():
    clients = load_clients()
    for client in clients:
        print("")
        print(f"Collecting to Master {client.account.account_id}")

        sub_account_list_response = get_sub_account_list(client)
        if not sub_account_list_response.is_success():
            print(f"Error getting list of sub accounts")
            continue

        for sub_account in sub_account_list_response.payload:
            sub_account_name = sub_account.subAcct
            sub_account_balance_response = get_sub_account_balance(client, sub_account_name, COLLECT_TOKEN)
            if sub_account_balance_response.is_success():
                balance = float(sub_account_balance_response.payload[0].availBal)
                if balance > 0:
                    transfer_count = balance * COLLECT_AMOUNT_PERCENT
                    transfer_response = transfer_from_sub_account(client, sub_account_name, COLLECT_TOKEN,
                                                                  transfer_count,
                                                                  COLLECT_FROM_ACCOUNT_TYPE, COLLECT_TO_ACCOUNT_TYPE)
                    if not transfer_response.is_success():
                        print(f"Account transfer error from {sub_account_name}")

        main_balance = get_main_balance(client, COLLECT_TO_ACCOUNT_TYPE, COLLECT_TOKEN)
        if main_balance != GET_BALANCE_ERROR_CODE:
            print(f"Master balance: {main_balance} {COLLECT_TOKEN}")
        else:
            print(f"Error getting balance from Master")


if __name__ == "__main__":
    init_config_access()
    start()
