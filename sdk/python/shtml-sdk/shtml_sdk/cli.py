import typer
from pysui.sui.sui_txresults.single_tx import ObjectRead

from shtml_sdk.shtml import Shtml
from shtml_sdk.models.html_elements import P

from rich import print

app = typer.Typer()

shtml = Shtml()


@app.command()
def hello():
    print("Hello, world!")
    return


@app.command(
    name="p",
)
def create_p(
    content: str,
):
    p = P(content=content)

    result = shtml.create_p(p)
    print(result)
    return


@app.command()
def render(
    id: str,
):
    result = shtml.render(id)
    print(result)
    return
