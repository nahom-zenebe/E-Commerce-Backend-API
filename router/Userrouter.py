# app/routers/auth_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db, Base, engine
from service.Userservice import Userservice
from schemas.Userschemas import UserCreate, UserResponse, Token, TokenPayload
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from core.security import decode_jwt_token
from typing import Dict

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # used for dependency on protected routes

# Create DB tables if not exist (simple approach)
Base.metadata.create_all(bind=engine)

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    svc = Userservice(db)
    user = svc.signup(user_in)
    return user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Use form fields: username, password (OAuth2PasswordRequestForm uses 'username' field)
    We'll treat 'username' as email.
    """
    svc = Userservice(db)
    user = svc.authenticate(email=form_data.username, password=form_data.password)
    tokens = svc.create_tokens_for_user(user.id)
    return {
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"],
        "token_type": "bearer"
    }

@router.post("/refresh", response_model=Token)
def refresh(refresh_token: str, db: Session = Depends(get_db)):
    svc = Userservice(db)
    payload = svc.decode_and_verify(refresh_token, expected_type="refresh")
    # optional: revoke old refresh token and issue new refresh token (rotate)
    # here we'll just issue new access token
    tokens = svc.create_tokens_for_user(int(payload.sub))
    return {
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"],  # rotated refresh token
        "token_type": "bearer"
    }

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(token: str, token_type: str = "refresh", db: Session = Depends(get_db)):
    """
    Logout by revoking the provided token (token param should be the raw JWT string).
    token_type should be 'access' or 'refresh' depending on which token you revoke.
    """
    svc = Userservice(db)
    payload = svc.decode_and_verify(token, expected_type=token_type)
    svc.revoke_token_by_jti(payload.jti, token_type=token_type)
    return None


@router.get("/me", response_model=UserResponse)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    svc = Userservice(db)
    payload = svc.decode_and_verify(token, expected_type="access")
    user = svc.user_repo.get_by_id(int(payload.sub))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
