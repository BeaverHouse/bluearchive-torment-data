import polars as pl

from app.parse.rank import get_rank_season
import app.constants as constants

def get_party_info(season: str, develop: bool = False) -> dict:
    """
    Get party data

    Args:
        season (str): season starts with "S" or "3S".
        develop (bool): parameter that indicates if the data is for development or not.
    """
    target_boss, rank_df = get_rank_season(season)

    if target_boss == 0:
        update_party_info_normal(season, rank_df, develop)
    else:
        update_party_info_triple(season, target_boss, rank_df, develop)
    
def update_party_info_normal(season: str, rank_df: pl.DataFrame, develop: bool = False):
    url = f"{constants.DATA_BASE_URL}/RaidRankData/{season}/TeamDataDetail_Original.csv"

    party_df = pl.read_csv(url)
    pass

def update_party_info_triple(season: str, target_boss: int, rank_df: pl.DataFrame, develop: bool = False):
    url = f"{constants.DATA_BASE_URL}/RaidRankDataER/{season}/TeamDataDetailBoss{target_boss}_Original.csv"

    party_df = pl.read_csv(url)
    pass