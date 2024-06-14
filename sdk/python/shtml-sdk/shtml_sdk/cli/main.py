import typer

from shtml_sdk.cli import console, shtml
from shtml_sdk.models.html_elements import P, Img
from shtml_sdk import DOWNLOADS_DIR
from shtml_sdk.shtml import Shtml
from shtml_sdk.utils import beautify_html

from html2text import html2text
from rich import print

from rich.markdown import Markdown
from shtml_sdk.cli.commands import div

app = typer.Typer()
app.add_typer(div.app, name="div")


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
    format: str = typer.Option("md", "--format", "-f"),
):
    html = shtml.render(id)
    formatted_html = beautify_html(html)

    if format == "html":
        console.print(formatted_html)
    else:
        console.print(Markdown(html2text(html)))

    if save:
        print(f"Writing HTML element to {DOWNLOADS_DIR / f'{id}.html'}")
        with open(DOWNLOADS_DIR / f"{id}.html", "w+") as f:
            f.write(beautify_html(html))

    return
