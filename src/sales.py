from fastapi import APIRouter
from utils import get_conn
from psycopg2.extras import RealDictCursor


router = APIRouter(tags=['Sales'])


#====================================================================
# 1. GET ALL THE SALES
@router.get('/get_sales')
def get_sales():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM sales ORDER BY sale_id ASC'
    # value = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 2. GET SALES BY ID
@router.get('/get_sale/{sale_id}')
def get_sale_id(sale_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM sales WHERE sale_id = %s'
    value = (sale_id,)
    cur.execute(script,value)
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Sale ID':f'[{sale_id}] not found'}
    return update
#====================================================================
# X. COUNT ALL SALES BY ID
@router.get('/count_sale/')
def count_sale():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT COUNT(employee_id) FROM sales ;'
    # value = ()
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#====================================================================
# X. GET  ALL SALES BY DETALIS
@router.get('/detail_sale')
def detali_sale():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = '''select s.sale_id , s.sale_date , p.product_name ,e.name , s.quantity ,s.total_amount 
                from public.sales s 
                join public.employees e  on s.employee_id  = e.employee_id
                join products p   on s.product_id  = p.product_id  
                 ORDER BY sale_id ASC ;'''
    # value = ()
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 3. CREATE A SALE 
@router.post('/create_sale')
def create_sale(sale_id,sale_date,product_id,employee_id,quantity,total_amount):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'INSERT INTO sales values (%s,%s,%s,%s,%s,%s) RETURNING sale_id,sale_date,product_id,employee_id,quantity,total_amount'
    value = (sale_id,sale_date,product_id,employee_id,quantity,total_amount)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 4. UPDATE A SALE
@router.put('/update_sale')
def update_sale(sale_id,sale_date,product_id,employee_id,quantity,total_amount):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'UPDATE sales SET  sale_date =%s, product_id=%s, employee_id =%s, quantity=%s, total_amount=%s where sale_id =%s  RETURNING sale_id,sale_date,product_id,employee_id,quantity,total_amount'
    value = (sale_date,product_id,employee_id,quantity,total_amount,sale_id)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    if not update :
        return {'Sale ID':f'[{product_id}] not found'}
    return update
#====================================================================
# 5. DELETE A SALE BY ID
@router.delete('/delete_sale/{sale_id}')
def delete_sale(sale_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'DELETE FROM sales WHERE sale_id = %s RETURNING sale_id,sale_date,product_id,employee_id,quantity,total_amount'
    value = (sale_id,)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Sale ID':f'[{sale_id}] not found'}
    return update

