from bs4 import BeautifulSoup


def beautify_html(
    html: str,
):
    soup = BeautifulSoup(html, "lxml")
    return soup.prettify()
