import requests
from app.oracle import get_oracle


def update_student_info(develop: bool = False) -> dict:
    """
    Update character id and name from SchaleDB
    """
    res = requests.get("https://schaledb.com/data/kr/students.min.json")

    student_info = list(map(
        lambda x: (int(x["Id"]), x["Name"]),
        res.json().values()
    ))

    table_name = "dev_ba_students" if develop else "ba_students" 

    with get_oracle() as conn:
        cur = conn.cursor()
        current_ids = list(map(lambda x: x[0], cur.execute(f"SELECT student_id FROM {table_name}").fetchall()))

        cur.executemany(
            f"INSERT INTO {table_name} (student_id, name) VALUES(:1, :2)",
            [(id, name) for id, name in student_info if id not in current_ids]
        )
        conn.commit()

    return dict(student_info)