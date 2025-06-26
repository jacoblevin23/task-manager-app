# This module contains utility functions for database operations.

def dict_from_cursor(cursor):
    """Optional: convert cursor result to dicts if not using dict=True"""
    cols = [col[0] for col in cursor.description]
    return [dict(zip(cols, row)) for row in cursor.fetchall()]
