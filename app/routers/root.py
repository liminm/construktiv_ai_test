from fastapi import APIRouter, Depends

from app.database import get_db
import app.crud as crud


router = APIRouter()


@router.get("/")
async def root(db = Depends(get_db)):
    prior_queries =  crud.get_queries(db,limit = 10000)

    if not prior_queries:
        return {"message": "As soon as you write your first prompt it will appear here! To do this visit localhost:8000/docs and click on the POST /queries endpoint."}
    return prior_queries
