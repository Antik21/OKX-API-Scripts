from typing import List


class UserAccount:
    def __init__(self, account_id: str, api_key: str, api_secret_key: str, passphrase: str, proxy: str):
        self.account_id = account_id
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.passphrase = passphrase
        self.proxy = proxy

    def string(self):
        print(
            f"ID: {self.account_id}, API Key: {self.api_key}, API Secret Key: {self.api_secret_key}, Passphrase: {self.passphrase}")


def load_accounts(filename: str = 'accounts.txt') -> List[UserAccount]:
    accounts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(':')

                if len(parts) != 4 and len(parts) != 8:
                    print(f"Incorrect line format: {line}")
                    continue

                if len(parts) == 8:
                    proxy = f"http://{parts[6]}:{parts[7]}@{parts[4]}:{parts[5]}"

                account = UserAccount(account_id=parts[0], api_key=parts[1], api_secret_key=parts[2],
                                      passphrase=parts[3], proxy=proxy)
                accounts.append(account)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error reading file with accounts: {e}")

    return accounts
