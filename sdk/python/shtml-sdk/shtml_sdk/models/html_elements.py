from pydantic import BaseModel


class Img(BaseModel):
    id: str | None = None
    alt: str | None
    crossorigin: str | None
    decoding: str | None
    height: int | None
    ismap: bool
    loading: str | None
    referrerpolicy: str | None
    sizes: list["ImgSizesValue"] = []
    src: str
    srcset: list["ImgSrcsetValue"] = []
    title: str | None
    usemap: str | None
    width: int | None


class ImgSizesValue(BaseModel):
    condition: str | None
    size: int


class ImgSrcsetValue(BaseModel):
    src: str
    width: int


class P(BaseModel):
    id: str | None = None
    content: str


class Div(BaseModel):
    id: str | None = None
    children: list[str]
