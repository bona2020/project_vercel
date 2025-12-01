import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('database_link')

def get_conn():
    conn=psycopg2.connect(db_url)
    return conn