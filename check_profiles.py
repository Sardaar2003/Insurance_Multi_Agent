# check_profiles.py
from database.sqlite_store import get_conn

conn = get_conn()

rows = conn.execute("SELECT * FROM user_profiles").fetchall()

print(rows)

conn.close()