from fastapi import FastAPI

from app.routers.queries import router as queries_router
from settings import OPENAI_API_KEY
import crud
import models 
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(queries_router, prefix="/queries", tags=["queries"])




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)