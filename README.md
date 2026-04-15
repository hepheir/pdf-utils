# pdf-utils

여러 개의 PDF 파일을 GUI 파일 다이얼로그로 선택하여 하나로 병합하는 도구입니다.

## 요구사항

- Python 3.12 이상
- [uv](https://docs.astral.sh/uv/)

## 설치

```bash
uv sync
```

## 실행

```bash
uv run main.py
```

## 사용 방법

1. 실행하면 PDF 파일 선택 다이얼로그가 열립니다.
2. 병합할 PDF 파일을 **순서대로** 선택합니다 (Ctrl 또는 Shift 클릭으로 다중 선택).
3. 저장할 파일 경로와 이름을 지정합니다.
4. 완료 메시지가 뜨면 지정한 경로에 병합된 PDF가 저장됩니다.

## 의존성

- [pypdf](https://pypdf.readthedocs.io/): PDF 병합 처리
