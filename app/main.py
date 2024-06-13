from fastapi import FastAPI

from app.routers.root import router as root_router
from app.routers.queries import router as queries_router
import app.models as models 
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(root_router)
app.include_router(queries_router, prefix="/queries", tags=["queries"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)