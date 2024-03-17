import csv
import json
import os
import collections

# 빈 셀 확인하는 함수
def is_cell_blank(value) -> bool:
    return value is None or len(str(value).strip()) <= 0

# 파티가 존재하는지 확인하는 함수
# 스트라이커만 있어도 유효 파티
def party_exists(row, i:int) -> bool:
    if (i+1)*44 + 2 > len(row): return False
    return not (
        is_cell_blank(row[i*44+4]) and \
        is_cell_blank(row[i*44+11]) and \
        is_cell_blank(row[i*44+18]) and \
        is_cell_blank(row[i*44+25])
    )

def get_char_name(char_json, id) -> str:
    return char_json[str(id)] if not is_cell_blank(id) else ""

def get_category(star: int, weapon: int) -> int:
    """
    Calculate the category based on the character's star and weapon levels.
    """
    return 9 - star if star < 5 else 5 - weapon

def parse_main():
    with open('character.json', encoding='utf-8') as f:
        char_json = json.load(f)

    for file in os.listdir('rawdetail'):
        f_csv = open(f"rawdetail/{file}",'r')
        reader = csv.reader(f_csv)

        # 캐릭터 필터 저장용
        filters = collections.defaultdict(lambda: [0]*9)
        assist_filters = collections.defaultdict(lambda: [0]*9)

        # 전체 파티 저장용
        total_partys = []
        max_party_cnt = -1
        min_party_cnt = 1000

        # 이전 점수 저장용
        score_cut = 86000000 if file.startswith("S3") else 35500000
        
        for idx, row in enumerate(reader):
            if idx == 0 : continue

            dic = {}

            score = int(row[1])

            # Cut by score or max 2000 rows
            if idx > 2000 or score_cut > score: break

            if is_cell_blank(row[0]): break

            # 점수 순위 저장
            dic["rank"] = int(row[0])
            dic["score"] = int(row[1])

            i = 0
            partys = []
            search_keys = set()
                
            # 파티가 존재하면 파티 추가
            while party_exists(row, i):
                members = []
                for slot in range(6):
                    begin_idx = i*44 + slot*7 + 4
                    _, id, star, _, _, weapon, is_assist = row[begin_idx:begin_idx + 7]
                    
                    if is_cell_blank(id): continue
                    
                    name = get_char_name(char_json=char_json, id=id)
                    category = get_category(star=int(star), weapon=int(weapon))
                    search_key = f'{name}_{category}'

                    if is_assist.upper() == "TRUE":
                        dic["assist"] = search_key
                        assist_filters[name][category] += 1
                    else:
                        filters[name][category] += 1
                        search_keys.add(search_key)
                    
                    members.append({
                        "name": name,
                        "category": category,
                        **({'assist': True} if is_assist.upper() == "TRUE" else {})
                    })

                partys.append({
                    "members": members,
                    "attempt": i+1
                })
                
                i += 1

            dic["partys"] = partys
            dic["search_keys"] = list(search_keys)
            dic["party_count"] = len(partys)
            if len(partys) > max_party_cnt: max_party_cnt = len(partys)
            if len(partys) < min_party_cnt: min_party_cnt = len(partys)

            print(".", end="")
            total_partys.append(dic)
            
        total_json = {
            "filter": collections.OrderedDict(sorted(filters.items())),
            "assist_filter": collections.OrderedDict(sorted(assist_filters.items())),
            "partys": total_partys,
            "min_party": min_party_cnt,
            "max_party": max_party_cnt
        }

        # JSON 저장
        with open(f"result_detail/{file.replace("D.csv", "")}.json", "w", encoding='utf-8') as f:
            json.dump(total_json, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    parse_main()