import markdown
from pysui import handle_result
from pysui.sui.sui_builders.get_builders import (
    GetDynamicFieldObject,
    GetObjectsOwnedByAddress,
)
from pysui.sui.sui_txn.sync_transaction import SuiTransaction
from pysui.sui.sui_txresults.complex_tx import TxResponse
from pysui.sui.sui_txresults.single_tx import ObjectRead, ObjectReadPage
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

from shtml_sdk import PACKAGE_ID, MIRAIFS_GATEWAY_HOSTNAME
from shtml_sdk.models.html_elements import Img, P, Div
from shtml_sdk.sui import Sui
from rich import print

# Div: 0x9a2fc204379dc2990c955be06082de7fecc5ffb4a7a1d7b899ec4ce69f825c79
# P: 0x14151113fb04ff03957cf04108ea80f0930f4288e09fe82551924c7527e1137b

TYPES = {
    "div": f"{PACKAGE_ID}::div::Div",
    "img": f"{PACKAGE_ID}::img::Img",
    "p": f"{PACKAGE_ID}::p::P",
}


class Shtml(Sui):
    def __init__(self) -> None:
        super().__init__()

    def create_div(
        self,
        recipient: SuiAddress | None = None,
    ):
        if not recipient:
            recipient = self.config.active_address

        txer = SuiTransaction(
            client=self.client,
            compress_inputs=True,
        )

        div_element = txer.move_call(
            target=f"{PACKAGE_ID}::div::create",
            arguments=[],
        )

        txer.transfer_objects(
            transfers=[div_element],
            recipient=recipient,
        )

        result = handle_result(
            txer.execute(),
        )

        return result

    def add_child_to_div(
        self,
        div: Div,
        child: Div | Img | P,
    ):
        txer = SuiTransaction(
            client=self.client,
            compress_inputs=True,
        )

        txer.move_call(
            target=f"{PACKAGE_ID}::div::add_child",
            arguments=[ObjectID(child.id), ObjectID(div.id)],
            type_arguments=[self.get_struct_type(child)],
        )

        result = handle_result(
            txer.execute(),
        )

        return result

    def create_img(
        self,
        img: Img,
        recipient: SuiAddress | None = None,
    ):
        if not recipient:
            recipient = self.config.active_address

        txer = SuiTransaction(
            client=self.client,
            compress_inputs=True,
        )

        alt = txer.move_call(
            target="0x1::option::some" if img.alt else "0x1::option::none",
            arguments=[SuiString(img.alt)] if img.alt else [],
            type_arguments=["0x1::string::String"],
        )

        crossorigin = txer.move_call(
            target="0x1::option::some" if img.crossorigin else "0x1::option::none",
            arguments=[SuiString(img.crossorigin)] if img.crossorigin else [],
            type_arguments=["0x1::string::String"],
        )

        decoding = txer.move_call(
            target="0x1::option::some" if img.decoding else "0x1::option::none",
            arguments=[SuiString(img.decoding)] if img.decoding else [],
            type_arguments=["0x1::string::String"],
        )

        height = txer.move_call(
            target="0x1::option::some" if img.height else "0x1::option::none",
            arguments=[SuiString(img.height)] if img.height else [],
            type_arguments=["u64"],
        )

        loading = txer.move_call(
            target="0x1::option::some" if img.loading else "0x1::option::none",
            arguments=[SuiString(img.loading)] if img.loading else [],
            type_arguments=["0x1::string::String"],
        )

        referrerpolicy = txer.move_call(
            target="0x1::option::some" if img.referrerpolicy else "0x1::option::none",
            arguments=[SuiString(img.referrerpolicy)] if img.referrerpolicy else [],
            type_arguments=["0x1::string::String"],
        )

        title = txer.move_call(
            target="0x1::option::some" if img.title else "0x1::option::none",
            arguments=[SuiString(img.title)] if img.title else [],
            type_arguments=["0x1::string::String"],
        )

        usemap = txer.move_call(
            target="0x1::option::some" if img.usemap else "0x1::option::none",
            arguments=[SuiString(img.usemap)] if img.usemap else [],
            type_arguments=["0x1::string::String"],
        )

        width = txer.move_call(
            target="0x1::option::some" if img.width else "0x1::option::none",
            arguments=[SuiString(img.width)] if img.width else [],
            type_arguments=["u64"],
        )

        img_element = txer.move_call(
            target=f"{PACKAGE_ID}::img::create",
            arguments=[
                alt,
                crossorigin,
                decoding,
                height,
                img.ismap,
                loading,
                referrerpolicy,
                img.src,
                title,
                usemap,
                width,
            ],
        )

        txer.transfer_objects(
            transfers=[img_element],
            recipient=recipient,
        )

        result = handle_result(
            txer.execute(),
        )

        return result

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

    def fetch_objects_for_address(
        self,
        element_model: Div | Img | P,  # div, img, p
        address: str | None = None,
        show_type: bool = False,
        show_owner: bool = False,
        show_previous_transaction: bool = False,
        show_display: bool = False,
        show_content: bool = False,
        show_bcs: bool = False,
        show_storage_rebate: bool = False,
    ) -> list[ObjectRead]:
        if not address.startswith("0x"):
            address = self.config.active_address

        query = {
            "filter": {
                "StructType": self.get_struct_type_from_element_model(element_model),
            },
            "options": {
                "showType": show_type,
                "showOwner": show_owner,
                "showPreviousTransaction": show_previous_transaction,
                "showDisplay": show_display,
                "showContent": show_content,
                "showBcs": show_bcs,
                "showStorageRebate": show_storage_rebate,
            },
        }

        builder = GetObjectsOwnedByAddress(
            address=address,
            query=query,
        )

        result = handle_result(
            self.client.execute(builder),
        )

        if isinstance(result, ObjectReadPage):
            return result.data

    def fetch(
        self,
        object_id: str,
    ) -> Div | P | Img:
        # Fetch object from the blockchain.
        obj = handle_result(
            self.client.get_object(
                ObjectID(object_id),
            )
        )

        if obj.object_type == f"{PACKAGE_ID}::div::Div":
            element = self.build_div(obj)
        if obj.object_type == f"{PACKAGE_ID}::p::P":
            element = self.build_p(obj)

        return element

    def get_struct_type(
        self,
        element: Div | P | Img,
    ):
        return TYPES[type(element).__name__.casefold()]

    def get_struct_type_from_element_model(
        self,
        model: Div | P | Img,
    ):
        return TYPES[model.__name__.casefold()]

    def render(
        self,
        id: str,
        version: SuiInteger | None = None,
    ) -> str:
        obj = handle_result(
            self.client.get_object(
                ObjectID(id),
                version=version,
            )
        )

        if not isinstance(obj, ObjectRead):
            raise Exception(f"Unable to read object {id}...")

        html = None

        element = self.fetch(obj.object_id)

        if obj.object_type == f"{PACKAGE_ID}::div::Div":
            html = self._render_div(element)
        if obj.object_type == f"{PACKAGE_ID}::img::Img":
            html = self._render_img(element)
        if obj.object_type == f"{PACKAGE_ID}::p::P":
            html = self._render_p(element)

        if not html:
            raise Exception(f"Object type ({obj.object_type}) not supported...")

        return html

    def build_div(
        self,
        obj: ObjectRead,
    ) -> Div:
        div = Div(
            id=obj.object_id,
            order=obj.content.fields["order"],
        )

        return div

    def build_img(
        self,
        obj: ObjectRead,
    ) -> Img:
        img = Img(
            id=obj.object_id,
            alt=obj.content.fields["alt"],
            crossorigin=obj.content.fields["crossorigin"],
            decoding=obj.content.fields["decoding"],
            height=obj.content.fields["height"],
            ismap=obj.content.fields["ismap"],
            loading=obj.content.fields["loading"],
            referrerpolicy=obj.content.fields["referrerpolicy"],
            src=obj.content.fields["src"],
            title=obj.content.fields["title"],
            usemap=obj.content.fields["usemap"],
            width=obj.content.fields["width"],
        )

        return img

    def build_p(
        self,
        obj: ObjectRead,
    ) -> P:
        p = P(
            id=obj.object_id,
            content=obj.content.fields["content"],
        )

        return p

    def _render_div(
        self,
        div: Div,
    ):
        child_html = []
        for child_id in div.order:
            element = self.fetch(child_id)
            if isinstance(element, P):
                html = self._render_p(element)
                child_html.append(html)

        html = f'<div id="{div.id}">{"".join(child_html)}</div>'
        return html

    def _render_img(
        self,
        img: Img,
    ) -> str:
        optional_attrs = []

        if img.alt:
            optional_attrs.append(f'alt="{img.alt}"')
        if img.crossorigin:
            optional_attrs.append(f'crossorigin="{img.crossorigin}"')
        if img.decoding:
            optional_attrs.append(f'decoding="{img.decoding}"')
        if img.height:
            optional_attrs.append(f'height="{img.height}"')
        if img.ismap:
            optional_attrs.append("ismap")
        if img.loading:
            optional_attrs.append(f'loading="{img.loading}"')
        if img.referrerpolicy:
            optional_attrs.append(f'referrerpolicy="{img.referrerpolicy}"')
        if img.title:
            optional_attrs.append(f'title="{img.title}"')
        if img.usemap:
            optional_attrs.append(f'usemap="{img.usemap}"')
        if img.width:
            optional_attrs.append(f'width="{img.width}"')

        if img.src.startswith("miraifs://"):
            img.src = img.src.replace(
                "miraifs://",
                f"https://{MIRAIFS_GATEWAY_HOSTNAME}/",
            )

        html = f'<img id="{img.id}" src="{img.src}" {" ".join(optional_attrs)}/>'
        return html

    def _render_p(
        self,
        p: P,
    ) -> str:
        html = f'<p id="{p.id}">{p.content}</p>'
        return html
