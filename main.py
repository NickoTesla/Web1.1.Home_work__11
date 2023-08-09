from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from db import get_db


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}




@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")