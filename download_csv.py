import requests
import os
from parse_party import parse_main

baseURL = "https://storage.googleapis.com/info.herdatasam.me"
types = ["폭발", "관통", "신비"]

def get_csv(category: str, type: str, season: int):
    os.makedirs("rawdetail", exist_ok=True)

    url, file_name = "", ""
    if category == "총력전":
        url = f"{baseURL}/BlueArchiveJP/RaidRankData/S{season}/TeamDataDetail_Original.csv"
        file_name = f"S{season}D.csv"
    else:
        type_idx = types.index(type)+1
        file_name = f"3S{season}-TD.csv"
        url = f"{baseURL}/BlueArchiveJP/RaidRankDataER/S{season}/TeamDataDetailBoss{type_idx}_Original.csv"
    
    res = requests.get(url)
    if res.ok:
        with open(f"rawdetail/{file_name}", "wb") as f:
            f.write(res.content)

        parse_main()


if __name__ == "__main__":
    # 24.03.13. ~ 24.03.20. 시가지 비나 (Torment 방어타입: 특수장갑)
    category: str   = "대결전"
    type: str       = "신비"         
    # season: int     = 63            # 총력전
    season: int     = 8            # 대결전
    
    get_csv(category=category, type=type, season=season)