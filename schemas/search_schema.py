from pydantic import BaseModel


class SearchResult(BaseModel):

    module: str

    id: int

    title: str


class SearchResponse(BaseModel):

    results: list[SearchResult]