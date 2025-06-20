import uvicorn
from config import REP

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.user.router import router_user
from app.core.DAO.router import dao_router
from app.core.group.router import group_router
from app.core.brand.router import router_brand
from app.core.contract.router import router_contract
from app.core.basket.router import basket_router
from app.core.nomenclature.router import nomenclature_router
from app.core.picture.router import router_picture
from app.core.favorite.router import favorite_router
from app.core.user_matrix.router import router_representative_data

app = FastAPI(title="SSK API",
              description="🐇",
              version="1.2.0")


origins = [
    "http://localhost:5173"
    # "http://бриола42.рф",
    # "http://xn--42-6kcd9asuo.xn--p1ai",
    # "http://uslada.nvadm.ru",
    # "http://158.46.50.214",
]

app.mount("/static", StaticFiles(directory="templates"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", description="Hello world!")
async def say_hello():
    return REP

app.include_router(router_user)
app.include_router(dao_router)
app.include_router(router_brand)
app.include_router(router_contract)
app.include_router(basket_router)
app.include_router(group_router)
app.include_router(nomenclature_router)
app.include_router(favorite_router)
app.include_router(router_picture)
app.include_router(router_representative_data)

if __name__ == "__main__":
    uvicorn.run("core:app", log_level="info", reload=True, host="127.0.0.1", port=8000)
 

