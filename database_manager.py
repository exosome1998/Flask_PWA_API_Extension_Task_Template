"""Database manager for SQLite operations."""

import sqlite3 as sql


def list_extension():
    """Retrieve all extensions from database."""
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def insert_extension(
    name,
    hyperlink="http://default.com",
    about="Default description",
    image="default.jpg",
    language="Python",
):
    """Insert a new extension into database."""
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO extension (name, hyperlink, about, image, language) VALUES (?, ?, ?, ?, ?)",
        (name, hyperlink, about, image, language),
    )
    con.commit()
    con.close()
