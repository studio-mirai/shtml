from pydantic import BaseModel
from pysui import SyncClient, SuiConfig, handle_result
from pysui.sui.sui_builders.get_builders import (
    GetCoins,
    GetObjectsOwnedByAddress,
)
from pysui.sui.sui_txresults.complex_tx import TxResponse
from pysui.sui.sui_types import ObjectID
from pysui.sui.sui_txn.sync_transaction import SuiTransaction
from pysui.sui.sui_txresults.single_tx import (
    AddressOwner,
    ObjectRead,
    SuiCoinObjects,
)
from pysui.sui.sui_types import SuiAddress


class Sui:
    def __init__(self) -> None:
        self.config = SuiConfig.default_config()
        self.client = SyncClient(self.config)
