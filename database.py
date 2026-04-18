"""
📌 Database Module - Naukri Automation Bot

This module is responsible for:
- Creating and managing the local SQLite database
- Tracking jobs that have already been applied
- Preventing duplicate job applications

Database Used:
- SQLite (lightweight, file-based database)

Table:
- jobs (stores applied job URLs)

⚠️ NOTE:
- Each job URL is stored as PRIMARY KEY to avoid duplicates
"""

import sqlite3

# Database file name
DB = "applied_jobs.db"


def get_conn():
    """
    🔌 Create and return a new database connection.

    Returns:
        sqlite3.Connection: Database connection object

    NOTE:
    - Each function creates its own connection (simple and safe approach)
    """
    return sqlite3.connect(DB)


def init_db():
    """
    🏗️ Initialize the database and create required tables.

    Table: jobs
    Columns:
        - url (TEXT, PRIMARY KEY)

    Purpose:
    - Ensures table exists before any operations
    - Prevents errors during runtime
    """
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            url TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()


def is_applied(url):
    """
    🔍 Check if a job has already been applied.

    Args:
        url (str): Job URL

    Returns:
        bool:
            True  → if already applied
            False → if not applied

    Logic:
    - Query database using job URL
    - If record exists → already applied
    """
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM jobs WHERE url=?", (url,))
    r = cur.fetchone()

    conn.close()

    return r is not None


def mark_applied(url):
    """
    ✅ Mark a job as applied by inserting it into the database.

    Args:
        url (str): Job URL

    Logic:
    - Insert job URL into 'jobs' table
    - Uses 'INSERT OR IGNORE' to avoid duplicate errors

    Why OR IGNORE?
    - If same job is inserted again → it will be ignored
    - Prevents crashes and duplicate entries
    """
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT OR IGNORE INTO jobs(url) VALUES (?)", (url,))

    conn.commit()
    conn.close()


# 🚀 Initialize database when module is loaded
init_db()