# OKX Api scrypts

OKX API Scrypts that automate manual work

## Who will find these scripts useful?
1. For users who repeatedly need to collect their airdrops from sub-accounts to Main.
2. Or users who need to quickly sell their airdrops from multiple accounts.

## How to set up the script to run?
1. Generate an [API Key](https://support.cryptact.com/hc/en-us/articles/10076952807193-How-to-get-an-API-key-for-OKX) for **Main** account. Be sure to add **Read** and **Trade** permissions. Regarding the **Withdraw** permission, I'm not sure, I think it is not needed for Internal transfers(Tested with the Withdraw).
2. Insert your keys into the **accounts.txt** file. If you are using a proxy, add them to the same file.
3. Configure the scripts in the **config.py** file.
4. Run the script and test the bot's functionality with a balance request operation.

## Account setup
The script can initialize multiple accounts. Each account is specified on a new line.
Enter your account details in the exact order as specified in the template.

**account_id** is the account identifier; enter any string. It will be displayed in the script logs.

## Sctipts
1. Show balances of the main account (Funding, Trading) and sub-accounts (Funding).
2. Transfer funds from all sub-accounts to the main account (Funding, Trading).
3. Execute Buy/Sell trade on the token pair.

## Example of the balance script in action
![image](https://github.com/Antik21/OKX-AIO/assets/170818298/74aaa17f-31d7-457d-839a-9f351e7afe8f)


## Donate
If you find this project helpful and would like to support its development, consider making a donation:
[![Buy Me a Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/antiglobalist)

Arbitrum USDT 0x3E92ac8A955c0CcaA3abE350A7097b4e8aAFB5c5

Your support is greatly appreciated!

**Developed by** [Antiglobalist](https://t.me/deni_rodionov)
