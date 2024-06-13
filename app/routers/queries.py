from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI
from app.database import get_db

from app.settings import OPENAI_API_KEY, SYSTEM_PROMPT
from app.routers.utils import get_prior_queries, calculate_tokens, token_limit_exceeded
from app.crud import create_query


router = APIRouter()


client = OpenAI(
    api_key=OPENAI_API_KEY,
)

@router.get("/query")
def query(
    user_prompt: str, 
    mood: str = "funny",
    language: str = "English",
    system_prompt: str = SYSTEM_PROMPT, 
    conversation_context_limit: int = 4,
    max_total_tokens: int = 1000,
    db = Depends(get_db)
):
    extended_system_prompt = f"{system_prompt}\nMOOD: {mood}\nLANGUAGE: {language}"
    print(extended_system_prompt)

    # Defines how far back in the conversation history the model should look for context
    db_prior_queries = get_prior_queries(db, conversation_context_limit)

    if db_prior_queries:
        prior_queries = [f"CURRENT PROMPT: {query.prompt} COMPLETION: {query.completion}\n" for query in db_prior_queries]
        extended_user_prompt = f"{user_prompt}\nPRIOR CONVERSATION: {prior_queries}"
    else:
        extended_user_prompt = user_prompt

    # Intercept the request if the token limit is exceeded
    try:
        total_tokens = calculate_tokens(extended_user_prompt) + calculate_tokens(extended_system_prompt)
        token_limit_exceeded(total_tokens, max_total_tokens)
    except ValueError as e:
        raise HTTPException(status_code=429, detail=str(e))

    extended_system_prompt = f"{system_prompt}\nMOOD: {mood}\nLANGUAGE: {language}"
    print(extended_system_prompt)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": extended_system_prompt},
            {"role": "user", "content": extended_user_prompt}
        ]
    )

    if completion.choices[0].finish_reason == "length":
        raise HTTPException(status_code=400, detail="Token limit exceeded")
    
    db_query = create_query(db, user_prompt, completion.choices[0].message.content)

    return db_query

