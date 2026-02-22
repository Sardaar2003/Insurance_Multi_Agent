from database.sqlite_store import get_conn
from datetime import datetime


def send_message(sender, receiver, message):
    conn = get_conn()
    conn.execute(
        "INSERT INTO agent_messages VALUES (NULL,?,?,?,?)",
        (sender, receiver, message, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def get_messages(agent_name):
    conn = get_conn()
    cur = conn.execute(
        "SELECT message FROM agent_messages WHERE receiver=?",
        (agent_name,)
    )
    msgs = [m[0] for m in cur.fetchall()]
    conn.close()
    return msgs