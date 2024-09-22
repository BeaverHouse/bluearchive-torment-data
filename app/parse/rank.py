from typing import Tuple
import polars as pl

import app.constants as constants


def get_rank_season(season: str) -> Tuple[int, pl.DataFrame]:
    """
    Get rank data

    Args:
        season (str): season starts with "S" or "3S".
    """
    if season.startswith("3S"):
        return get_rank_season_triple(season)
    else:
        return get_rank_season_normal(season)


def get_rank_season_normal(season: str) -> Tuple[int, pl.DataFrame]:
    """
    Get "Total Assault (총력전)" rank data
    """
    url = f"{constants.DATA_BASE_URL}/RaidRankData/{season}/FullData_Original.csv"
    
    try:
        df = pl.read_csv(url)
        target_boss = 0
        return target_boss, \
            df.select(pl.col("AccountId", "Rank", "BestRankingPoint")) \
              .filter(pl.col("BestRankingPoint") > constants.TORMENT_MIN_SCORE) \
              .sort(by="BestRankingPoint", descending=True)
    except Exception as e:
        print(e)


def get_rank_season_triple(season: str) -> Tuple[int, pl.DataFrame]:
    """
    Get "Grand Assault (대결전)" rank data
    """
    parsed_season = season[1:]
    url = f"{constants.DATA_BASE_URL}/RaidRankDataER/{parsed_season}/FullData_Original.csv"
    
    try:
        df = pl.read_csv(url, truncate_ragged_lines=True)
        target_boss = -1
        for i in range(1, 4):
            if df.select(pl.first(f"Boss{i}")).item() > constants.TORMENT_MIN_SCORE:
                target_boss = i
                break
        return target_boss, \
            df.select(pl.col("AccountId", "Rank", "BestRankingPoint", f"Boss{target_boss}")) \
              .filter(pl.col(f"Boss{target_boss}") > constants.TORMENT_MIN_SCORE) \
              .sort(by=f"Boss{target_boss}", descending=True)
    except Exception as e:
        print(e)
