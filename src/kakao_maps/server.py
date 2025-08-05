import os
from typing import Final

import aiohttp
from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.contrib.mcp_mixin import mcp_tool

from src.kakao_maps.models.document import Address2CoordinatesDocument, Coord2RegionCodeDocument, Coord2AddressDocument, \
    TransCoordDocument, PlacesDocument
from src.kakao_maps.models.type import CategoryGroupCodeType, CoordType

BASE_API_URL: Final = 'https://dapi.kakao.com/v2/local'

if not os.getenv("KAKAO_API_KEY"):
    load_dotenv()

KAKAO_API_KEY: Final = str(os.getenv("KAKAO_API_KEY")).strip()

mcp: Final = FastMCP("kakao_maps")


async def client_session():
    return aiohttp.ClientSession(
        headers={
            'Authorization': f'KakaoAK {KAKAO_API_KEY}'
        }
    )


@mcp_tool("convertAddressToCoordinates")
async def convert_address_to_coordinates(query: str) -> list[Address2CoordinatesDocument] | str:
    """
    주소를 지도 위에 정확하게 표시하기 위해 해당 주소의 좌표 정보를 제공하는 API입니다.
    이 API는 지번 주소, 도로명 주소 모두 지원합니다.

    Args:
        query (str): 주소 질의어로, 지번 주소 또는 도로명 주소를 입력할 수 있습니다.

    Returns:
        List[Address2CoordinatesDocument]: 성공 시 주소 좌표 정보를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/search/address.JSON', query={
                'query': query
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [Address2CoordinatesDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'좌표 정보를 가져올 수 없습니다. 오류: {str(e)}'

@mcp_tool("coordToRegionCode")
async def coord_to_region_code(longitude: str, latitude: str) -> list[Coord2RegionCodeDocument] | str:
    """
    다양한 좌표계에 대한 좌표값을 받아 해당 좌표에 부합하는 행정동, 법정동을 얻는 API입니다.

    Args:
        longitude (str): 경도 값
        latitude (str): 위도 값

    Returns:
        List[Coord2RegionCodeDocument]: 성공 시 좌표에 해당하는 행정동, 법정동 정보를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/geo/coord2regioncode.JSON', query={
                'x': longitude,
                'y': latitude,
                'input_coord': CoordType.WGS84.value,  # 기본적으로 WGS84 좌표계로 변환
                'output_coord': CoordType.WGS84.value  # 기본적으로 WGS84 좌표계로 변환
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [Coord2RegionCodeDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'주소 정보를 가져올 수 없습니다. 오류: {str(e)}'

@mcp_tool("coordToAddress")
async def coord_to_address(longitude: str, latitude: str) -> list[Coord2AddressDocument] | str:
    """
    좌표 정보의 지번 주소와 도로명 주소 정보를 반환하는 API입니다.
    도로명 주소는 좌표에 따라 반환되지 않을 수 있습니다.

    Args:
        longitude (str): 경도 값
        latitude (str): 위도 값

    Returns:
        List[Coord2AddressDocument]: 성공 시 좌표에 해당하는 지번 주소와 도로명 주소 정보를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/geo/coord2address.JSON', query={
                'x': longitude,
                'y': latitude,
                'input_coord': CoordType.WGS84.value  # 기본적으로 WGS84 좌표계로 변환
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [Coord2AddressDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'주소 변환을 할 수 없습니다. 오류: {str(e)}'

@mcp_tool("transCoord")
async def trans_coord(longitude: str, latitude: str) -> list[TransCoordDocument] | str:
    """
    x, y 값과 입력 및 출력 좌표계를 지정해 변환된 좌표 값을 구해, 서로 다른 좌표계간 데이터 호환이 가능하도록 합니다.

    Args:
        longitude (str): 변환할 좌표의 경도 값
        latitude (str): 변환할 좌표의 위도 값

    Returns:
        List[TransCoordDocument]: 성공 시 변환된 좌표 정보를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/geo/transcoord.JSON', query={
                'x': longitude,
                'y': latitude,
                'input_coord': CoordType.WGS84.value,  # 기본적으로 WGS84 좌표계로 변환
                'output_coord': CoordType.WGS84.value  # 기본적으로 WGS84 좌표계로 변환
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [TransCoordDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'좌표 변환을 할 수 없습니다. 오류: {str(e)}'

@mcp_tool("searchPlacesByKeyword")
async def search_places_by_keyword(query: str, category_group_code: CategoryGroupCodeType) -> list[PlacesDocument] | str:
    """
    질의어에 매칭된 장소 검색 결과를 지정된 정렬 기준에 따라 제공합니다.

    Args:
        query (str): 장소 검색을 위한 질의어로, 검색하고자 하는 장소의 이름이나 키워드를 입력합니다.
        category_group_code (CategoryGroupCodeType): 장소 카테고리 그룹 코드로, 특정 카테고리에 속하는 장소를 검색할 때 사용합니다.

    Returns:
        List[PlacesDocument]: 성공 시 장소 검색 결과를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/search/keyword.JSON', {
                'query': query,
                'category_group_code': category_group_code.value
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [PlacesDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'장소 검색을 할 수 없습니다. 오류: {str(e)}'

@mcp_tool("searchPlacesByCategory")
async def search_places_by_category(category_group_code: CategoryGroupCodeType) -> list[PlacesDocument] | str:
    """
    미리 정의된 카테고리 코드에 해당하는 장소 검색 결과를 지정된 정렬 기준에 따라 제공합니다.

    Args:
        category_group_code (CategoryGroupCodeType): 장소 카테고리 그룹 코드

    Returns:
        List[PlacesDocument]: 성공 시 장소 검색 결과를 담은 객체 리스트를 반환합니다.
        str: 오류 발생 시 오류 메시지를 반환합니다.
    """
    try:
        async with client_session() as session:
            async with session.get(f'{BASE_API_URL}/search/category.JSON', {
                'category_group_code': category_group_code.value
            }) as resp:
                resp.raise_for_status()
                response = await resp.json()
                return [PlacesDocument(**document) for document in response.get('documents', [])]
    except Exception as e:
        return f'장소 검색을 할 수 없습니다. 오류: {str(e)}'

if __name__ == "__main__":
    mcp.run(transport="stdio")