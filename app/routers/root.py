from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI
from database import SessionLocal, get_db

from settings import OPENAI_API_KEY, SYSTEM_PROMPT, MAX_TOTAL_TOKENS
from models import Query
from crud import create_query
import crud


router = APIRouter()


@router.get("/")
async def root(db = Depends(get_db)):
    prior_queries =  crud.get_queries(db,limit = 10000)

    if not prior_queries:
        return {"message": "As soon as you write your first prompt it will appear here!"}
    return prior_queries
