import time
from database.sqlite_store import get_conn
from datetime import datetime


def record_metrics(state, start_time):
    latency = time.time() - start_time

    conn = get_conn()
    conn.execute(
        "INSERT INTO metrics VALUES (NULL,?,?,?,?)",
        (latency, 0, 1, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

    state["logs"].append(f"📈 Latency: {latency:.2f}s")
    return state