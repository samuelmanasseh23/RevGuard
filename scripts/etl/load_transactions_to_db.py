import pandas as pd
import sqlite3
from pathlib import Path


def load_transactions():

    db_path = Path("database/revguard.db")
    data_path = Path("data/raw/transactions.csv")

    # connect to database
    conn = sqlite3.connect(db_path)

    try:
        print("Loading dataset...")

        df = pd.read_csv(data_path)

        print(f"Records found: {len(df)}")

        # write to SQL table
        df.to_sql(
            "transactions",
            conn,
            if_exists="replace",
            index=False
        )

        print("Transactions successfully loaded into database")

    except Exception as e:
        print("Error loading transactions:", e)

    finally:
        conn.close()
        print("Database connection closed")


if __name__ == "__main__":
    load_transactions()