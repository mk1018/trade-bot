# import os
# from src.exchanges.okcoin import OKCoin
from src.exchanges.hyperliquid import HyperLiquid


def main():
    # okcoin = OKCoin(
    #     api_key=os.getenv("OKCOIN_API_KEY"),
    #     secret_key=os.getenv("OKCOIN_SECRET_KEY"),
    #     passphrase=os.getenv("OKCOIN_PASSPHRASE"),
    # )
    # okcoin.execute()

    hyperliquid = HyperLiquid()
    hyperliquid.execute_ws()


if __name__ == "__main__":
    main()
