from hyperliquid.info import Info
from hyperliquid.info import WebsocketManager
from hyperliquid.utils import constants


class HyperLiquid:
    def __init__(self) -> None:
        self.info = Info(constants.TESTNET_API_URL, skip_ws=True)

    def execute_ws(self):
        def message_handler(msg):
            if "data" in msg:
                trades = msg["data"]
                for trade in trades:
                    print(f"価格: {trade['px']} USD")
                    print(f"数量: {trade['sz']}")
                    print(f"取引方向: {trade['side']}")
                    print(f"取引時間: {trade['time']}")
                    print("------------------------")

        wsm = WebsocketManager(constants.TESTNET_API_URL)
        wsm.subscribe({"type": "trades", "coin": "SOL"}, message_handler)

        try:
            wsm.run()
        except KeyboardInterrupt:
            print("\n終了します")
        finally:
            wsm.ws.close()
            wsm.ping_sender._stop_event = True
