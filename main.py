from fastapi import FastAPI
from utils import get_conn

app = FastAPI()

@app.get('/')
def read_root():
    return {'Message':'Hello from Root'}

@app.get('/employees')
def get_employees():
    conn = get_conn()
    cur = conn.cursor()
    script = 'SELECT * FROM employees'
    # value = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

