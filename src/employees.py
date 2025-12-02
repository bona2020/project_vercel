from fastapi import APIRouter
from psycopg2.extras import RealDictCursor
from utils import get_conn

router = APIRouter(tags=['Employees'])

#====================================================================
# 1. GET ALL THE EMPLOYEES
@router.get('/get_employees')
def get_employees():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM employees ORDER BY employee_id ASC'
    # value = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 2. GET EMPLOYEE BY ID
@router.get('/get_employee/{employee_id}')
def get_employee_id(employee_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM employees WHERE employee_id = %s'
    value = (employee_id,)
    cur.execute(script,value)
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Employee ID':f'[{employee_id}] not found'}
    return update
#====================================================================
# X. COUNT ALL EMPLOYEES BY ID
@router.get('/count_employee/')
def count_employee():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT COUNT(employee_id) FROM employees ;'
    # value = ()
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 3. CREATE EMPLOYEE 
@router.post('/create_employee')
def create_employee(employee_id,name,position,region):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'INSERT INTO employees values (%s,%s,%s,%s) RETURNING employee_id,name,position,region'
    value = (employee_id,name,position,region)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 4. UPDATE AN EMPLOYEE
@router.put('/update_employee')
def update_employee(employee_id,name,position,region):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'UPDATE employees SET  name= %s, position=%s, region=%s where employee_id = %s  RETURNING employee_id,name,position,region'
    value = (name,position,region,employee_id)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    if not update :
        return {'Employee ID':f'[{employee_id}] not found'}
    return update
#====================================================================
# 5. DELETE AN EMPLOYEE BY ID
@router.delete('/delete_employee/{employee_id}')
def delete_employee(employee_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'DELETE FROM employees WHERE employee_id = %s RETURNING employee_id,name,position,region'
    value = (employee_id,)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Employee ID':f'[{employee_id}] not found'}
    return update
