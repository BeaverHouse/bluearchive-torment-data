import requests
import json
import os

res = requests.get("https://schaledb.com/data/kr/students.min.json")

res_json = res.json()

result = {}
for e in res_json.values():
    id = e["Id"]
    name = e["Name"]
    result[id] = name.replace("*", "-")

# JSON 저장
with open("character.json", "w", encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)


os.makedirs("image", exist_ok=True)

# IMG 저장
# https://raw.githubusercontent.com/lonqie/SchaleDB/main/images/student/icon/10000.webp
for id, val in result.items():
    url = f'https://schaledb.com/images/student/icon/{id}.webp'
    res = requests.get(url)
    with open(f'image/{val}.webp', "wb") as f:
        f.write(res.content)
    print(".", end="", flush=True)