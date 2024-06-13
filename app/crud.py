from sqlalchemy.orm import Session

import app.models as models


def create_query(db: Session, query: str, completion: str):
    db_query = models.Query(prompt=query, completion=completion)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_queries(db: Session, skip=0, limit=4):
    return db.query(models.Query).order_by(models.Query.id.desc()).offset(skip).limit(limit).all()

