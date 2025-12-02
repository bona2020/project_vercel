from fastapi import APIRouter
from psycopg2.extras import RealDictCursor
from utils import get_conn

router = APIRouter(tags=['Products'])



#====================================================================
# 1. GET ALL THE PRODUCTS
@router.get('/get_products')
def get_products():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM products ORDER BY product_id ASC'
    # value = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 2. GET PRODUCT BY ID
@router.get('/get_product/{product_id}')
def get_product_id(product_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT * FROM products WHERE product_id = %s'
    value = (product_id,)
    cur.execute(script,value)
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Product ID':f'[{product_id}] not found'}
    return update
#====================================================================
# X. COUNT ALL PRODUCT BY ID
@router.get('/count_product/')
def count_product():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'SELECT COUNT(product_id) FROM products ;'
    # value = ()
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 3. CREATE A PRODUCT 
@router.post('/create_product')
def create_product(product_id,product_name,category,price):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'INSERT INTO products values (%s,%s,%s,%s) RETURNING product_id,product_name,category,price'
    value = (product_id,product_name,category,price)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update

#====================================================================
# 4. UPDATE A PRODUCT
@router.put('/update_product')
def update_product(product_id,product_name,category,price):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'UPDATE products SET  product_name =%s, category = %s, price = %s  where product_id = %s  RETURNING product_id,product_name,category,price'
    value = (product_name,category,price,product_id)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    if not update :
        return {'Product ID':f'[{product_id}] not found'}
    return update
#====================================================================
# 5. DELETE A PRODCUT BY ID
@router.delete('/delete_product/{product_id}')
def delete_product(product_id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    script = 'DELETE FROM products WHERE product_id = %s RETURNING product_id,product_name,category,price'
    value = (product_id,)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchone()
    cur.close()
    conn.close()
    if not update :
        return {'Product ID':f'[{product_id}] not found'}
    return update
