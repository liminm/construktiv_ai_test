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
    res =  crud.get_queries(db,limit = 10000)
    return res
