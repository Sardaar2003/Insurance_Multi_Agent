"""
Enterprise Insurance Multi-Agent UI
-----------------------------------

Features:
- User/Admin login
- Role based UI
- Admin console (multi-file RAG upload, audit logs, metrics)
- Profile fetch
- General insurance Q&A
- Spinner + process tracking
"""

import streamlit as st
import uuid
import sqlite3
import time
from dotenv import load_dotenv
load_dotenv()
import os
print(os.getenv("OPENAI_API_KEY"))

from database.sqlite_store import init_db, get_conn, insert_audit, insert_metrics
from agents.executor_agent import run_executor_agent
from agents.general_agent import run_general_agent
from rag.vector_store import add_document
from rag.document_loader import extract_text


# ============================================================
# INIT
# ============================================================

init_db()

st.set_page_config(
    page_title="Enterprise Insurance AI",
    layout="wide"
)

# session init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())


# ============================================================
# LOGIN PAGE
# ============================================================

if not st.session_state.logged_in:

    st.title("🔐 Enterprise Insurance Platform Login")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            conn = get_conn()

            row = conn.execute(
                "SELECT role FROM users WHERE username=? AND password=?",
                (username, password)
            ).fetchone()

            conn.close()

            if row:
                st.session_state.logged_in = True
                st.session_state.user_id = username
                st.session_state.role = row[0]

                insert_audit("LOGIN", f"user={username}")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()


# ============================================================
# MAIN UI
# ============================================================

st.title("🏦 Enterprise Insurance AI Assistant")

# sidebar
with st.sidebar:
    st.success(f"Logged in as: {st.session_state.user_id}")
    st.write("Role:", st.session_state.role)

    if st.button("Logout"):
        insert_audit("LOGOUT", f"user={st.session_state.user_id}")
        st.session_state.clear()
        st.rerun()


# ============================================================
# ADMIN CONSOLE
# ============================================================

if st.session_state.role == "admin":

    st.divider()
    st.header("🛠 Enterprise Admin Console")

    tab1, tab2, tab3 = st.tabs([
        "📚 Knowledge Upload",
        "📊 Audit Logs",
        "📈 Metrics Dashboard"
    ])

    # ========================================================
    # MULTI FILE RAG UPLOAD
    # ========================================================
    with tab1:

        st.subheader("Upload Knowledge Documents")

        uploaded_files = st.file_uploader(
            "Upload PDF / DOCX / TXT files",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True
        )

        if uploaded_files:

            if st.button("Process Documents"):

                with st.spinner("Indexing documents..."):

                    count = 0
                    for file in uploaded_files:
                        text = extract_text(file)
                        if text:
                            add_document(text)
                            count += 1

                insert_audit(
                    "DOCUMENT_UPLOAD",
                    f"{count} documents uploaded by {st.session_state.user_id}"
                )

                st.success(f"{count} documents indexed successfully")

    # ========================================================
    # AUDIT LOGS
    # ========================================================
    with tab2:

        st.subheader("System Audit Logs")

        conn = sqlite3.connect("insurance.db")

        rows = conn.execute(
            "SELECT * FROM audit_logs ORDER BY id DESC LIMIT 100"
        ).fetchall()

        conn.close()

        if rows:
            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No audit logs available")

    # ========================================================
    # METRICS
    # ========================================================
    with tab3:

        st.subheader("System Metrics")

        conn = sqlite3.connect("insurance.db")

        rows = conn.execute(
            "SELECT * FROM metrics ORDER BY id DESC LIMIT 100"
        ).fetchall()

        conn.close()

        if rows:
            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No metrics available")


# ============================================================
# CHAT INTERFACE
# ============================================================

st.divider()
st.header("💬 Ask Assistant")

query = st.text_input(
    "Ask about insurance, policies, or your profile"
)

if st.button("Run Query") and query:

    state = {
        "user_input": query,
        "user_id": st.session_state.user_id,
        "role": st.session_state.role,
        "final_response": "",
        "logs": []
    }

    process_text = st.empty()

    start_time = time.time()

    with st.spinner("Processing request..."):

        # STEP 1 — understand query
        process_text.info("⚙️ Understanding request...")
        time.sleep(0.5)

        # STEP 2 — route request
        if "profile" in query.lower():

            process_text.info("⚙️ Fetching user profile...")
            result = run_executor_agent(state)

        else:

            process_text.info("⚙️ Generating AI response...")
            result = run_general_agent(state)

        time.sleep(0.5)

    latency = time.time() - start_time

    insert_metrics(latency)

    process_text.success("✅ Completed")

    st.subheader("Response")
    st.write(result.get("final_response"))

    insert_audit(
        "QUERY_EXECUTED",
        f"user={st.session_state.user_id} query={query}"
    )