import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import List, Dict, Any


def get_connection(cfg: Dict[str, Any]) -> MySQLConnection:
    """
    Create and return a MySQLConnection using parameters from cfg.
    cfg should contain:
      - DB_HOST
      - DB_USER
      - DB_PASSWORD
      - DB_PORT
      - DB_NAME
    """
    return mysql.connector.connect(
        host=cfg["DB_HOST"],
        user=cfg["DB_USER"],
        password=cfg["DB_PASSWORD"],
        port=cfg["DB_PORT"],
        database=cfg["DB_NAME"],
        charset="utf8mb4",
        use_unicode=True,
    )

def fetch_tables(conn: MySQLConnection) -> List[Dict[str, Any]]:
    """
    Return a list of dictionaries, each representing one row of SHOW TABLE STATUS.
    Keys include 'Name', 'Comment', etc.
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SHOW TABLE STATUS;")
    tables = cursor.fetchall()
    cursor.close()
    return tables

def fetch_columns(conn: MySQLConnection, table: str) -> List[Dict[str, Any]]:
    """
    Return a list of dictionaries for SHOW FULL COLUMNS FROM `table`.
    Keys include 'Field', 'Type', 'Null', 'Key', 'Default', 'Extra', 'Comment', etc.
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SHOW FULL COLUMNS FROM `{table}`;")
    columns = cursor.fetchall()
    cursor.close()
    return columns

def fetch_indexes(conn: MySQLConnection, table: str) -> List[Dict[str, Any]]:
    """
    Return a list of dictionaries for SHOW INDEX FROM `table`.
    Keys include 'Key_name', 'Column_name', 'Seq_in_index', etc.
    """
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SHOW INDEX FROM `{table}`;")
    indexes = cursor.fetchall()
    cursor.close()
    return indexes