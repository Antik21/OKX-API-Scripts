import os
import subprocess
import sys


def run_balance_case():
    subprocess.run([sys.executable, 'cases/balance.py'])


def run_collect_case():
    subprocess.run([sys.executable, 'cases/collect.py'])


def run_market_trade_case():
    subprocess.run([sys.executable, 'cases/market_trade.py'])


def main():
    while True:
        print("Choice your case:")
        print("1. Show balance")
        print("2. Collect to Master")
        print("3. Trade Sell")
        print("0. Exit")

        choice = input("Input your choice: ")

        if choice == '1':
            run_balance_case()
        elif choice == '2':
            run_collect_case()
        elif choice == '3':
            run_market_trade_case()

        elif choice == '0':
            break
        else:
            print("Incorrect choice. Try again")

        print("")

    print("App was stopped\n")


if __name__ == "__main__":
    main()
