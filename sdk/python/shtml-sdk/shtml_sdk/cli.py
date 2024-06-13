import typer
from shtml_sdk.shtml import Shtml
from shtml_sdk.models.html_elements import P, Img
from shtml_sdk import DOWNLOADS_DIR
from shtml_sdk.utils import beautify_html

from rich import print

app = typer.Typer()

shtml = Shtml()


@app.command()
def hello():
    print("Hello, world!")
    return


@app.command(
    name="div",
)
def create_div():
    result = shtml.create_div()
    print(result)
    return


@app.command(
    name="div-add-child",
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
    name="img",
)
def create_img(
    src: str = typer.Argument(...),
):
    img = Img(
        src=src,
    )
    result = shtml.create_img(img)
    print(result)
    return


@app.command(
    name="p",
)
def create_p(
    content: str,
):
    p = P(
        content=content,
    )

    result = shtml.create_p(p)
    print(result)
    return


@app.command()
def fetch(
    object_id: str,
):
    obj = shtml.fetch(object_id)
    print(obj)
    return


@app.command()
def render(
    id: str,
    save: bool = typer.Option(
        False,
        "--save",
        "-s",
    ),
):
    html = shtml.render(id)
    print(beautify_html(html))

    if save:
        print(f"Writing HTML element to {DOWNLOADS_DIR / f'{id}.html'}")
        with open(DOWNLOADS_DIR / f"{id}.html", "w+") as f:
            f.write(html)

    return
