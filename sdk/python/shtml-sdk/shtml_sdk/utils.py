from bs4 import BeautifulSoup


def beautify_html(
    html: str,
):
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()
