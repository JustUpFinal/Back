from fastapi import FastAPI
from app.database import Database
from .routers import cameras
from starlette.middleware.cors import CORSMiddleware

origins = ["*"]    
db = Database 
app = FastAPI()



@app.on_event("startup")
async def startup():
    await db.create_pool(db)
    
    
@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await db.close(db)
    

app.include_router(cameras.router)
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)