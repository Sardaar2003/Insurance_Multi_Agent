"""
SQLite Database Layer
Handles:
- DB connection
- table creation
- audit logging
- metrics logging
"""

import sqlite3
from datetime import datetime

DB_NAME = "insurance.db"


# ============================================================
# CONNECTION
# ============================================================

def get_conn():
    return sqlite3.connect(DB_NAME)


# ============================================================
# INIT DATABASE
# ============================================================

def init_db():
    conn = get_conn()

    # ================= USERS =================
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )
    """)

    # ================= USER PROFILES =================
    conn.execute("""
    CREATE TABLE IF NOT EXISTS user_profiles (
        user_id TEXT PRIMARY KEY,
        profile TEXT
    )
    """)

    # ================= AUDIT LOGS =================
    conn.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        action TEXT,
        details TEXT
    )
    """)

    # ================= METRICS =================
    conn.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latency REAL,
        tokens INTEGER,
        success INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


# ============================================================
# AUDIT INSERT
# ============================================================

def insert_audit(action: str, details: str):
    """
    Insert audit log entry.
    """

    conn = get_conn()

    conn.execute(
        "INSERT INTO audit_logs (timestamp, action, details) VALUES (?,?,?)",
        (datetime.now().isoformat(), action, details)
    )

    conn.commit()
    conn.close()


# ============================================================
# METRICS INSERT
# ============================================================

def insert_metrics(latency: float, tokens: int = 0, success: int = 1):
    """
    Insert metrics record.
    """

    conn = get_conn()

    conn.execute(
        "INSERT INTO metrics (latency, tokens, success, timestamp) VALUES (?,?,?,?)",
        (latency, tokens, success, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()