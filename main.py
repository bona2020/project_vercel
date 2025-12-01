from fastapi import FastAPI
from utils import get_conn
from src.employees import router as employee_router
from src.products import router as product_router
from src.sales import router as sales_router

app = FastAPI(tags=['Root'])


@app.get('/')
def read_root():
    return {'Message':'Hello from Root'}


app.include_router(employee_router)
app.include_router(product_router)
app.include_router(sales_router)





