from enum import StrEnum


class AddressType(StrEnum):
    REGION = "REGION"  # 지명
    ROAD = "ROAD"  # 도로명
    REGION_ADDR = "REGION_ADDR"  # 지번 주소
    ROAD_ADDR = "ROAD_ADDR"  # 도로명 주소

class YesOrNoType(StrEnum):
    Y = "Y"  # Yes
    N = "N"  # No

class CategoryGroupCodeType(StrEnum):
    MART = "MT1"  # 대형마트
    CONVENIENCE_STORE = "CS2"  # 편의점
    KINDER_GARTEN = "PS3"  # 어린이집, 유치원
    SCHOOL = "SC4"  # 학교
    ACADEMY = "AC5"  # 학원
    PARKING_LOT = "PK6"  # 주차장
    PETROL_STATION = "OL7"  # 주유소, 충전소
    SUBWAY_STATION = "SW8"  # 지하철역
    BANK = "BK9"  # 은행
    CULTURAL_FACILITIES = "CT1"  # 문화시설
    BROKERAGE = "AG2"  # 중개업소
    PUBLIC_INSTITUTION = "PO3"  # 공공기관
    TOURIST_ATTRACTION = "AT4"  # 관광명소
    ACCOMMODATION = "AD5"  # 숙박
    RESTAURANT = "FD6"  # 음식점
    CAFE = "CE7"  # 카페
    HOSPITAL = "HP8"  # 병원
    PHARMACY = "PM9"  # 약국

class CoordType(StrEnum):
    WGS84 = "WGS84"  # WGS84 좌표계
    WCONGNAMUL = "WCONGNAMUL"  # 원주율 좌표계
    CONGNAMUL = "CONGNAMUL"  # 원주율 좌표계
    WTM = "WTM"  # WTM 좌표계
    TM = "TM"  # TM 좌표계
    KTM = "KTM"  # KTM 좌표계
    UTM = "UTM"  # UTM 좌표계
    BESSEL = "BESSEL"  # Bessel 좌표계
    WKTM = "WKTM"  # WKTM 좌표계
    WUTM = "WUTM"  # WUTM 좌표계