<p align="center">
  <a href="https://github.com/BeaverHouse/bluearchive-torment-data">
    <img src="logo.png" alt="Logo">
  </a>

  <p align="center">
    Data & processing code for BA Torment
    <br>
    <br>
    <a href="https://github.com/BeaverHouse/bluearchive-torment-data/issues">Bug Report</a>
    |
    <a href="https://github.com/BeaverHouse/bluearchive-torment-data/issues">Request to HU-Lee</a>
  </p>

  <p align="center">
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    </a>
    <a href="https://python-poetry.org/">
      <img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat&logo=Poetry&logoColor=white" alt="Poetry">
    </a>
    <a href="https://docs.pytest.org/en/8.0.x/">
      <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
    </a>
    <a href="./LICENSE">
      <img src="https://img.shields.io/github/license/BeaverHouse/bluearchive-torment-data" alt="License">
    </a>
  </p>
</p>

<!-- Content -->

<br>

## Description

**❗❗This app is KOREAN only.❗❗**

블루아카이브 토먼트 파티찾기의 데이터 저장소입니다.

총력전/대결전 데이터는 [외부 API]에서 원본 데이터를 받아 Python으로 가공하고 있습니다.  
⚠ 문제시 링크가 삭제될 수 있습니다.

캐릭터 정보는 [Schale DB] 소스에서 받아오고 있습니다.

[외부 API]: https://storage.googleapis.com/info.herdatasam.me
[Schale DB]: https://github.com/lonqie/SchaleDB

<br>

## Requirements

1. You need to install [Python 3.12] and [Poetry] to manage the packages.  
   To install Poetry:

   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. You need to set repository secret to run GitHub Actions.

   - `GH_PAT_ORGANIZATION` : fine-grained access token for organization repositories

<br>

**Create virtual environment**

```
poetry shell
```

**Install packages**

```
poetry install
```

[Poetry]: https://python-poetry.org/
[Python 3.12]: https://www.python.org/downloads/release/python-3120/

<br>

## Contributing

See the [CONTRIBUTING.md][contributing].

[contributing]: ./CONTRIBUTING.md
