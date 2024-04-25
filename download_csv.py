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
    # 24.05.01. ~ 24.05.08. SEASON #65 시가지 호드
    category: str   = "총력전"
    type: str       = "관통"         
    season: int     = 65            # 총력전
    # season: int     = 9            # 대결전
    
    get_csv(category=category, type=type, season=season)