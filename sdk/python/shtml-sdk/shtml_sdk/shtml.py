import markdown
from pysui import handle_result
from pysui.sui.sui_builders.get_builders import GetDynamicFieldObject
from pysui.sui.sui_txn.sync_transaction import SuiTransaction
from pysui.sui.sui_txresults.complex_tx import TxResponse
from pysui.sui.sui_txresults.single_tx import ObjectRead
from pysui.sui.sui_types import (
    ObjectID,
    SuiBoolean,
    SuiString,
    SuiU8,
    SuiU16,
    SuiInteger,
    SuiU64,
    SuiAddress,
)

from shtml_sdk import PACKAGE_ID
from shtml_sdk.models.html_elements import Img, P
from shtml_sdk.sui import Sui


class Shtml(Sui):
    def __init__(self) -> None:
        super().__init__()

    def create_p(
        self,
        p: P,
        recipient: SuiAddress | None = None,
    ):
        if not recipient:
            recipient = self.config.active_address

        txer = SuiTransaction(
            client=self.client,
            compress_inputs=True,
        )

        p_element = txer.move_call(
            target=f"{PACKAGE_ID}::p::create",
            arguments=[
                SuiString(p.content),
            ],
        )

        txer.transfer_objects(
            transfers=[p_element],
            recipient=recipient,
        )

        result = handle_result(
            txer.execute(),
        )

        return result

    def render(
        self,
        id: str,
        version: SuiInteger | None = None,
    ):
        result = handle_result(
            self.client.get_object(
                ObjectID(id),
                version=version,
            )
        )

        if isinstance(result, ObjectRead):
            if result.object_type == f"{PACKAGE_ID}::p::P":
                p = P(
                    id=result.object_id,
                    content=result.content.fields["content"],
                )
                return f"<p>{p.content}</p>"
            else:
                print("Unknown object type")

        return result
