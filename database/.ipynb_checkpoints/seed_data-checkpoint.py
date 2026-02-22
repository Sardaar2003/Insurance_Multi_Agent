"""
Database Seeder
Creates login users + matching profiles.
"""

from sqlite_store import get_conn, init_db
import json


# ============================================================
# USERS
# ============================================================

def seed_users():
    conn = get_conn()

    users = [
        ("admin", "admin@123", "admin"),
        ("user1", "pass123", "user"),
        ("user2", "pass123", "user"),
    ]

    for u in users:
        conn.execute(
            "INSERT OR REPLACE INTO users VALUES (?,?,?)",
            u
        )

    conn.commit()
    conn.close()
    print("✅ users seeded")


# ============================================================
# USER PROFILES (MATCH LOGIN USERS)
# ============================================================

def seed_user_profiles():
    conn = get_conn()

    profiles = {
        "user1": {
            "name": "John Doe",
            "policy_number": "POL1001",
            "plan": "Premium",
            "premium": "₹5000/month"
        },
        "user2": {
            "name": "Jane Smith",
            "policy_number": "POL1002",
            "plan": "Gold",
            "premium": "₹7000/month"
        }
    }

    for user_id, profile in profiles.items():
        conn.execute(
            "INSERT OR REPLACE INTO user_profiles VALUES (?,?)",
            (user_id, json.dumps(profile))
        )

    conn.commit()
    conn.close()
    print("✅ user profiles seeded")


# ============================================================
# MASTER
# ============================================================

def seed_all():
    init_db()
    seed_users()
    seed_user_profiles()
    print("🚀 Database ready")


if __name__ == "__main__":
    seed_all()