from pydantic import BaseModel, Field

class SameName(BaseModel):
    region: list[str] = Field(description="List of recognized regions from the query")
    keyword: str = Field(description="Keywords excluding regional information from the query")
    selected_region: str = Field(description="Selected region from the list of recognized regions")

class Meta(BaseModel):
    total_count: int = Field(description="total number of items in the response")
    pageable_count: int = Field(description="number of exposed items")
    is_end: bool = Field(description="indicates if the current page is the last page of results")
    same_name: SameName | None = Field(default=None, description="information about the same name query, if applicable")