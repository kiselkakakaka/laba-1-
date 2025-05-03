
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import *
from app.schemas import Token
from app.dependencies import get_db
from app.crud import get_user_by_username

router = APIRouter()

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect credentials")

    access_token = create_access_token({"sub": user.username})
    refresh_token = create_refresh_token({"sub": user.username})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
async def refresh_token(request: Request):
    data = await request.json()
    refresh = data.get("refresh_token")
    if not refresh:
        raise HTTPException(status_code=400, detail="Refresh token required")
    try:
        payload = decode_refresh_token(refresh)
        username = payload.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = create_access_token({"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
