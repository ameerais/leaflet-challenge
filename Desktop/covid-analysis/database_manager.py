

import sqlite3
import pandas as pd

def save_to_database(df, db_name):
    """
    Save the cleaned DataFrame to an SQLite database.

    Args:
    df (pd.DataFrame): Cleaned data.
    db_name (str): Database file name.
    """
    conn = sqlite3.connect(db_name)
    try:
        df.to_sql('conditions', conn, if_exists='replace', index=False)
        print(f"Data saved to database '{db_name}'.")
    except Exception as e:
        print(f"Error saving to database: {e}")
    finally:
        conn.close()

def fetch_data_from_db(db_name):
    """
    Fetch the data from the SQLite database.

    Args:
    db_name (str): Database file name.

    Returns:
    pd.DataFrame: Data retrieved from the database.
    """
    conn = sqlite3.connect(db_name)
    try:
        query = "SELECT * FROM conditions"
        df = pd.read_sql(query, conn)
        print(f"Data fetched from database '{db_name}'.")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        conn.close()
