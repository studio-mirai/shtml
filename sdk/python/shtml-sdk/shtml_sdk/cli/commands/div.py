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


@app.command()
def svg():
    num_rows = 5
    num_cols = 5
    square_size = 50
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    # Generate SVG markup for the grid of colored squares
    def generate_svg():
        svg_content = f'<svg width="{num_cols * square_size}" height="{num_rows * square_size}" xmlns="http://www.w3.org/2000/svg">\n'
        for row in range(num_rows):
            for col in range(num_cols):
                color = colors[(row + col) % len(colors)]  # Alternate colors
                x = col * square_size
                y = row * square_size
                svg_content += f'<rect x="{x}" y="{y}" width="{square_size}" height="{square_size}" fill="rgb{color}"/>\n'
        svg_content += "</svg>"
        return svg_content

    svg_content = generate_svg()

    with open("grid.svg", "w") as svg_file:
        svg_file.write(svg_content)

    return
