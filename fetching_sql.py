import pandas as pd
import psycopg2

# Replace with your credentials
db_name = "your_database_name"
db_user = "your_username"
db_password = "your_password"
db_host = "your_host"
db_port = "your_port"

sql_query = "SELECT * FROM your_app_name_your_model_name"  # Replace with your table name

try:
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
    cur = conn.cursor()
    cur.execute(sql_query)
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=[col.name for col in cur.description])
    conn.close()
    print("Data fetched successfully!")

    # Explore and analyze data (optional)
    print(df.head())
    print(df.info())
except Exception as e:
    print("Error:", e)
    conn.close()
