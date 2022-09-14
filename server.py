from fastapi import FastAPI
from src.infra.sqlalchemy.config.configs import criar_db
from src.routers import router_auth, router_product, router_orders



criar_db()
app = FastAPI()

app.include_router(router_auth.router, prefix='/auth')
app.include_router(router_product.router, prefix='/product')
app.include_router(router_orders.router, prefix='/orders')

