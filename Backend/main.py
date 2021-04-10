from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import Database


database = Database()
database.create_db()
app = FastAPI()


@app.post("/admin/", response_model=schemas.ResponseAdmin)
def create_admin(admin: schemas.CreateAdmin, db: Session = Depends(database.get_db)):
    return crud.create_admin(db=db, admin=admin)


@app.get("/admin/", response_model=schemas.ResponseAdmin)
def get_admin(db: Session = Depends(database.get_db)):
    return crud.get_admin(db)

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(database.get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user



