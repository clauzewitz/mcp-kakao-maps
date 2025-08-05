# 카카오지도 MCP

이 프로젝트는 카카오지도를 연동한 MCP 입니다. 이를 활용하여 장소 조회 등을 쉽게 조회할 수 있습니다.

## 기능

- 장소 조회

## 사용 방법

python 직접 실행
```
{
    "servers": {
        "kakao-maps": {
            "command": "python",
            "args": ["-m", " src.kakao_maps.server.py"],
            "env": {
                "KAKAO_API_KEY": "Enter your KAKAO API Key here.",
            }
        }
    }
}
```

Docker를 이용한 실행
```
{
    "servers": {
        "kakao-maps": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-e",
                "KAKAO_API_KEY",
                "kakao-maps:latest"
            ],
            "env": {
                "KAKAO_API_KEY": "Enter your KAKAO API Key here.",
            }
        }
    }
}
```

## 라이선스

이 프로젝트는 [MIT](LICENSE) 라이선스에 따라 배포됩니다.

## 참고

- 이 프로젝트는 카카오 지도의 공식 API를 사용합니다.
- API 사용에 대한 자세한 정보는 카카오 개발자 포털을 참조하세요.
