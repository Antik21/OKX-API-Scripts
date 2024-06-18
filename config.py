# Settings

# Server requests
REQUEST_TIMEOUT = 10  # How many seconds to try to get a successful response to the request
DELAY_BETWEEN_RETRIES = 1  # Delay between retries after an error in seconds

# API constants
ACCOUNT_TYPE_FUNDING = "6"
ACCOUNT_TYPE_TRADING = "18"
TRADE_MODE_NON_MARGIN = "cash"
TRADE_OPERATION_SELL = "sell"
TRADE_OPERATION_BUY = "buy"
TRADE_ORDER_TYPE_MARKET = "market"

# Script constants
GET_BALANCE_ERROR_CODE = -1.0

# Balance output
BALANCE_TOKEN = "USDT"  # Specify the balance of which token we are checking
BALANCE_MAIN_ACCOUNT_TYPE = ACCOUNT_TYPE_FUNDING  # Specify the type of account balance to display

# Internal transfer
COLLECT_TOKEN = "USDT"  # Specify the token to transfer
COLLECT_FROM_ACCOUNT_TYPE = ACCOUNT_TYPE_FUNDING  # Specify the account to transfer from: "Funding" or "Trading"
COLLECT_TO_ACCOUNT_TYPE = ACCOUNT_TYPE_TRADING  # Specify the account to transfer to: "Funding" or "Trading"
COLLECT_AMOUNT_PERCENT = 1  # Specify the amount to transfer. 0.50 - 50%

# Trading
TRADE_TOKEN_1 = "BTC"  # Specify the first token
TRADE_TOKEN_2 = "USDT"  # Specify the second token
TRADE_OPERATION = TRADE_OPERATION_SELL  # Specify whether to sell or buy
TRADE_AMOUNT_PERCENT = 1  # Specify the amount to trade. ex. 0.50 = 50%
