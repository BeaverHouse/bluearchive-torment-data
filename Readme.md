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

**❗❗ This app is KOREAN Only.❗❗**

Data & processing code for BA Torment.  
It is processed manually and migrated to [frontend repository].

- Raw data: [API] (can be deleted)
- Character info: [Schale DB]

[frontend repository]: https://github.com/BeaverHouse/bluearchive-torment-front
[API]: https://storage.googleapis.com/info.herdatasam.me
[Schale DB]: https://github.com/lonqie/SchaleDB

<br>

## Data information (2024.03)

**Final rank is not same as TORMENT rank in Grand Assault.**

| Category                                 | Value    | Description                |
| ---------------------------------------- | -------- | -------------------------- |
| 총력전 (Total Assault, 総力戦) score cut | 35500000 | > TORMENT 8pt              |
| 대결전 (Grand Assault, 大決戦) score cut | 86000000 | > TORMENT 8pt + INSANE 2pt |
| Max data count                           | 2000     |

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
