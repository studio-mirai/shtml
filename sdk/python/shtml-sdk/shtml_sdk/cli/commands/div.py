import typer
from shtml_sdk.models.html_elements import Div, P, Img
from shtml_sdk import DOWNLOADS_DIR
from shtml_sdk.cli import shtml, console
from shtml_sdk.utils import beautify_html
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

app = typer.Typer()


@app.command(
    name="fetch-all",
)
def fetch_divs_for_address(
    address: str = typer.Option(
        "",
        help="Address to fetch divs for.",
    ),
):
    objs = shtml.fetch_objects_for_address(
        Div,
        address,
        show_type=True,
        show_content=True,
        show_previous_transaction=True,
        show_storage_rebate=True,
    )

    print(f"Found {len(objs)} Div objects!")

    for obj in objs:
        console.print("".join(["-"] * 80))
        console.print(f"Object ID: {obj.object_id}")
        console.print(f"Version: {obj.version}")
        console.print(f"Storage Rebate: {int(obj.storage_rebate) / 10**9} SUI")
        console.print(f"Previous TX: {obj.previous_transaction}")
        console.print("")
        console.print(f"{beautify_html(shtml.render(obj.object_id)).rstrip("\n")}")

    return


@app.command(
    name="add-child",
)
def add_child_to_div(
    child_id: str = typer.Argument(...),
    div_id: str = typer.Argument(...),
):
    div = shtml.fetch(div_id)
    child = shtml.fetch(child_id)
    shtml.add_child_to_div(div, child)
    return


@app.command(
    name="create",
)
def create_div():
    result = shtml.create_div()
    print(result)
    return
