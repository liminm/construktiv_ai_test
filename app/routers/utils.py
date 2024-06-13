from app import crud


def get_prior_queries(db, context_limit):
    # Get the prior conversation from the database
    prior_queries = crud.get_queries(db=db, limit=context_limit)[::-1]
    return prior_queries


def calculate_tokens(text):
    token_count = len(text) // 4
    return token_count


def token_limit_exceeded(token_count, limit= 100000):
    # Throw an exception if the token limit is exceeded
    if token_count > limit:
        raise ValueError("Token limit exceeded")
    return token_count