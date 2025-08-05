from pydantic import BaseModel, Field

from src.kakao_maps.models.type import YesOrNoType, CategoryGroupCodeType


class Address(BaseModel):
    address_name: str = Field(description="name of the address")
    region_1depth_name: str = Field(description="name of the first-level region, e.g., 'Seoul'")
    region_2depth_name: str = Field(description="name of the second-level region, e.g., 'Gangnam-gu'")
    region_3depth_name: str = Field(description="name of the third-level region, e.g., 'Yeoksam-dong'")
    region_3depth_h_name: str = Field(description="name of the third-level region in Hangul, e.g., '역삼동'")
    h_code: str = Field(description="Hanjung code of the address")
    b_code: str = Field(description="bupjung code of the address")
    mountain_yn: YesOrNoType = Field(description="indicates if the address is in a mountainous area, 'Y' for yes, 'N' for no")
    main_address_no: str = Field(description="main address")
    sub_address_no: str = Field(description="sub address")
    zip_code: str = Field(description="postal code of the address")
    x: str = Field(description="longitude of the address")
    y: str = Field(description="latitude of the address")

class RoadAddress(BaseModel):
    address_name: str = Field(description="name of the road address")
    region_1depth_name: str = Field(description="name of the first-level region, e.g., 'Seoul'")
    region_2depth_name: str = Field(description="name of the second-level region, e.g., 'Gangnam-gu'")
    region_3depth_name: str = Field(description="name of the third-level region, e.g., 'Yeoksam-dong'")
    road_name: str = Field(description="name of the road")
    underground_yn: YesOrNoType = Field(description="indicates if the road is underground, 'Y' for yes, 'N' for no")
    main_building_no: str = Field(description="main building number on the road")
    sub_building_no: str = Field(description="sub building number on the road")
    building_name: str = Field(description="name of the building on the road")
    zone_no: str = Field(description="zone number of the road address")
    x: str = Field(description="longitude of the road address")
    y: str = Field(description="latitude of the road address")

class Address2CoordinatesDocument(BaseModel):
    address_name: str = Field(description="name of the address")
    address_type: str = Field(description="type of the address, e.g., 'REGION' for region-based addresses")
    x: str = Field(description="longitude of the address")
    y: str = Field(description="latitude of the address")
    address: Address | None = Field(default=None, description="address of the address")
    road_address: RoadAddress | None = Field(default=None, description="road address of the address, if available")

class Coord2RegionCodeDocument(BaseModel):
    region_type: str = Field(description="type of the region, e.g., 'B' for basic region, 'H' for detailed region")
    address_name: str = Field(description="name of the region")
    region_1depth_name: str = Field(description="name of the first-level region, e.g., 'Seoul'")
    region_2depth_name: str = Field(description="name of the second-level region, e.g., 'Gangnam-gu'")
    region_3depth_name: str = Field(description="name of the third-level region, e.g., 'Yeoksam-dong'")
    region_4depth_name: str = Field(description="name of the fourth-level region, e.g., 'Gangsan-ri' (only exists when region_type is 'B' and the area is village level)")
    code: str = Field(description="code of the region, e.g., '11' for Seoul, '110' for Gangnam-gu")
    x: str = Field(description="longitude of the road address")
    y: str = Field(description="latitude of the road address")

class Coord2AddressDocument(BaseModel):
    address: Address | None = Field(default=None, description="address of the address")
    road_address: RoadAddress | None = Field(default=None, description="road address of the address, if available")

class TransCoordDocument(BaseModel):
    x: str = Field(description="longitude of the address")
    y: str = Field(description="latitude of the address")

class PlacesDocument(BaseModel):
    id: str = Field(description="id of the address")
    place_name: str = Field(description="name of the place")
    category_name: str = Field(description="category name of the place")
    category_group_code: CategoryGroupCodeType = Field(description="category group code of the place")
    category_group_name: str = Field(description="category group name of the place")
    phone: str = Field(description="phone number of the place")
    address_name: str = Field(description="name of the address")
    road_address_name: str = Field(description="name of the road address")
    x: str = Field(description="longitude of the place")
    y: str = Field(description="latitude of the place")
    place_url: str = Field(description="URL of the place")
    distance: str = Field(description="distance from the search point to the place, in meters")
