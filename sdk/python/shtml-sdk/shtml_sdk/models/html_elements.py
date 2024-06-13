from pydantic import BaseModel


class Div(BaseModel):
    id: str
    order: list[str] = []


class Img(BaseModel):
    alt: str | None = None
    crossorigin: str | None = None
    decoding: str | None = None
    height: int | None = None
    ismap: bool = False
    loading: str | None = None
    referrerpolicy: str | None = None
    sizes: list["ImgSizesValue"] = []
    src: str
    srcset: list["ImgSrcsetValue"] = []
    title: str | None = None
    usemap: str | None = None
    width: int | None = None


class ImgSizesValue(BaseModel):
    condition: str | None
    size: int


class ImgSrcsetValue(BaseModel):
    src: str
    width: int


class P(BaseModel):
    id: str | None = None
    content: str
